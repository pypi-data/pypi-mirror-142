# -*- coding: utf-8 -*-
from pyskydl.core.netv2 import NetV2
from pyskydl.core.torch_lightning_modelv2_mixin import TorchLightningModelV2Mixin


class TorchLightningNetV2(NetV2, TorchLightningModelV2Mixin):
    """pytorch lightning net"""
    def __init__(self, name: str = None, parser_args=None):
        super().__init__(name=name, parser_args=parser_args)
        # 再显式调用其它的__init__(self)
        TorchLightningModelV2Mixin.__init__(self)

    def forward(self, *input, **kwargs):
        """forward e.g. return self.layer(*input)"""
        return super().forward(*input, **kwargs)

    def call_hidden_layers(self, _x, name="predict"):
        name = 'predict' if name is None else name
        predict = None
        return predict

    def compile_loss_metrics_optimizer_predict(self, _x, _y, _learning_rate=0.001, devices=[]):
        pass
