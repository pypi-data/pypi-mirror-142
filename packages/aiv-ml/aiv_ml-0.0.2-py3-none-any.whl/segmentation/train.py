import os
import os.path as osp
import sys 
from pathlib import Path 
import time
import datetime 
import collections
import matplotlib.pyplot as plt 
from threading import Event
# sys.path.append(osp.join(osp.dirname(__file__), 'src'))
# sys.path.append(osp.join(osp.dirname(__file__), 'src/utils'))
# sys.path.append(osp.join(osp.dirname(__file__), 'models'))

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
print("** SEGMENTATION FILE: ", FILE)
print("** SEGMENTATION ROOT: ", ROOT)
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
print("** SEGMENTATION SYS PATH: ", sys.path)

# sys.path.append(osp.join(osp.dirname(__file__), '../utils'))

### deep learning library
import torch
import torch.utils.data
import torchvision
from torch import nn

### utils & datasets & arguments for training 
from src.losses import CELoss, DiceLoss
from src.coco_utils import get_coco, get_mask
from configs.parse_cfgs import parse_train_cfgs
import src.presets as presets
import src.utils as utils
import wandb

### models 
from models.modeling import Create_Model

### ignore warnings
import warnings
warnings.filterwarnings(action='ignore') 

### logging
from utils.logger import get_root_logger

