import datetime
import os
import os.path as osp
from pathlib import Path
import sys
from tabnanny import check 

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

import time
import json
import torch
import torch.utils.data
from torch import nn
import torchvision

from src.coco_utils import get_coco
import src.presets as presets
import src.utils as utils
from tqdm import tqdm
from torchvision import transforms
import seaborn as sns 
import matplotlib.pyplot as plt 
import matplotlib 
from src.losses import CELoss, DiceLoss

### models 
from models.modeling import Create_Model

import numpy as np
from PIL import Image
import math
import cv2
import warnings
import glob
import copy
from src.transforms import Compose
import src.transforms_ as T
import collections 
from threading import Event

warnings.filterwarnings("ignore")

from configs.parse_cfgs import parse_test_cfgs

### logging
from utils.logger import get_root_logger

class segTest():
    def __init__(self, verbose_args=False):
        self.e_stop = Event()
        self.verbose_args = verbose_args
        self.reset()

    def get_args(self, cfgs_project_fp, exp=None, verbose=False):
        self.args = parse_test_cfgs(cfgs_project_fp=cfgs_project_fp, exp=exp, verbose=verbose)

        VALUES = list(range(0, self.args.num_classes)) 
        IDS = list(map(int, np.linspace(0, 255, self.args.num_classes)))
        self.t2l = { val : id_ for val, id_ in zip(VALUES, IDS) }

        mean=(0.485, 0.456, 0.406)
        std=(0.229, 0.224, 0.225)
        self.transform = T.Compose_([
            T.RandomResize_(self.args.base_imgsz, self.args.base_imgsz),
            T.ToTensor_(),
            T.Normalize_(mean=mean, std=std),
        ])

    def stop(self):
        self.e_stop.set()

    def reset(self):
        print(">> Reset all .......!!!!!!!")
        self.start_time = time.time()
        self.e_stop.clear()
        self.idx = 0
        self.fname = None 
        self.img_files = []
        self.num_img_files = 0

 

    def set(self):
        ### SET LOSS FUNCTION -----------------------------------------------------------------------------------------------
        if self.args.loss == 'CE':
            self.criterion = CELoss(self.args.aux_loss)
        elif self.args.loss == 'DiceLoss':
            self.criterion = DiceLoss(self.args.num_classes, False)
        elif self.args.loss == 'BceDiceLoss':
            self.criterion = DiceLoss(self.args.num_classes, True)

        self.model = Create_Model(self.args, train=False)

        checkpoint = torch.load(self.args.weights_fp, map_location="cpu")
        self.model.load_state_dict(checkpoint["model"], strict=True)

        print(">>> Loaded the model: ", self.args.weights_fp)
        self.model.to(self.args.device)
        self.model.eval()

        self.output_dir=osp.join(self.args.output_dir, 'imgs')
        if not osp.exists(self.output_dir):
            os.mkdir(self.output_dir)

        self.img_files = glob.glob(osp.join(self.args.data_path, '*.jpg'))
        self.num_img_files = len(self.img_files)


    def save_as_images(self, img, tensor_pred, filename, save_tensor):
        fig = plt.figure(figsize=(30, 20), dpi=200)
        plt.subplot(121)
        plt.imshow(img)
        plt.xlabel("original")
        plt.subplot(122)
        plt.imshow(img)
        plt.imshow(tensor_pred, alpha=0.8)
        plt.xlabel("pred")
        plt.savefig(filename)
        plt.close()

        if save_tensor:
            if not os.path.exists(os.path.join(self.output_dir, '../tensors')):
                os.makedirs(os.path.join(self.output_dir, '../tensors'))
            Image.fromarray(tensor_pred).save(os.path.join(self.output_dir, '../tensors', filename))

            
    @torch.inference_mode()
    def run_one_batch(self, save_img=True, save_tensor=False, ext='.jpg'):
        fname = osp.split(osp.splitext(self.img_files[self.idx])[0])[-1]
        img = Image.open(self.img_files[self.idx]).convert("RGB")
        _img = copy.deepcopy(img)
        _img = _img.resize((self.args.base_imgsz, self.args.base_imgsz))
        img = self.transform(img)
        img = torch.unsqueeze(img, 0)
        img = img.to(self.args.device)

        output = self.model(img)

        if isinstance(output, collections.OrderedDict) and 'out' in output.keys():
            output = output['out']

        preds = torch.nn.functional.softmax(output, dim=1)
        preds_labels = torch.argmax(preds, dim=1)
        preds_labels = preds_labels.float().to('cpu')
        _, x, y = preds_labels.size()
        preds_labels.apply_(lambda x: self.t2l[x])
        # preds_labels = transforms.Resize((1100, 1200), interpolation=Image.NEAREST)(preds_labels)
        # print(preds_labels.size(), np.unique(preds_labels.cpu()))
        
        preds_labels = np.array(transforms.ToPILImage()(preds_labels[0].byte()))

        filename = os.path.join(self.output_dir, fname + ext)

        if save_img:
            self.save_as_images(_img, preds_labels, filename, save_tensor)   

        self.idx += 1
        
        return filename

    @torch.inference_mode()
    def evaluate(self):
        for self.idx in range(self.num_img_files):
            self.run_one_batch()
        

  


    # def evaluate(self):

    #     self.output_dir=osp.join(self.args.output_dir, 'imgs')
    #     if not osp.exists(self.output_dir):
    #         os.mkdir(self.output_dir)

    #     self.model.eval()

    #     with torch.inference_mode():
    #         cnt = 1
    #         img_files = glob.glob(osp.join(self.args.data_path, '*.jpg'))
    #         for img_file in tqdm(img_files):
    #             if self.e_stop.isSet():
    #                 break
    #             fname = osp.split(osp.splitext(img_file)[0])[-1]
                
    #             img = Image.open(img_file).convert("RGB")
    #             _img = copy.deepcopy(img)
    #             _img = _img.resize((1280, 1280))
    #             # img = cv2.resize(img, (1280, 1280))
    #             # _img = copy.deepcopy(img)
    #             # img = transforms.ToTensor()(img)
    #             img = self.transform(img)
    #             img = torch.unsqueeze(img, 0)
    #             img = img.to(self.device)

    #             output = self.model(img)

    #             if isinstance(output, collections.OrderedDict) and 'out' in output.keys():
    #                 output = output['out']

    #             preds = torch.nn.functional.softmax(output, dim=1)
    #             preds_labels = torch.argmax(preds, dim=1)
    #             preds_labels = preds_labels.float()
    #             # print("* pred size: ", preds_labels.size())
                
    #             # for x in range(preds_labels.size(1)):
    #             #     for y in range(preds_labels.size(2)):
    #             #         print("\r {}, {}".format(x, y), end='')
    #             #         if preds_labels[0][x][y].cpu().detach().item() != 0.0:
    #             #             print('---', preds_labels[0][x][y].cpu().detach().item())

    #             preds_labels = preds_labels.to('cpu')
    #             _, x, y = preds_labels.size()
    #             preds_labels.apply_(lambda x: self.t2l[x])
    #             # preds_labels = transforms.Resize((1100, 1200), interpolation=Image.NEAREST)(preds_labels)
    #             # print(preds_labels.size(), np.unique(preds_labels.cpu()))
                
    #             cnt += 1
    #             preds_labels = np.array(transforms.ToPILImage()(preds_labels[0].byte()))

    #             # image, cx, cy, r = get_circle(im0, fname)
    #             # preds_labels = exceptions(preds_labels, cx, cy, r, offset1, offset2)
    #             self.save_as_images(_img, preds_labels, output_dir, fname)     

    #             if cnt > 2:
    #                 break    

if __name__ == "__main__":
    agent = segTest(True)
    agent.get_args(cfgs_project_fp='./configs/projects/interojo_s_factory.yaml', verbose=True)
    agent.set()       
    agent.evaluate()