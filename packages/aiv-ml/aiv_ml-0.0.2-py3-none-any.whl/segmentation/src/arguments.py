import os
import os.path as osp
import argparse
import datetime
# import src.utils as utils
import json
import torch.backends.cudnn as cudnn
import yaml


def get_args(add_help=True, verbose=False):
    parser = argparse.ArgumentParser(description="PyTorch based semantic segmentation", add_help=add_help)
    
    parser.add_argument('--project-name', default='INTEROJO_S_Factory')
    # parser.add_argument('--data-path', default='/home/wonchul/HDD/datasets/projects/interojo/S_factory_ver2/coco_datasets_good/DUST', help='dataset path')
    # parser.add_argument('--data-path', default='/home/wonchul/HDD/datasets/projects/interojo/S_factory/coco_datasets_good/DUST_BUBBLE_DAMAGE_EDGE_RING_LINE_OVERLAP', help='dataset path')
    parser.add_argument('--data-path', default='/home/nvadmin/wonchul/mnt/HDD/datasets/projects/interojo/S_factory/coco_datasets_good/DUST_BUBBLE_DAMAGE_EDGE_RING_LINE_OVERLAP', help='dataset path')
    parser.add_argument('--with-good', action='store_true')
    parser.add_argument('--wandb', action='store_true')
    parser.add_argument('--dataset-type', default='coco', help='dataset name')

    # Model setting
    parser.add_argument("--model", default="deeplabv3plus_hrnetv2_48", type=str, 
            help="For torchvision,  deeplabv3_resnet50 | deeplabv3_resnet101 | deeplabv3_mobilenet_v3_large | lraspp_mobilenet_v3_large" +
                 "For UNet**, NestedUNet | UNet" + 
                 "For deeplabv3, deeplabv3_resnet50 | deeplabv3_resnet101 | deeplabv3_mobilenet | deeplabv3_hrnetv2_48 |deeplabv3_hrnetv2_32" + 
                 "For deeplabv3plus, deeplabv3plus_resnet50 | deeplabv3plus_resnet101 | deeplabv3plus_mobilenet | " + 
                                   " deeplabv3plus_hrnetv2_48 | deeplabv3plus_hrnetv2_32")
    parser.add_argument("--pretrained", default='True')
    parser.add_argument("--weights", default=None, type=str, help="the weights to load")
    parser.add_argument("--input-channels", default=3)
    parser.add_argument('--base-imgsz', default=1440, type=int, help='base image size')
    parser.add_argument('--crop-imgsz', default=1440, type=int, help='base image size')

    # output stride for deeplabv3+
    parser.add_argument("--output-stride", type=int, default=16, choices=[8, 16])
    parser.add_argument("--separable-conv", action='store_true', default=False,
                        help="apply separable conv to decoder and aspp")
    # loss
    parser.add_argument("--loss", default='DiceLoss', help='CE | DiceLoss | BceDiceLoss')
    parser.add_argument("--aux-loss", action="store_true", help="auxiliar loss")
    
    # device
    parser.add_argument('--device', default='cuda', help='gpu device ids')
    parser.add_argument('--device-ids', default='0,1,2,3', help='gpu device ids')
    
    # training parameters
    parser.add_argument("--batch-size", default=8, type=int, help="images per gpu, the total batch size is $NGPU x batch_size")
    parser.add_argument("--start-epoch", default=0, type=int, metavar="N", help="start epoch")
    
    parser.add_argument("--epochs", default=800, type=int, metavar="N", help="number of total epochs to run")
    parser.add_argument('--dataparallel', action='store_true')
    parser.add_argument("--num-workers", default=32, type=int, metavar="N", help="number of data loading workers (default: 16)")

    # optimizer & lr 
    parser.add_argument("--lr", default=0.01, type=float, help="initial learning rate")
    parser.add_argument("--lr-warmup-epochs", default=30, type=int, help="the number of epochs to warmup (default: 0)")
    parser.add_argument("--lr-warmup-method", default="linear", type=str, help="the warmup method (default: linear)")
    parser.add_argument("--lr-warmup-decay", default=0.01, type=float, help="the decay for lr")
    parser.add_argument("--lr_scheduler", type=str, default='LambdaLR', choices=['PolyLR', 'LambdaLR'],
                        help="learning rate scheduler policy")

    parser.add_argument("--optimizer", default='SGD', help='SGD | Adam')
    parser.add_argument("--momentum", default=0.9, type=float, metavar="M", help="momentum")
    parser.add_argument("--weight-decay", default=1e-4, type=float, metavar="W", help="weight decay (default: 1e-4)", dest="weight_decay")
    parser.add_argument('--nesterov', default=False, help='nesterov')

    # if the model is unetpp
    parser.add_argument('--deep-supervision', action='store_true')

    # distributed training parameters
    parser.add_argument("--distributed", action='store_true')
    parser.add_argument("--local-rank", default=0, type=int)
    parser.add_argument("--world-size", default=1, type=int, help="number of distributed processes")
    parser.add_argument("--dist-url", default='tcp://127.0.0.1:5001', type=str, help="url used to set up distributed training")
    parser.add_argument('--dist-backend', default='nccl', type=str, help='')
    parser.add_argument('--rank', default=0, type=int, help='')

    # Prototype models only

    
    # etc.
    parser.add_argument("--print-freq", default=10, type=int, help="print frequency")
    parser.add_argument('--output-dir', default='./outputs/train', help='path where to save')

    args = parser.parse_args()

    if args.deep_supervision and (args.model != "NestedUNet" and args.model != "UNet"):
            raise RuntimeError("Deep supervision option can be applied with NestedUNet or UNet! Current model is {}".format(args.model))

    if args.model == "NestedUNet" or args.model == "UNet":
        if args.crop_imgsz%160 != 0.:
            raise RuntimeError("UNet and NestedUNet should have image size multiplied by 160! Current crop imgsz is {}".format(args.crop_imgsz))

    args.device_ids = list(map(int, args.device_ids.split(',')))

    args.world_size = len(args.device_ids)*args.world_size
    args.rank = args.rank*len(args.device_ids) + args.device_ids[0]

    args.classes = ['_background_'] + list(osp.split(osp.splitext(args.data_path)[0])[-1].split('_'))
    args.num_classes = len(list(osp.split(osp.splitext(args.data_path)[0])[-1].split('_'))) + 1
    if args.device == 'cuda':
        args.device = 'cuda:{}'.format(args.device_ids[0])
    
    now = datetime.datetime.now()
    if args.output_dir:
        if not os.path.exists(args.output_dir):
            args.output_dir = os.path.join(args.output_dir, 'seg1')
            os.makedirs(args.output_dir)
        else:
            folders = os.listdir(args.output_dir)
            args.output_dir = os.path.join(args.output_dir, 'seg' + str(len(folders) + 1))
            os.makedirs(args.output_dir)

        output_path = args.output_dir
        args.date = str(datetime.datetime.now())
        utils.mkdir(osp.join(output_path, 'cfg'))
        args.weights_path = osp.join(output_path, 'weights')
        utils.mkdir(args.weights_path)

    args.run_name = osp.split(osp.splitext(output_path)[0])[-1]
    # with open(osp.join(output_path, 'cfg/config.json'), 'w') as f:
    #     json.dump(args.__dict__, f, indent=2)
    
    with open(osp.join(output_path, 'cfg/args.yaml'), 'w') as f:
        yaml.dump(args.__dict__, f, indent=2)

    # utils.init_distributed_mode(args)

    if args.distributed and args.dataparallel:
        raise RuntimeError("Distributed mode cannot be executed with Dataparallel mode .......!")

    cudnn.benchmark = True ## ??????????????????????????????????????????????????????????

    if verbose:
        for arg in vars(args):
            print("{}: {}".format(arg, getattr(args, arg)))

    return args


if __name__ == '__main__':
    import utils as utils

    get_args(verbose=True)
    # with open("/home/wonchul/projects/mlops/MLDashboard/mlalgorithms/segmentation/outputs/train/seg4/cfg/args.yaml") as f:
    #     args = yaml.safe_load(f)

    # print(args)
