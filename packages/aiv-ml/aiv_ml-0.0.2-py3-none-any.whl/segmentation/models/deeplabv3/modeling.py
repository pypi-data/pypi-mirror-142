from .utils import IntermediateLayerGetter
from ._deeplab import DeepLabHead, DeepLabHeadV3Plus, DeepLabV3
from .backbone import resnet
from .backbone import mobilenetv2
from .backbone import hrnetv2
import torch 
import os.path as osp

def _segm_hrnet(name, backbone_name, num_classes, num_classes_, pretrained_backbone, pretrained):

    backbone = hrnetv2.__dict__[backbone_name](pretrained_backbone)
    # HRNetV2 config:
    # the final output channels is dependent on highest resolution channel config (c).
    # output of backbone will be the inplanes to assp:
    hrnet_channels = int(backbone_name.split('_')[-1])
    inplanes = sum([hrnet_channels * 2 ** i for i in range(4)])
    low_level_planes = 256 # all hrnet version channel output from bottleneck is the same
    aspp_dilate = [12, 24, 36] # If follow paper trend, can put [24, 48, 72].

    if num_classes == num_classes_:
        if name=='deeplabv3plus':
            return_layers = {'stage4': 'out', 'layer1': 'low_level'}
            classifier = DeepLabHeadV3Plus(inplanes, low_level_planes, num_classes, aspp_dilate)
        elif name=='deeplabv3':
            return_layers = {'stage4': 'out'}
            classifier = DeepLabHead(inplanes, num_classes, aspp_dilate)

        backbone = IntermediateLayerGetter(backbone, return_layers=return_layers, hrnet_flag=True)
        model = DeepLabV3(backbone, classifier)
    else:
        if pretrained != 'True' and pretrained != 'False':
            if name=='deeplabv3plus':
                return_layers = {'stage4': 'out', 'layer1': 'low_level'}
                classifier = DeepLabHeadV3Plus(inplanes, low_level_planes, num_classes, aspp_dilate)
            elif name=='deeplabv3':
                return_layers = {'stage4': 'out'}
                classifier = DeepLabHead(inplanes, num_classes, aspp_dilate)

            backbone = IntermediateLayerGetter(backbone, return_layers=return_layers, hrnet_flag=True)
            model = DeepLabV3(backbone, classifier)

            checkpoint = torch.load(pretrained, map_location=torch.device('cpu'))
            model.load_state_dict(checkpoint["state_dict"])
                
            if name=='deeplabv3plus':
                return_layers = {'stage4': 'out', 'layer1': 'low_level'}
                classifier = DeepLabHeadV3Plus(inplanes, low_level_planes, num_classes_, aspp_dilate)
            elif name=='deeplabv3':
                return_layers = {'stage4': 'out'}
                classifier = DeepLabHead(inplanes , num_classes_, aspp_dilate)
            backbone = IntermediateLayerGetter(backbone, return_layers=return_layers)
            model = DeepLabV3(backbone, classifier)

            print(" * Loaded the pretrained weights for {} + {} with {}".format(backbone_name, name, pretrained))
        else:
            if name=='deeplabv3plus':
                return_layers = {'stage4': 'out', 'layer1': 'low_level'}
                classifier = DeepLabHeadV3Plus(inplanes, low_level_planes, num_classes_, aspp_dilate)
            elif name=='deeplabv3':
                return_layers = {'stage4': 'out'}
                classifier = DeepLabHead(inplanes, num_classes_, aspp_dilate)

            backbone = IntermediateLayerGetter(backbone, return_layers=return_layers, hrnet_flag=True)
            model = DeepLabV3(backbone, classifier)

    return model

