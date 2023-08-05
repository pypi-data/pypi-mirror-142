from typing import Any, Type, Union, List, Optional

import torch
import torch.nn as nn
from torch import Tensor
from torchvision.models.resnet import Bottleneck, BasicBlock, ResNet, model_urls

from ..._internally_replaced_utils import load_state_dict_from_url
from .utils import _fuse_modules, _replace_relu, quantize_model

__all__ = ["QuantizableResNet", "resnet18", "resnet50", "resnext101_32x8d"]


quant_model_urls = {
    "resnet18_fbgemm": "https://download.pytorch.org/models/quantized/resnet18_fbgemm_16fa66dd.pth",
    "resnet50_fbgemm": "https://download.pytorch.org/models/quantized/resnet50_fbgemm_bf931d71.pth",
    "resnext101_32x8d_fbgemm": "https://download.pytorch.org/models/quantized/resnext101_32x8_fbgemm_09835ccf.pth",
}


class QuantizableBasicBlock(BasicBlock):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.add_relu = torch.nn.quantized.FloatFunctional()

    def forward(self, x: Tensor) -> Tensor:
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.downsample is not None:
            identity = self.downsample(x)

        out = self.add_relu.add_relu(out, identity)

        return out

    def fuse_model(self, is_qat: Optional[bool] = None) -> None:
        _fuse_modules(self, [["conv1", "bn1", "relu"], ["conv2", "bn2"]], is_qat, inplace=True)
        if self.downsample:
            _fuse_modules(self.downsample, ["0", "1"], is_qat, inplace=True)


class QuantizableBottleneck(Bottleneck):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.skip_add_relu = nn.quantized.FloatFunctional()
        self.relu1 = nn.ReLU(inplace=False)
        self.relu2 = nn.ReLU(inplace=False)

    def forward(self, x: Tensor) -> Tensor:
        identity = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu1(out)
        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu2(out)

        out = self.conv3(out)
        out = self.bn3(out)

        if self.downsample is not None:
            identity = self.downsample(x)
        out = self.skip_add_relu.add_relu(out, identity)

        return out

    def fuse_model(self, is_qat: Optional[bool] = None) -> None:
        _fuse_modules(
            self, [["conv1", "bn1", "relu1"], ["conv2", "bn2", "relu2"], ["conv3", "bn3"]], is_qat, inplace=True
        )
        if self.downsample:
            _fuse_modules(self.downsample, ["0", "1"], is_qat, inplace=True)


class QuantizableResNet(ResNet):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.quant = torch.ao.quantization.QuantStub()
        self.dequant = torch.ao.quantization.DeQuantStub()

    def forward(self, x: Tensor) -> Tensor:
        x = self.quant(x)
        # Ensure scriptability
        # super(QuantizableResNet,self).forward(x)
        # is not scriptable
        x = self._forward_impl(x)
        x = self.dequant(x)
        return x

    def fuse_model(self, is_qat: Optional[bool] = None) -> None:
        r"""Fuse conv/bn/relu modules in resnet models

        Fuse conv+bn+relu/ Conv+relu/conv+Bn modules to prepare for quantization.
        Model is modified in place.  Note that this operation does not change numerics
        and the model after modification is in floating point
        """
        _fuse_modules(self, ["conv1", "bn1", "relu"], is_qat, inplace=True)
        for m in self.modules():
            if type(m) is QuantizableBottleneck or type(m) is QuantizableBasicBlock:
                m.fuse_model(is_qat)


def _resnet(
    arch: str,
    block: Type[Union[QuantizableBasicBlock, QuantizableBottleneck]],
    layers: List[int],
    pretrained: bool,
    progress: bool,
    quantize: bool,
    **kwargs: Any,
) -> QuantizableResNet:

    model = QuantizableResNet(block, layers, **kwargs)
    _replace_relu(model)
    if quantize:
        # TODO use pretrained as a string to specify the backend
        backend = "fbgemm"
        quantize_model(model, backend)
    else:
        assert pretrained in [True, False]

    if pretrained:
        if quantize:
            model_url = quant_model_urls[arch + "_" + backend]
        else:
            model_url = model_urls[arch]

        state_dict = load_state_dict_from_url(model_url, progress=progress)

        model.load_state_dict(state_dict)
    return model


def resnet18(
    pretrained: bool = False,
    progress: bool = True,
    quantize: bool = False,
    **kwargs: Any,
) -> QuantizableResNet:
    r"""ResNet-18 model from
    `"Deep Residual Learning for Image Recognition" <https://arxiv.org/pdf/1512.03385.pdf>`_

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
        progress (bool): If True, displays a progress bar of the download to stderr
        quantize (bool): If True, return a quantized version of the model
    """
    return _resnet("resnet18", QuantizableBasicBlock, [2, 2, 2, 2], pretrained, progress, quantize, **kwargs)


def resnet50(
    pretrained: bool = False,
    progress: bool = True,
    quantize: bool = False,
    **kwargs: Any,
) -> QuantizableResNet:

    r"""ResNet-50 model from
    `"Deep Residual Learning for Image Recognition" <https://arxiv.org/pdf/1512.03385.pdf>`_

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
        progress (bool): If True, displays a progress bar of the download to stderr
        quantize (bool): If True, return a quantized version of the model
    """
    return _resnet("resnet50", QuantizableBottleneck, [3, 4, 6, 3], pretrained, progress, quantize, **kwargs)


def resnext101_32x8d(
    pretrained: bool = False,
    progress: bool = True,
    quantize: bool = False,
    **kwargs: Any,
) -> QuantizableResNet:
    r"""ResNeXt-101 32x8d model from
    `"Aggregated Residual Transformation for Deep Neural Networks" <https://arxiv.org/pdf/1611.05431.pdf>`_

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
        progress (bool): If True, displays a progress bar of the download to stderr
        quantize (bool): If True, return a quantized version of the model
    """
    kwargs["groups"] = 32
    kwargs["width_per_group"] = 8
    return _resnet("resnext101_32x8d", QuantizableBottleneck, [3, 4, 23, 3], pretrained, progress, quantize, **kwargs)
