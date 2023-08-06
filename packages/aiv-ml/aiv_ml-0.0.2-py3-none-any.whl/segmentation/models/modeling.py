from models.torchvision.torchvision_models import torchvision_models
import models.unetpp.unetpp as unetpp
import models.deeplabv3 as deeplabv3 
import src.utils as utils
from models.deeplabv3._deeplab import DeepLabHead, DeepLabHeadV3Plus, DeepLabV3

TORCHVISION_MODELS = [
    'torchv_fcn_resnet50', 'torchv_fcn_resnet101', 'torchv_deeplabv3_resnet50', 'torchv_deeplabv3_resnet101', 'torchv_deeplabv3_mobilenet_v3_large',
    'torchv_lraspp_mobilenet_v3_large'
]

UNETPP = ['UNet', 'NestedUNet']

DEEPLABV3 = [ "deeplabv3_resnet50", "deeplabv3_resnet101", "deeplabv3_mobilenet", "deeplabv3_hrnetv2_48", "deeplabv3_hrnetv2_32", \
              "deeplabv3plus_resnet50", "deeplabv3plus_resnet101", "deeplabv3plus_mobilenet", "deeplabv3plus_hrnetv2_48", \
              "deeplabv3plus_hrnetv2_32"]

def Create_Model(args, train=True):
    if args.model in TORCHVISION_MODELS:
        if args.model.split('_')[0] == 'torchv':
            args.model = args.model.split('_')[1] + '_' + args.model.split('_')[2]
        if isinstance(args.pretrained, str):
            if args.pretrained == 'True':
                args.pretrained = True
            else:
                args.pretrained = False

        model = torchvision_models(args)

        if train:
            params_to_optimize = [
                {"params": [p for p in model.backbone.parameters() if p.requires_grad]},
                {"params": [p for p in model.classifier.parameters() if p.requires_grad]},
            ]
            if args.aux_loss:
                params = [p for p in model.aux_classifier.parameters() if p.requires_grad]
                params_to_optimize.append({"params": params, "lr": args.lr * 10})

            return model, params_to_optimize
        else:
            return model

    elif args.model in UNETPP:
        if isinstance(args.pretrained, str):
            if args.pretrained == 'True':
                args.pretrained = True
            else:
                args.pretrained = False
        model = unetpp.__dict__[args.model](args.num_classes, args.input_channels, args.deep_supervision)
        if train:
            return model, model.parameters()
        else:
            return model

    elif args.model in DEEPLABV3:
        model = deeplabv3.modeling.__dict__[args.model](pretrained=args.pretrained, num_classes_=args.num_classes, output_stride=args.output_stride)
        if args.separable_conv and 'plus' in args.model:
            deeplabv3.convert_to_separable_conv(model.classifier)
        utils.set_bn_momentum(model.backbone, momentum=0.01)

        params_to_optimize = [
                {'params': model.backbone.parameters(), 'lr': 0.1 * args.lr},
                {'params': model.classifier.parameters(), 'lr': args.lr}]

        if train:
            return model, params_to_optimize
        else:
            return model 
    elif args.model.split("_")[0] == 'segformer':
        from transformers import SegformerForSemanticSegmentation
        label2id = {val: idx for idx, val in enumerate(['_background_'] + args.classes)}
        id2label = {idx: val for idx, val in enumerate(['_background_'] + args.classes)}

        model = SegformerForSemanticSegmentation.from_pretrained("nvidia/mit-{}".format(args.model.split("_")[1]), ignore_mismatched_sizes=True,
                                                         num_labels=len(id2label), id2label=id2label, label2id=label2id,
                                                         reshape_last_stage=True)
        if train:
            return model, model.parameters()
        else:
            return model 
    else:
        raise RuntimeError(f"Invalid model: '{args.model}'. '{TORCHVISION_MODELS}', '{UNETPP}', and '{DEEPLABV3}' are available.") 