def _segm_resnet(name, backbone_name, num_classes, num_classes_, output_stride, pretrained_backbone, pretrained):

    if output_stride==8:
        replace_stride_with_dilation=[False, True, True]
        aspp_dilate = [12, 24, 36]
    else:
        replace_stride_with_dilation=[False, False, True]
        aspp_dilate = [6, 12, 18]

    backbone = resnet.__dict__[backbone_name](
        pretrained=pretrained_backbone,
        replace_stride_with_dilation=replace_stride_with_dilation)
    
    inplanes = 2048
    low_level_planes = 256
    if num_classes_ == num_classes:
        if name=='deeplabv3plus':
            return_layers = {'layer4': 'out', 'layer1': 'low_level'}
            classifier = DeepLabHeadV3Plus(inplanes, low_level_planes, num_classes, aspp_dilate)
        elif name=='deeplabv3':
            return_layers = {'layer4': 'out'}
            classifier = DeepLabHead(inplanes , num_classes, aspp_dilate)

        backbone = IntermediateLayerGetter(backbone, return_layers=return_layers)
        model = DeepLabV3(backbone, classifier)
    else:
        if pretrained != 'True' and pretrained != 'False':
            if name=='deeplabv3plus':
                return_layers = {'layer4': 'out', 'layer1': 'low_level'}
                classifier = DeepLabHeadV3Plus(inplanes, low_level_planes, num_classes, aspp_dilate)
            elif name=='deeplabv3':
                return_layers = {'layer4': 'out'}
                classifier = DeepLabHead(inplanes , num_classes, aspp_dilate)

            backbone = IntermediateLayerGetter(backbone, return_layers=return_layers)
            model = DeepLabV3(backbone, classifier)

            checkpoint = torch.load(pretrained, map_location=torch.device('cpu'))
            model.load_state_dict(checkpoint["model_state"])
                
            if name=='deeplabv3plus':
                return_layers = {'layer4': 'out', 'layer1': 'low_level'}
                classifier = DeepLabHeadV3Plus(inplanes, low_level_planes, num_classes_, aspp_dilate)
            elif name=='deeplabv3':
                return_layers = {'layer4': 'out'}
                classifier = DeepLabHead(inplanes , num_classes_, aspp_dilate)
            backbone = IntermediateLayerGetter(backbone, return_layers=return_layers)
            model = DeepLabV3(backbone, classifier)

            print(" * Loaded the pretrained weights for {} + {} with {}".format(backbone_name, name, pretrained))
        else:
            if name=='deeplabv3plus':
                return_layers = {'layer4': 'out', 'layer1': 'low_level'}
                classifier = DeepLabHeadV3Plus(inplanes, low_level_planes, num_classes_, aspp_dilate)
            elif name=='deeplabv3':
                return_layers = {'layer4': 'out'}
                classifier = DeepLabHead(inplanes , num_classes_, aspp_dilate)

            backbone = IntermediateLayerGetter(backbone, return_layers=return_layers)
            model = DeepLabV3(backbone, classifier)

    return model