class Segmentation():
    def __init__(self, verbose_args=False):
        self.e_stop = Event()
        self.verbose_args = verbose_args
        self.args = None
        self.logger = None
        self.scaler = None 
        self.reset()

    def get_args(self, cfgs_model_fp, cfgs_project_fp, verbose=False):
        self.args = parse_train_cfgs(cfgs_model_fp=cfgs_model_fp, cfgs_project_fp=cfgs_project_fp, verbose=verbose)
        self.logger = get_root_logger(name='train', log_file=osp.join(self.args.log_path, 'train.log'))
        
        if self.args.amp:
            self.logger.info("The scaler is set by AMP")
            self.scaler = torch.cuda.amp.GradScaler()

    def stop(self):
        self.e_stop.set()

    def reset(self):
        if self.logger is not None:
            self.logger.info("Reset all .......!!!!!!!")

        self.epoch = 0
        self.e_stop = Event()
        self.min_loss = 999
        self.info_weights = {'best': None, 'last': None}
        self.start_time = time.time()

    def set_datasets(self):      
        def get_dataset(dir_path, dataset_type, mode, transform, num_classes):
            paths = {
                "coco": (dir_path, get_coco, num_classes),
                "mask": (dir_path, get_mask, num_classes),
            }

            ds_path, ds_fn, num_classes = paths[dataset_type]
            ds = ds_fn(ds_path, mode=mode, transforms=transform, num_classes=num_classes)
            return ds, num_classes

        def get_transform(train, base_size, crop_size):
            return presets.SegmentationPresetTrain(base_size, crop_size) if train else presets.SegmentationPresetEval(base_size)
        
        dataset, num_classes = get_dataset(self.args.data_path, self.args.dataset_type, "train", 
                                        get_transform(True, self.args.base_imgsz, self.args.crop_imgsz), self.args.num_classes)

        assert num_classes == self.args.num_classes
                                            
        dataset_test, _ = get_dataset(self.args.data_path, self.args.dataset_type, "val", 
                                            get_transform(False, self.args.base_imgsz, self.args.crop_imgsz), self.args.num_classes)

        # if self.args.distributed:
        #     self.train_sampler = torch.utils.data.distributed.DistributedSampler(dataset)
        #     self.test_sampler = torch.utils.data.distributed.DistributedSampler(dataset_test)
        # else:
        #     self.train_sampler = torch.utils.data.RandomSampler(dataset)
        #     self.test_sampler = torch.utils.data.SequentialSampler(dataset_test)
        self.train_sampler = torch.utils.data.RandomSampler(dataset)
        self.test_sampler = torch.utils.data.SequentialSampler(dataset_test)
        
        self.data_loader_train = torch.utils.data.DataLoader(dataset, batch_size=self.args.batch_size,
                                                            sampler=self.train_sampler, num_workers=self.args.num_workers,
                                                            collate_fn=utils.collate_fn, drop_last=True,
                                                            pin_memory=True)

        self.data_loader_test = torch.utils.data.DataLoader(dataset_test, batch_size=1,
                                                            sampler=self.test_sampler, num_workers = self.args.num_workers,
                                                            collate_fn = utils.collate_fn, pin_memory=True)


    def set_model(self):
        ### SET MODEL -------------------------------------------------------------------------------------------------------
        self.model, params_to_optimize = Create_Model(self.args)
        self.logger.info(f"LOADED MODEL: {self.args.model}")

        # if self.args.distributed:
        #     model = torch.nn.SyncBatchNorm.convert_sync_batchnorm(self.model)

        self.model_without_ddp = self.model

        if self.args.optimizer == 'Adam':
            self.optimizer = torch.optim.Adam(params_to_optimize, lr=self.args.lr, weight_decay=self.args.weight_decay)
        elif self.args.optimizer == 'SGD':
            self.optimizer = torch.optim.SGD(params_to_optimize, lr=self.args.lr, momentum=self.args.momentum,
                                nesterov=self.args.nesterov, weight_decay=self.args.weight_decay)
        elif self.args.optimizer == 'AdamW':
            from transformers import AdamW
            self.optimizer = AdamW(params_to_optimize, lr=0.00006)
        else:
            raise NotImplementedError


        iters_per_epoch = len(self.data_loader_train)
        if self.args.lr_scheduler == 'LambdaLR':
            main_lr_scheduler = torch.optim.lr_scheduler.LambdaLR(
                self.optimizer, lambda x: (1 - x / (iters_per_epoch * (self.args.epochs - self.args.lr_warmup_epochs))) ** 0.9
            )
        elif self.args.lr_scheduler == 'PolyLR':
            main_lr_scheduler = utils.PolyLR(self.optimizer, 30e3, power=0.9)


        ##########################################################################################################################    
        ### Important! Need to locate parallel training settings after parameter settings for optimization !!!!!!!!!!!!!!!!!!!!!!!
        ##########################################################################################################################
        self.model.to(self.args.device)
        # if self.args.distributed:
        #     self.model = torch.nn.parallel.DistributedDataParallel(self.model, device_ids=[self.args.gpu])
        #     self.model_without_ddp = self.model

        if len(self.args.device_ids): 
            self.logger.info("The algiorithm is executed by nn.DataParallel on devices: {}".format(self.args.device_ids))
            self.model = torch.nn.DataParallel(self.model, device_ids=self.args.device_ids, output_device=self.args.device_ids[0])

        ### SET LOSS FUNCTION -----------------------------------------------------------------------------------------------
        if self.args.loss == 'CE':
            self.criterion = CELoss(self.args.aux_loss)
        elif self.args.loss == 'DiceLoss':
            self.criterion = DiceLoss(self.args.num_classes, False)
        elif self.args.loss == 'BceDiceLoss':
            self.criterion = DiceLoss(self.args.num_classes, True)


        ### SET TRAIN PARAMETERS -------------------------------------------------------------------------------------------
        if self.args.lr_warmup_epochs > 0:
            warmup_iters = iters_per_epoch*self.args.lr_warmup_epochs
            self.args.lr_warmup_method = self.args.lr_warmup_method.lower()
            if self.args.lr_warmup_method == "linear":
                # warmup_lr_scheduler = torch.optim.lr_scheduler.LinearLR(
                warmup_lr_scheduler = utils.LinearLR(
                    self.optimizer, start_factor=self.args.lr_warmup_decay, total_iters=warmup_iters
                )
            elif self.args.lr_warmup_method == "constant":
                # warmup_lr_scheduler = torch.optim.lr_scheduler.ConstantLR(
                warmup_lr_scheduler = utils.ConstantLR(
                    self.optimizer, factor=self.args.lr_warmup_decay, total_iters=warmup_iters
                )
            else:
                self.logger.error(f"Invalid warmup lr method '{self.args.lr_warmup_method}'. Only linear and constant are supported.")
                raise RuntimeError(
                    f"Invalid warmup lr method '{self.args.lr_warmup_method}'. Only linear and constant are supported."
                )
            # lr_scheduler = torch.optim.lr_scheduler.SequentialLR(
            self.lr_scheduler = utils.SequentialLR(
                self.optimizer, schedulers=[warmup_lr_scheduler, main_lr_scheduler], milestones=[warmup_iters]
            )
        else:
            self.lr_scheduler = main_lr_scheduler

        if self.args.weights:
            try:
                checkpoint = torch.load(self.args.weights, map_location="cpu")
                self.model_without_ddp.load_state_dict(checkpoint["model"], strict=True)

                self.optimizer.load_state_dict(checkpoint["optimizer"])
                self.lr_scheduler.load_state_dict(checkpoint["lr_scheduler"])
                self.args.start_epoch = checkpoint["epoch"] + 1

                if self.args.amp:
                    self.scaler.load_state_dict(checkpoint['scaler'])

                self.logger.info("RELOAD ALL !!!!!!!!!!!!!!!!!!!!!!!!!!")
            except:
                pass
        else:
            self.logger.info("No pretrained weights ....................")

    def set_wandb(self):
        if self.args.wandb:
            self.wandb.init(project=self.args.project_name, reinit=True)
            if self.args.data_path.split('/')[-2].split('_')[-1] == 'good' or self.args.with_good:
                self.wandb.run.name = self.args.run_name + '_' + self.args.model + '_good'
            else:    
                self.wandb.run.name = self.args.run_name + '_' + self.args.model
            self.wandb.config.update(self.args)
            self.wandb.watch(self.model)

    @torch.inference_mode()
    def validate(self):
        self.model.eval()
        confmat = utils.ConfusionMatrix(self.args.num_classes)
        metric_logger = utils.MetricLogger(delimiter="  ")
        header = "Test:"
        losses = 0
        with torch.inference_mode():
            for image, target, fn in metric_logger.log_every(self.data_loader_test, 100, header):
                if self.e_stop.isSet():
                    self.logger.info("EMERGENCY STOP the training . . . . . . . . ! ! !")

                    break
                image, target = image.to(self.args.device), target.to(self.args.device)

                if self.args.deep_supervision:
                    outputs = self.model(image)
                    loss = 0
                    for output in outputs:
                        loss += self.criterion(output, target)
                    loss /= len(outputs)
                else:
                    output = self.model(image)
                    if self.args.model.split('_')[0] == 'segformer':
                        output = nn.functional.interpolate(output.logits, size=target.shape[-2:], mode="bilinear", align_corners=False)
                    loss = self.criterion(output, target)
                if isinstance(output, collections.OrderedDict) and 'out' in output.keys():
                    output = output['out']

                losses += loss.item() 
                confmat.update(target.flatten(), output.argmax(1).flatten())
            confmat.reduce_from_all_processes()


            acc_global, acc, iu = confmat.compute()
            if self.args.wandb and self.wandb != None:
                self.wandb.log({"val_loss": losses.item()})
                
                for class_name, val in zip(self.args.classes, (iu*100).tolist()):
                    self.wandb.log({class_name + '_iou': val})
                self.wandb.log({'mean iou': iu.mean().item()*100})
                for class_name, val in zip(self.args.classes, (acc*100).tolist()):
                    self.wandb.log({class_name + '_acc': val})
                
            checkpoint = {
                "model": self.model_without_ddp.state_dict(),
                "optimizer": self.optimizer.state_dict(),
                "lr_scheduler": self.lr_scheduler.state_dict(),
                "epoch": self.epoch,
                "args": self.args,
            }

            if self.args.amp:
                checkpoint['scaler'] = self.scaler.state_dict()

            if self.min_loss > losses:
                min_loss = losses
                utils.save_on_master(checkpoint, os.path.join(self.args.weights_path, "best.pth"))
                if self.args.model.split('_')[0] == 'segformer':
                    self.model.module.save_pretrained(os.path.join(self.args.weights_path, './best'))

                self.info_weights['best'] = self.epoch
                self.logger.info("Saved the best model . . . . . . . . .")

            utils.save_on_master(checkpoint, os.path.join(self.args.weights_path, "last.pth"))
            if self.args.model.split('_')[0] == 'segformer':
                    self.model.module.save_pretrained(os.path.join(self.args.weights_path, './last'))

            self.info_weights['last'] = self.epoch

            with open(osp.join(self.args.weights_path, 'info.txt'), 'w') as f:
                f.write('best: {}'.format(self.info_weights['best']))
                f.write('\n')
                f.write('last: {}'.format(self.info_weights['last']))
                f.write('\n')    

        return confmat, losses

    def train_one_epoch(self):
        self.model.train()
        metric_logger = utils.MetricLogger(delimiter="  ")
        metric_logger.add_meter("lr", utils.SmoothedValue(window_size=1, fmt="{value}"))
        header = f"Epoch: [{self.epoch}]"
        losses = 0
        self.epoch += 1
        for image, target, fn in metric_logger.log_every(self.data_loader_train, self.args.print_freq, header):
            # plt.imshow(image[0].permute(1, 2, 0).detach().numpy())
            # plt.imshow(target[0].unsqueeze(0).permute(1, 2, 0).detach().numpy(), alpha=0.8)
            # plt.show()
            if self.e_stop.isSet():
                self.logger.info("EMERGENCY STOP the training * * * * * * * * *")
                # break
                return 
        
            ### to check if the mask image has wrong value .....
            # import numpy as np
            # for batch in target:
            #     values = np.unique(batch)
            #     print(values)
            #     for value in values:
            #         if value < 255 and value >= len(self.args.classes) + 1:
            #             raise Exception(f"There is unwanted value: {values} in {fn}")
                
            image, target = image.to(self.args.device), target.to(self.args.device)
            with torch.cuda.amp.autocast(enabled=self.scaler is not None):
                if self.args.deep_supervision: 
                    outputs = self.model(image)     
                    loss = 0
                    for output in outputs:
                        loss += self.criterion(output, target)
                    loss /= len(outputs)
                else:
                    output = self.model(image)   

                    if self.args.model.split('_')[0] == 'segformer':
                        output = nn.functional.interpolate(output.logits, size=target.shape[-2:], mode="bilinear", align_corners=False)
                        # predicted = upsampled_logits.argmax(dim=1)

                        # mask = (labels != 255) # we don't include the background class in the accuracy calculation
                        # pred_labels = predicted[mask].detach().cpu().numpy()
                        # true_labels = labels[mask].detach().cpu().numpy()
                        # accuracy = accuracy_score(pred_labels, true_labels)
                        # loss = outputs.loss
                        # accuracies.append(accuracy)
                        # losses.append(loss.item())
                        # pbar.set_postfix({'Batch': idx, 'Pixel-wise accuracy': sum(accuracies)/len(accuracies), 'Loss': sum(losses)/len(losses)})

                    loss = self.criterion(output, target)

            losses += loss.item()
            self.optimizer.zero_grad()

            if self.scaler is not None:
                self.scaler.scale(loss).backward()
                self.scaler.step(self.optimizer)
                self.scaler.update()
            else:
                loss.backward()
                self.optimizer.step()

            self.lr_scheduler.step()

            # logging >>>
            metric_logger.update(loss=loss.item(), lr=self.optimizer.param_groups[0]["lr"])
            if self.wandb != None and self.args.wandb:
                self.wandb.log({"train_loss": loss.item(), "learning rate": self.optimizer.param_groups[0]["lr"]})
        
        return losses
         
    def train_(self):
        self.logger.info("Start training > > > > > > > >")
        min_loss = 999
        info_weights = {'best': None, 'last': None}
        start_time = time.time()
        for _ in range(self.args.start_epoch, self.args.epochs):
            # if self.args.distributed:
            #     self.train_sampler.set_epoch(self.epoch)

            self.train_one_epoch()
            confmat, loss_val = self.validate()
                
            acc_global, acc, iu = confmat.compute()
            if self.args.wandb and self.wandb != None:
                self.wandb.log({"val_loss": loss_val.item()})
                
                for class_name, val in zip(self.args.classes, (iu*100).tolist()):
                    self.wandb.log({class_name + '_iou': val})
                self.wandb.log({'mean iou': iu.mean().item()*100})
                for class_name, val in zip(self.args.classes, (acc*100).tolist()):
                    self.wandb.log({class_name + '_acc': val})
                
            self.logger.info(self.args.classes)
            self.logger.info(confmat)
            checkpoint = {
                "model": self.model_without_ddp.state_dict(),
                "optimizer": self.optimizer.state_dict(),
                "lr_scheduler": self.lr_scheduler.state_dict(),
                "epoch": self.epoch,
                "args": self.args,
            }

            if min_loss > loss_val:
                min_loss = loss_val
                utils.save_on_master(checkpoint, os.path.join(self.args.weights_path, "best.pth"))
                info_weights['best'] = self.epoch
                self.logger.info("Saved the best model ! ")
            utils.save_on_master(checkpoint, os.path.join(self.args.weights_path, "last.pth"))
            info_weights['last'] = self.epoch

            with open(osp.join(self.args.weights_path, 'info.txt'), 'w') as f:
                f.write('best: {}'.format(info_weights['best']))
                f.write('\n')
                f.write('last: {}'.format(info_weights['last']))
                f.write('\n')    
            
        total_time = time.time() - start_time

        total_time_str = str(datetime.timedelta(seconds=int(total_time)))
        self.logger.info(f"Training time {total_time_str}")


    def train(self):
        self.train_()

if __name__ == "__main__":

    seg = Segmentation()
    cfgs_model_fp = './configs/models/deeplabv3/{}.yaml'.format('deeplabv3plus_resnet101')
    # cfgs_model_fp = './configs/models/segformer/{}.yaml'.format('segformer')
    cfgs_project_fp = './configs/projects/interojo_s_factory.yaml'
    seg.get_args(cfgs_model_fp, cfgs_project_fp)
    seg.set_datasets()
    seg.set_model()
    if seg.args.wandb:
        seg.wandb = wandb
        seg.set_wandb()
    else:
        seg.wandb = None

    seg.epoch = 0

    seg.train()