# -*- coding: utf-8 -*-
import pytorch_lightning as pl
from typing import Optional, Any
from pytorch_lightning.callbacks import ModelCheckpoint
from pyskydl.core.torch_lightning_netv2 import TorchLightningNetV2


class CheckpointEveryEpoch(pl.Callback):
    def __init__(self, start_epoch, save_path, ):
        self.start_epoch = start_epoch
        self.save_path = save_path

    def on_epoch_end(self, trainer: pl.Trainer, _):
        """ Check if we should save a checkpoint after every train epoch """
        current_epoch = trainer.current_epoch
        if current_epoch >= self.start_epoch:
            trainer.save_checkpoint(self.save_path)


class DefaultTorchLightningNet(TorchLightningNetV2):
    """default pytorch-lightning net"""
    def __init__(self, name: str = None, parser_args=None):
        super().__init__(name=name, parser_args=parser_args)

    def forward(self, *input, **kwargs):
        """forward e.g. return self.layer(*input)"""
        return None

    def configure_callbacks(self):
        checkpoint_callback = ModelCheckpoint(
            monitor="val_loss",
            verbose=True,
            dirpath=self.parser_args.checkpoint_path,
            filename=self.name() + "-{epoch:02d}-{val_loss:.2f}",
            save_last=True,
            mode="min",
        )
        return [checkpoint_callback]

    def configure_optimizers(self):
        return None

    def training_step(self, train_batch, batch_idx):
        pass

    def validation_step(self, val_batch, batch_idx):
        pass

    def test_step(self, batch, batch_idx):
        pass

    def predict_step(self, batch: Any, batch_idx: int, dataloader_idx: Optional[int] = None) -> Any:
        return super().predict_step(batch, batch_idx, dataloader_idx)