def _segm_mobilenet(name, backbone_name, num_classes, num_classes_, output_stride, pretrained_backbone, pretrained):
    if output_stride==8:
        aspp_dilate = [12, 24, 36]
    else:
        aspp_dilate = [6, 12, 18]

    backbone = mobilenetv2.mobilenet_v2(pretrained=pretrained_backbone, output_stride=output_stride)
    
    # rename layers
    backbone.low_level_features = backbone.features[0:4]
    backbone.high_level_features = backbone.features[4:-1]
    backbone.features = None
    backbone.classifier = None

    inplanes = 320
    low_level_planes = 24
    
    if num_classes_ == num_classes:
        if name=='deeplabv3plus':
            return_layers = {'high_level_features': 'out', 'low_level_features': 'low_level'}
            classifier = DeepLabHeadV3Plus(inplanes, low_level_planes, num_classes, aspp_dilate)
        elif name=='deeplabv3':
            return_layers = {'high_level_features': 'out'}
            classifier = DeepLabHead(inplanes , num_classes, aspp_dilate)

        backbone = IntermediateLayerGetter(backbone, return_layers=return_layers)
        model = DeepLabV3(backbone, classifier)
    else:
        if pretrained != 'True' and pretrained != 'False':
            if name=='deeplabv3plus':
                return_layers = {'high_level_features': 'out', 'low_level_features': 'low_level'}
                classifier = DeepLabHeadV3Plus(inplanes, low_level_planes, num_classes, aspp_dilate)
            elif name=='deeplabv3':
                return_layers = {'high_level_features': 'out'}
                classifier = DeepLabHead(inplanes , num_classes, aspp_dilate)

            backbone = IntermediateLayerGetter(backbone, return_layers=return_layers)
            model = DeepLabV3(backbone, classifier)

            checkpoint = torch.load(pretrained, map_location=torch.device('cpu'))
            model.load_state_dict(checkpoint["model_state"])
                
            if name=='deeplabv3plus':
                return_layers = {'high_level_features': 'out', 'low_level_features': 'low_level'}
                classifier = DeepLabHeadV3Plus(inplanes, low_level_planes, num_classes_, aspp_dilate)
            elif name=='deeplabv3':
                return_layers = {'high_level_features': 'out'}
                classifier = DeepLabHead(inplanes , num_classes_, aspp_dilate)
            backbone = IntermediateLayerGetter(backbone, return_layers=return_layers)
            model = DeepLabV3(backbone, classifier)

            print(" * Loaded the pretrained weights for {} + {} with {}".format(backbone_name, name, pretrained))
        else:
            if name=='deeplabv3plus':
                return_layers = {'high_level_features': 'out', 'low_level_features': 'low_level'}
                classifier = DeepLabHeadV3Plus(inplanes, low_level_planes, num_classes_, aspp_dilate)
            elif name=='deeplabv3':
                return_layers = {'high_level_features': 'out'}
                classifier = DeepLabHead(inplanes , num_classes_, aspp_dilate)

            backbone = IntermediateLayerGetter(backbone, return_layers=return_layers)
            model = DeepLabV3(backbone, classifier)

    return model

def _load_model(arch_type, backbone, num_classes, num_classes_, output_stride, pretrained_backbone, pretrained):

    if backbone=='mobilenetv2':
        model = _segm_mobilenet(arch_type, backbone, num_classes, num_classes_, output_stride=output_stride, pretrained_backbone=pretrained_backbone, pretrained=pretrained)
    elif backbone.startswith('resnet'):
        model = _segm_resnet(arch_type, backbone, num_classes, num_classes_, output_stride=output_stride, pretrained_backbone=pretrained_backbone, pretrained=pretrained)
    elif backbone.startswith('hrnetv2'):
        model = _segm_hrnet(arch_type, backbone, num_classes, num_classes_, pretrained_backbone=pretrained_backbone, pretrained=pretrained)
    else:
        raise NotImplementedError
    return model


# Deeplab v3
def deeplabv3_hrnetv2_48(pretrained=None, num_classes=21, num_classes_=0, output_stride=4, pretrained_backbone=False): # no pretrained backbone yet
    return _load_model('deeplabv3', 'hrnetv2_48', output_stride, num_classes, num_classes_, pretrained_backbone=pretrained_backbone, pretrained=pretrained)

def deeplabv3_hrnetv2_32(pretrained=None, num_classes=21, num_classes_=0, output_stride=4, pretrained_backbone=True):
    return _load_model('deeplabv3', 'hrnetv2_32', output_stride, num_classes, num_classes_, pretrained_backbone=pretrained_backbone, pretrained=pretrained)

def deeplabv3_resnet50(pretrained=None, num_classes=21, num_classes_=0, output_stride=8, pretrained_backbone=True):
    """Constructs a DeepLabV3 model with a ResNet-50 backbone.

    Args:
        num_classes (int): number of classes.
        output_stride (int): output stride for deeplab.
        pretrained_backbone (bool): If True, use the pretrained backbone.
    """
    return _load_model('deeplabv3', 'resnet50', num_classes, num_classes_, output_stride=output_stride, pretrained_backbone=pretrained_backbone, pretrained=pretrained)

