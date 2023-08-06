# -*- coding: utf-8 -*-
import pytorch_lightning as pl


class TorchLightningModelV2Mixin(pl.LightningModule):
    """
    default pytorch-lightning model wrapper
    """
    @property
    def logits(self):
        return self._logits

    def __init__(self):
        self._logits = None
        super().__init__()

    def forward(self, *input):
        self._logits = super().forward(input)
        return self._logits
