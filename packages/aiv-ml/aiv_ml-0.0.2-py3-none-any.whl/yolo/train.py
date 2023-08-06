from ast import Call
import math
import os
import random
import sys
from tabnanny import verbose
import time
from copy import deepcopy
from datetime import datetime
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import yaml
from torch.cuda import amp
from torch.optim import SGD, Adam, lr_scheduler
from tqdm import tqdm
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
print("** DETECTION FILE: ", FILE)
print("** DETECTION ROOT: ", ROOT)
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
print("** DETECTION SYS PATH: ", sys.path)

import val  # for end-of-epoch mAP\
from models.experimental import attempt_load
from models.yolo import Model
from utils.autoanchor import check_anchors
from utils.autobatch import check_train_batch_size
from utils.callbacks import Callbacks
from utils.datasets import create_dataloader
from utils.downloads import attempt_download
from utils.general import (LOGGER, check_dataset, check_file, check_img_size, 
                           check_suffix, check_yaml, colorstr, get_latest_run, increment_path, init_seeds,
                           intersect_dicts, labels_to_class_weights, labels_to_image_weights, methods, one_cycle,
                           strip_optimizer)
from utils.loggers import Loggers
from utils.loss import ComputeLoss
from utils.metrics import fitness
from utils.plots import plot_labels
from utils.torch_utils import EarlyStopping, ModelEMA, de_parallel, select_device



RANK = int(os.getenv('RANK', -1))
WORLD_SIZE = int(os.getenv('WORLD_SIZE', 1))

from threading import Event 
from src.arguments import get_args_parser
import argparse 
import yaml