def deeplabv3_resnet101(pretrained=None, num_classes=21, num_classes_=0, output_stride=8, pretrained_backbone=True):
    """Constructs a DeepLabV3 model with a ResNet-101 backbone.

    Args:
        num_classes (int): number of classes.
        output_stride (int): output stride for deeplab.
        pretrained_backbone (bool): If True, use the pretrained backbone.
    """
    return _load_model('deeplabv3', 'resnet101', num_classes, num_classes_, output_stride=output_stride, pretrained_backbone=pretrained_backbone, pretrained=pretrained)

def deeplabv3_mobilenet(pretrained=None, num_classes=21, num_classes_=0, output_stride=8, pretrained_backbone=True, **kwargs):
    """Constructs a DeepLabV3 model with a MobileNetv2 backbone.

    Args:
        num_classes (int): number of classes.
        output_stride (int): output stride for deeplab.
        pretrained_backbone (bool): If True, use the pretrained backbone.
    """
    return _load_model('deeplabv3', 'mobilenetv2', num_classes, num_classes_, output_stride=output_stride, pretrained_backbone=pretrained_backbone, pretrained=pretrained)


# Deeplab v3+
def deeplabv3plus_hrnetv2_48(pretrained=None, num_classes=21, num_classes_=0, output_stride=4, pretrained_backbone=False): # no pretrained backbone yet
    return _load_model('deeplabv3plus', 'hrnetv2_48', num_classes, num_classes_, output_stride, pretrained_backbone=pretrained_backbone, pretrained=pretrained)

def deeplabv3plus_hrnetv2_32(pretrained=None, num_classes=21, num_classes_=0, output_stride=4, pretrained_backbone=True):
    return _load_model('deeplabv3plus', 'hrnetv2_32', num_classes, num_classes_, output_stride, pretrained_backbone=pretrained_backbone, pretrained=pretrained)

def deeplabv3plus_resnet50(pretrained=None, num_classes=21, num_classes_=0, output_stride=8, pretrained_backbone=True):
    """Constructs a DeepLabV3 model with a ResNet-50 backbone.

    Args:
        num_classes (int): number of classes.
        output_stride (int): output stride for deeplab.
        pretrained_backbone (bool): If True, use the pretrained backbone.
    """
    return _load_model('deeplabv3plus', 'resnet50', num_classes, num_classes_, output_stride=output_stride, pretrained_backbone=pretrained_backbone, pretrained=pretrained)


def deeplabv3plus_resnet101(pretrained=None, num_classes=21, num_classes_=0, output_stride=8, pretrained_backbone=True):
    """Constructs a DeepLabV3+ model with a ResNet-101 backbone.

    Args:
        num_classes (int): number of classes.
        output_stride (int): output stride for deeplab.
        pretrained_backbone (bool): If True, use the pretrained backbone.
    """
    return _load_model('deeplabv3plus', 'resnet101', num_classes, num_classes_, output_stride=output_stride, pretrained_backbone=pretrained_backbone, pretrained=pretrained)


def deeplabv3plus_mobilenet(pretrained=None, num_classes=21, num_classes_=0, output_stride=8, pretrained_backbone=True):
    """Constructs a DeepLabV3+ model with a MobileNetv2 backbone.

    Args:
        num_classes (int): number of classes.
        output_stride (int): output stride for deeplab.
        pretrained_backbone (bool): If True, use the pretrained backbone.
    """
    if pretrained.split('_')[-2] == 'cityscapes':
        num_classes = 19

    return _load_model('deeplabv3plus', 'mobilenetv2', num_classes, num_classes_, output_stride=output_stride, pretrained_backbone=pretrained_backbone, pretrained=pretrained)