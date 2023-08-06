# -*- coding: utf-8 -*-
import torch
import torch.nn as nn
from torchmetrics import Accuracy
from torch.nn import functional as F
from pyskydl.core.default_torch_lightning_net import DefaultTorchLightningNet


class LitAutoEncoderNet(DefaultTorchLightningNet):
    """lit auto encoder pytorch net"""
    def __init__(self, name: str = None, parser_args=None):
        super().__init__(name=name, parser_args=parser_args)
        self.encoder = nn.Sequential(
            nn.Linear(28 * 28, 64),
            nn.ReLU(),
            nn.Linear(64, 3))
        self.decoder = nn.Sequential(
            nn.Linear(3, 64),
            nn.ReLU(),
            nn.Linear(64, 28 * 28))
        self.train_acc = Accuracy()
        self.valid_acc = Accuracy()
        self.test_acc = Accuracy()

    def forward(self, *input, **kwargs):
        embedding = self.encoder(*input)
        return embedding

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=1e-3)
        return optimizer

    def training_step(self, train_batch, batch_idx):
        x, y = train_batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        logits = self.decoder(z)
        loss = F.mse_loss(logits, x)
        self.log("train_loss", loss, prog_bar=True)
        # self.log("train_acc", self.train_acc(logits, y), prog_bar=True)
        return loss

    def validation_step(self, val_batch, batch_idx):
        x, y = val_batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = F.mse_loss(x_hat, x)
        self.log('val_loss', loss)

    def test_step(self, batch, batch_idx):
        x, y = batch
        x = x.view(x.size(0), -1)
        z = self.encoder(x)
        x_hat = self.decoder(z)
        loss = F.mse_loss(x_hat, x)
        self.log("test_loss", loss, on_step=True)