class Yolov5():
    def __init__(self, verbose_args=False):
        self.e_stop = Event()
        self.verbose_args = verbose_args
        self.args = argparse.Namespace() 
        self.logger = None 

        self.callbacks = Callbacks()
        self.dataset = None
        
        self._vars = argparse.Namespace()

        self.reset()

    def reset(self):
        self.e_stop.clear()

    def stop(self):
        self.e_stop.set()

    def get_args(self):
        # self.args = get_args_parser()
        # self.args = argparse.Namespace()
        self.args.desc = "yolov5"

        args_ = vars(self.args)
        with open(os.path.join(ROOT, "configs/args/interojo.yaml")) as f:
            cfgs_model = yaml.safe_load(f)
        for key, val in cfgs_model.items():
            args_[key] = val 

        self.args.data = os.path.join(ROOT, self.args.data)
        self.args.hyp = os.path.join(ROOT, self.args.hyp)
        self.args.cfg = os.path.join(ROOT, self.args.cfg)
        print(self.args)

        if self.args.resume:  # resume an interrupted run
            self._vars.ckpt = self.args.resume if isinstance(self.args.resume, str) else get_latest_run()  # specified or most recent path
            assert os.path.isfile(self._vars.ckpt), 'ERROR: --resume checkpoint does not exist'
            with open(Path(self._vars.ckpt).parent.parent / 'opt.yaml', errors='ignore') as f:
                import argparse
                self.args = argparse.Namespace(**yaml.safe_load(f))  # replace
            self.args.cfg, self.args.weights, self.args.resume = '', self._vars.ckpt, True  # reinstate
            LOGGER.info(f'Resuming training from {self._vars.ckpt}')
        else:
            self.args.data, self.args.cfg, self.args.hyp, self.args.weights, self.args.project = \
                check_file(self.args.data), check_yaml(self.args.cfg), check_yaml(self.args.hyp), str(self.args.weights), str(self.args.project)  # checks
            assert len(self.args.cfg) or len(self.args.weights), 'either --cfg or --weights must be specified'
            self.args.save_dir = str(increment_path(Path(self.args.project) / self.args.name, exist_ok=self.args.exist_ok))
        
        self.device = select_device(self.args.device, batch_size=self.args.batch_size)

        self._vars.save_dir, self._vars.epochs, self._vars.batch_size, self._vars.weights, self._vars.single_cls, self._vars.data, self._vars.cfg, self._vars.resume, self._vars.noval, self._vars.nosave, self._vars.workers, self._vars.freeze, = \
            Path(self.args.save_dir), self.args.epochs, self.args.batch_size, self.args.weights, self.args.single_cls, self.args.data, self.args.cfg, \
            self.args.resume, self.args.noval, self.args.nosave, self.args.workers, self.args.freeze

        print(">>>>>", self._vars.save_dir)


    def set_datasets(self):
        self.train_loader, self.dataset = create_dataloader(self._vars.train_path, self._vars.imgsz, self._vars.batch_size // WORLD_SIZE, self._vars.gs, self._vars.single_cls,
                                                hyp=self._vars.hyp, augment=True, cache=self.args.cache, rect=self.args.rect, 
                                                workers=self._vars.workers, image_weights=self.args.image_weights, quad=self.args.quad,
                                                prefix=colorstr('train: '), shuffle=True)
        mlc = int(np.concatenate(self.dataset.labels, 0)[:, 0].max())  # max label class
        self._vars.nb = len(self.train_loader)  # number of batches
        assert mlc < self._vars.nc, f'Label class {mlc} exceeds nc={self._vars.nc} in {self._vars.data}. Possible class labels are 0-{self._vars.nc - 1}'

        # Process 0
        if RANK in [-1, 0]:
            self.val_loader = create_dataloader(self._vars.val_path, self._vars.imgsz, self._vars.batch_size // WORLD_SIZE * 2, self._vars.gs, self._vars.single_cls,
                                        hyp=self._vars.hyp, cache=None if self._vars.noval else self.args.cache, rect=True, rank=-1,
                                        workers=self._vars.workers, pad=0.5,
                                        prefix=colorstr('val: '))[0]

            if not self._vars.resume:
                labels = np.concatenate(self.dataset.labels, 0)
                # c = torch.tensor(labels[:, 0])  # classes
                # cf = torch.bincount(c.long(), minlength=nc) + 1.  # frequency
                # model._initialize_biases(cf.to(device))
                if self.plots:
                    plot_labels(labels, self._vars.names, self._vars.save_dir)

                # Anchors
                if not self.args.noautoanchor:
                    check_anchors(self.dataset, model=self.model, thr=self._vars.hyp['anchor_t'], imgsz=self._vars.imgsz)
                self.model.half().float()  # pre-reduce anchor precision

            self.callbacks.run('on_pretrain_routine_end')

    def set_model(self):
        check_suffix(self._vars.weights, '.pt')  # check weights
        self._vars.pretrained = self._vars.weights.endswith('.pt')
        if self._vars.pretrained:
            self._vars.weights = attempt_download(self._vars.weights)  # download if not found locally
            self._vars.ckpt = torch.load(self._vars.weights, map_location=self.device)  # load checkpoint
            self.model = Model(self._vars.cfg or self._vars.ckpt['model'].yaml, ch=3, nc=self._vars.nc, anchors=self._vars.hyp.get('anchors')).to(self.device)  # create
            exclude = ['anchor'] if (self._vars.cfg or self._vars.hyp.get('anchors')) and not self._vars.resume else []  # exclude keys
            self._vars.csd = self._vars.ckpt['model'].float().state_dict()  # checkpoint state_dict as FP32
            self._vars.csd = intersect_dicts(self._vars.csd, self.model.state_dict(), exclude=exclude)  # intersect
            self.model.load_state_dict(self._vars.csd, strict=False)  # load
            LOGGER.info(f'Transferred {len(self._vars.csd)}/{len(self.model.state_dict())} items from {self._vars.weights}')  # report
        else:
            self.model = Model(self._vars.cfg, ch=3, nc=self._vars.nc, anchors=self._vars.hyp.get('anchors')).to(self.device)  # create

        # Freeze
        self._vars.freeze = [f'model.{x}.' for x in range(self._vars.freeze)]  # layers to self._vars.freeze
        for k, v in self.model.named_parameters():
            v.requires_grad = True  # train all layers
            if any(x in k for x in self._vars.freeze):
                LOGGER.info(f'freezing {k}')
                v.requires_grad = False

        # Image size
        self._vars.gs = max(int(self.model.stride.max()), 32)  # grid size (max stride)
        self._vars.imgsz = check_img_size(self.args.imgsz, self._vars.gs, floor=self._vars.gs * 2)  # verify imgsz is gs-multiple

        # Batch size
        if RANK == -1 and self._vars.batch_size == -1:  # single-GPU only, estimate best batch size
            self._vars.batch_size = check_train_batch_size(self.model, self._vars.imgsz)

        # Optimizer
        self._vars.nbs = 64  # nominal batch size
        self._vars.accumulate = max(round(self._vars.nbs / self._vars.batch_size), 1)  # accumulate loss before optimizing
        self._vars.hyp['weight_decay'] *= self._vars.batch_size * self._vars.accumulate / self._vars.nbs  # scale weight_decay
        LOGGER.info(f"Scaled weight_decay = {self._vars.hyp['weight_decay']}")

        g0, g1, g2 = [], [], []  # optimizer parameter groups
        for v in self.model.modules():
            if hasattr(v, 'bias') and isinstance(v.bias, nn.Parameter):  # bias
                g2.append(v.bias)
            if isinstance(v, nn.BatchNorm2d):  # weight (no decay)
                g0.append(v.weight)
            elif hasattr(v, 'weight') and isinstance(v.weight, nn.Parameter):  # weight (with decay)
                g1.append(v.weight)

        if self.args.adam:
            self.optimizer = Adam(g0, lr=self._vars.hyp['lr0'], betas=(self._vars.hyp['momentum'], 0.999))  # adjust beta1 to momentum
        else:
            self.optimizer = SGD(g0, lr=self._vars.hyp['lr0'], momentum=self._vars.hyp['momentum'], nesterov=True)

        self.optimizer.add_param_group({'params': g1, 'weight_decay': self._vars.hyp['weight_decay']})  # add g1 with weight_decay
        self.optimizer.add_param_group({'params': g2})  # add g2 (biases)
        LOGGER.info(f"{colorstr('optimizer:')} {type(self.optimizer).__name__} with parameter groups "
                    f"{len(g0)} weight, {len(g1)} weight (no decay), {len(g2)} bias")
        del g0, g1, g2

        # Scheduler
        if self.args.linear_lr:
            self._vars.lf = lambda x: (1 - x / (self._vars.epochs - 1)) * (1.0 - self._vars.hyp['lrf']) + self._vars.hyp['lrf']  # linear
        else:
            self._vars.lf = one_cycle(1, self._vars.hyp['lrf'], self._vars.epochs)  # cosine 1->self._vars.hyp['lrf']
        self.scheduler = lr_scheduler.LambdaLR(self.optimizer, lr_lambda=self._vars.lf)  # plot_lr_scheduler(optimizer, scheduler, epochs)

        # EMA
        self._vars.ema = ModelEMA(self.model) if RANK in [-1, 0] else None

        # Resume
        self._vars.start_epoch, self._vars.best_fitness = 0, 0.0
        if self._vars.pretrained:
            # Optimizer
            if self._vars.ckpt['optimizer'] is not None:
                self.optimizer.load_state_dict(self._vars.ckpt['optimizer'])
                self._vars.best_fitness = self._vars.ckpt['best_fitness']

            # EMA
            if self._vars.ema and self._vars.ckpt.get('ema'):
                self._vars.ema.ema.load_state_dict(self._vars.ckpt['ema'].float().state_dict())
                self._vars.ema.updates = self._vars.ckpt['updates']

            # Epochs
            self._vars.start_epoch = self._vars.ckpt['epoch'] + 1
            if self._vars.resume:
                assert self._vars.start_epoch > 0, f'{self._vars.weights} training to {self._vars.epochs} epochs is finished, nothing to resume.'
            if self._vars.epochs < self._vars.start_epoch:
                LOGGER.info(f"{self._vars.weights} has been trained for {self._vars.ckpt['epoch']} epochs. Fine-tuning for {self._vars.epochs} more epochs.")
                self._vars.epochs += self._vars.ckpt['epoch']  # finetune additional epochs

            del self._vars.ckpt, self._vars.csd

        # DP mode
        if self._vars.cuda and RANK == -1 and torch.cuda.device_count() > 1:
            self.model = torch.nn.DataParallel(self.model)

        # SyncBatchNorm
        if self.args.sync_bn and self._vars.cuda and RANK != -1:
            self.model = torch.nn.SyncBatchNorm.convert_sync_batchnorm(self.model).to(self.device)
            LOGGER.info('Using SyncBatchNorm()')


        self.set_datasets()

        # Model attributes
        nl = de_parallel(self.model).model[-1].nl  # number of detection layers (to scale self._vars.hyps)
        self._vars.hyp['box'] *= 3 / nl  # scale to layers
        self._vars.hyp['cls'] *= self._vars.nc / 80 * 3 / nl  # scale to classes and layers
        self._vars.hyp['obj'] *= (self._vars.imgsz / 640) ** 2 * 3 / nl  # scale to image size and layers
        self._vars.hyp['label_smoothing'] = self.args.label_smoothing
        self.model.nc = self._vars.nc  # attach number of classes to model
        self.model.hyp = self._vars.hyp  # attach hyperparameters to model
        self.model.class_weights = labels_to_class_weights(self.dataset.labels, self._vars.nc).to(self.device) * self._vars.nc  # attach class weights
        self.model.names = self._vars.names


    def train_one_epoch(self):
        self.model.train()
        
        # Update image weights (optional, single-GPU only)
        if self.args.image_weights:
            cw = self.model.class_weights.cpu().numpy() * (1 - self._vars.maps) ** 2 / self._vars.nc  # class weights
            iw = labels_to_image_weights(self.dataset.labels, nc=self._vars.nc, class_weights=cw)  # image weights
            self.dataset.indices = random.choices(range(self.dataset.n), weights=iw, k=self.dataset.n)  # rand weighted idx

        self._vars.mloss = torch.zeros(3, device=self.device)  # mean losses
        if RANK != -1:
            self.train_loader.sampler.set_epoch(self._vars.epoch)
        self.pbar = enumerate(self.train_loader)
        LOGGER.info(('\n' + '%10s' * 7) % ('Epoch', 'gpu_mem', 'box', 'obj', 'cls', 'labels', 'img_size'))
        if RANK in [-1, 0]:
            self.pbar = tqdm(self.pbar, total=self._vars.nb, bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}')  # progress bar
        self.optimizer.zero_grad()

        losses = 0
        for i, (imgs, targets, paths, _) in self.pbar:  
            if self.e_stop.is_set():
                break
            ni = i + self._vars.nb * self._vars.epoch  # number integrated batches (since train start)
            imgs = imgs.to(self.device, non_blocking=True).float() / 255  # uint8 to float32, 0-255 to 0.0-1.0

            # Warmup
            if ni <= self._vars.nw:
                xi = [0, self._vars.nw]  # x interp
                # compute_loss.gr = np.interp(ni, xi, [0.0, 1.0])  # iou loss ratio (obj_loss = 1.0 or iou)
                self._vars.accumulate = max(1, np.interp(ni, xi, [1, self._vars.nbs / self._vars.batch_size]).round())
                for j, x in enumerate(self.optimizer.param_groups):
                    # bias lr falls from 0.1 to lr0, all other lrs rise from 0.0 to lr0
                    x['lr'] = np.interp(ni, xi, [self._vars.hyp['warmup_bias_lr'] if j == 2 else 0.0, x['initial_lr'] * self._vars.lf(self._vars.epoch)])
                    if 'momentum' in x:
                        x['momentum'] = np.interp(ni, xi, [self._vars.hyp['warmup_momentum'], self._vars.hyp['momentum']])

            # Multi-scale
            if self.args.multi_scale:
                sz = random.randrange(self._vars.imgsz * 0.5, self._vars.imgsz * 1.5 + self._vars.gs) // self._vars.gs * self._vars.gs  # size
                sf = sz / max(imgs.shape[2:])  # scale factor
                if sf != 1:
                    ns = [math.ceil(x * sf / self._vars.gs) * self._vars.gs for x in imgs.shape[2:]]  # new shape (stretched to gs-multiple)
                    imgs = nn.functional.interpolate(imgs, size=ns, mode='bilinear', align_corners=False)

            # Forward
            with amp.autocast(enabled=self._vars.cuda):
                pred = self.model(imgs)  # forward
                loss, loss_items = self.compute_loss(pred, targets.to(self.device))  # loss scaled by batch_size
                if self.args.quad:
                    loss *= 4.

            # Backward
            losses += loss
            self._vars.scaler.scale(loss).backward()

            # Optimize
            if ni - self._vars.last_opt_step >= self._vars.accumulate:
                self._vars.scaler.step(self.optimizer)  # self.optimizer.step
                self._vars.scaler.update()
                self.optimizer.zero_grad()
                if self._vars.ema:
                    self._vars.ema.update(self.model)
                self._vars.last_opt_step = ni

            # Log
            if RANK in [-1, 0]:
                self._vars.mloss = (self._vars.mloss * i + loss_items) / (i + 1)  # update mean losses
                mem = f'{torch.cuda.memory_reserved() / 1E9 if torch.cuda.is_available() else 0:.3g}G'  # (GB)
                self.pbar.set_description(('%10s' * 2 + '%10.4g' * 5) % (
                    f'{self._vars.epoch}/{self._vars.epochs - 1}', mem, *self._vars.mloss, targets.shape[0], imgs.shape[-1]))
                self.callbacks.run('on_train_batch_end', ni, self.model, imgs, targets, paths, self.plots, self.args.sync_bn)

        if isinstance(losses, int):
            return losses 
        else:
            return losses.item()


    def set_train_cfg(self):
        # Directories
        self._vars.w = self._vars.save_dir / 'weights'  # weights dir
        (self._vars.w).mkdir(parents=True, exist_ok=True)  # make dir
        self._vars.last, self._vars.best = self._vars.w / 'last.pt', self._vars.w / 'best.pt'

        # Hyperparameters
        self._vars.hyp = self.args.hyp
        if isinstance(self._vars.hyp, str):
            with open(self._vars.hyp, errors='ignore') as f:
                self._vars.hyp = yaml.safe_load(f)  # load hyps dict
        LOGGER.info(colorstr('hyperparameters: ') + ', '.join(f'{k}={v}' for k, v in self._vars.hyp.items()))

        # Save run settings
        with open(self._vars.save_dir / 'hyp.yaml', 'w') as f:
            yaml.safe_dump(self._vars.hyp, f, sort_keys=False)
        with open(self._vars.save_dir / 'opt.yaml', 'w') as f:
            yaml.safe_dump(vars(self.args), f, sort_keys=False)

        # Loggers
        self.data_dict = None
        if RANK in [-1, 0]:
            self.loggers = Loggers(self._vars.save_dir, self._vars.weights, self.args, self._vars.hyp, LOGGER)  # loggers instance

            # Register actions
            print("-----------------------------------------------------------")
            for k in methods(self.loggers):
                print(k)
                self.callbacks.register_action(k, callback=getattr(self.loggers, k))
            print("-----------------------------------------------------------")

        # Config
        self.plots = True  # create plots
        self._vars.cuda = self.device.type != 'cpu'
        init_seeds(1 + RANK)
        self.data_dict = self.data_dict or check_dataset(self._vars.data)  # check if None
        self._vars.train_path, self._vars.val_path = self.data_dict['train'], self.data_dict['val']
        self._vars.nc = 1 if self._vars.single_cls else int(self.data_dict['nc'])  # number of classes
        self._vars.names = ['item'] if self._vars.single_cls and len(self.data_dict['names']) != 1 else self.data_dict['names']  # class names
        assert len(self._vars.names) == self._vars.nc, f'{len(self._vars.names)} names found for nc={self._vars.nc} dataset in {self._vars.data}'  # check
        self._vars.is_coco = isinstance(self._vars.val_path, str) and self._vars.val_path.endswith('coco/val2017.txt')  # COCO dataset


    def set_train_vars(self):
        self._vars.t0 = time.time()
        self._vars.nw = max(round(self._vars.hyp['warmup_epochs'] * self._vars.nb), 1000)  # number of warmup iterations, max(3 epochs, 1k iterations)
        # nw = min(nw, (epochs - self._vars.start_epoch) / 2 * self._vars.nb)  # limit warmup to < 1/2 of training
        self._vars.last_opt_step = -1
        self._vars.maps = np.zeros(self._vars.nc)  # mAP per class
        self._vars.results = (0, 0, 0, 0, 0, 0, 0)  # P, R, mAP@.5, mAP@.5-.95, val_loss(box, obj, cls)
        self.scheduler.last_epoch = self._vars.start_epoch - 1  # do not move
        self._vars.scaler = amp.GradScaler(enabled=self._vars.cuda)
        self.stopper = EarlyStopping(patience=self.args.patience)
        self.compute_loss = ComputeLoss(self.model)  # init loss class
        LOGGER.info(f'Image sizes {self._vars.imgsz} train, {self._vars.imgsz} val\n'
                    f'Using {self.train_loader.num_workers * WORLD_SIZE} dataloader workers\n'
                    f"Logging results to {colorstr('bold', self._vars.save_dir)}\n"
                    f'Starting training for {self._vars.epochs} epochs...')
        
        self._vars.epoch = self._vars.start_epoch

    def after_one_epoch(self):
        self._vars.epoch += 1
        # Scheduler
        self._vars.lr = [x['lr'] for x in self.optimizer.param_groups]  # for loggers
        self.scheduler.step()

        if RANK in [-1, 0]:
            # mAP
            self.callbacks.run('on_train_epoch_end', epoch=self._vars.epoch)
            self._vars.ema.update_attr(self.model, include=['yaml', 'nc', 'hyp', 'names', 'stride', 'class_weights'])
            final_epoch = (self._vars.epoch + 1 == self._vars.epochs) or self.stopper.possible_stop
            if not self._vars.noval or final_epoch:  # Calculate mAP
                self._vars.results, self._vars.maps, _ = val.run(self.data_dict,
                                        batch_size=self._vars.batch_size // WORLD_SIZE * 2,
                                        imgsz=self._vars.imgsz,
                                        model=self._vars.ema.ema,
                                        single_cls=self._vars.single_cls,
                                        dataloader=self.val_loader,
                                        save_dir=self._vars.save_dir,
                                        plots=False,
                                        callbacks=self.callbacks,
                                        compute_loss=self.compute_loss)

            '''
                self._vars.restuls:
                Precision, Recall, mAP@0.5, mAP@0.5:0.95, ...
            '''

            # Update best mAP
            self._vars.fi = fitness(np.array(self._vars.results).reshape(1, -1))  # weighted combination of [P, R, mAP@.5, mAP@.5-.95]
            if self._vars.fi > self._vars.best_fitness:
                self._vars.best_fitness = self._vars.fi
            log_vals = list(self._vars.mloss) + list(self._vars.results) + self._vars.lr
            self.callbacks.run('on_fit_epoch_end', log_vals, self._vars.epoch, self._vars.best_fitness, self._vars.fi)

            # Save model
            if (not self._vars.nosave) or (final_epoch):  # if save
                self._vars.ckpt = {'epoch': self._vars.epoch,
                        'best_fitness': self._vars.best_fitness,
                        'model': deepcopy(de_parallel(self.model)).half(),
                        'ema': deepcopy(self._vars.ema.ema).half(),
                        'updates': self._vars.ema.updates,
                        'optimizer': self.optimizer.state_dict(),
                        'date': datetime.now().isoformat()}

                # Save last, best and delete
                torch.save(self._vars.ckpt, self._vars.last)
                if self._vars.best_fitness == self._vars.fi:
                    torch.save(self._vars.ckpt, self._vars.best)
                if (self._vars.epoch > 0) and (self.args.save_period > 0) and (self._vars.epoch % self.args.save_period == 0):
                    torch.save(self._vars.ckpt, self._vars.w / f'epoch{self._vars.epoch}.pt')
                del self._vars.ckpt
                self.callbacks.run('on_model_save', self._vars.last, self._vars.epoch, final_epoch, self._vars.best_fitness, self._vars.fi)

            # if RANK == -1 and self.stopper(epoch=self._vars.epoch, fitness=fi):
            #     break


    def end_of_train(self):
        # end training -----------------------------------------------------------------------------------------------------
        if RANK in [-1, 0]:
            LOGGER.info(f'\n{self._vars.epoch - self._vars.start_epoch + 1} epochs completed in {(time.time() - self._vars.t0) / 3600:.3f} hours.')
            for f in self._vars.last, self._vars.best:
                if f.exists():
                    strip_optimizer(f)  # strip optimizers
                    if f is self._vars.best:
                        LOGGER.info(f'\nValidating {f}...')
                        self._vars.results, _, _ = val.run(self.data_dict,
                                                batch_size=self._vars.batch_size // WORLD_SIZE * 2,
                                                imgsz=self._vars.imgsz,
                                                model=attempt_load(f, self.device).half(),
                                                iou_thres=0.65 if self._vars.is_coco else 0.60,  # best pycocotools results at 0.65
                                                single_cls=self._vars.single_cls,
                                                dataloader=self.val_loader,
                                                save_dir=self._vars.save_dir,
                                                save_json=self._vars.is_coco,
                                                verbose=True,
                                                plots=True,
                                                callbacks=self.callbacks,
                                                compute_loss=self.compute_loss)  # val best model with plots
                        if self._vars.is_coco:
                            self.callbacks.run('on_fit_epoch_end', list(self._vars.mloss) + list(self._vars.results) + self._vars.lr, self._vars.epoch, self._vars.best_fitness, self._vars.fi)

            self.callbacks.run('on_train_end', self._vars.last, self._vars.best, self.plots, self._vars.epoch, self._vars.results)
            LOGGER.info(f"Results saved to {colorstr('bold', self._vars.save_dir)}")

        torch.cuda.empty_cache()

    def train(self):#, callbacks=Callbacks()):

        self.set_train_cfg()
        self.set_model()
        self.set_train_vars()
        
        while self._vars.epoch <= self._vars.epochs:  # epoch ------------------------------------------------------------------
            self.train_one_epoch()

            if self.e_stop.is_set():
                break
                            
            self.after_one_epoch()

        self.end_of_train()

        return self._vars.results


if __name__ == "__main__":
    engine = Yolov5() 
    engine.get_args()
    # engine.train()
    engine.set_train_cfg()
    engine.set_model()
    engine.set_train_vars()
    
    for engine._vars.epoch in range(engine._vars.start_epoch, engine._vars.epochs):  # epoch ------------------------------------------------------------------
        engine.train_one_epoch()

        if engine.e_stop.is_set():
            break
                        
        engine.after_one_epoch()

    engine.end_of_train()

    print(engine._vars.results)
