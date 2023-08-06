# -*- coding: utf-8 -*-
import torch
import torch.nn as nn
from typing import Any
import torch.nn.functional as F
from pyskydl.core.default_torch_lightning_net import DefaultTorchLightningNet


class HelloPyTorchNet(DefaultTorchLightningNet):
    """"hello pytorch net"""
    def __init__(self, name=None, parser_args=None):
        super().__init__(name=name, parser_args=parser_args)
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Linear(320, 50)
        self.fc2 = nn.Linear(50, 10)

    def forward(self, *input, **kwargs):
        x = F.relu(F.max_pool2d(self.conv1(input[0]), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = x.view(-1, 320)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)

    def configure_optimizers(self):
        optimizer = torch.optim.SGD(self.parameters(), lr=self.parser_args.learning_rate, momentum=self.parser_args.momentum)
        return optimizer

    def training_step(self, train_batch, batch_idx):
        x, y = train_batch
        x = x.view(-1, 1, 28, 28)
        y = y.view([-1])
        logits = self(x)
        loss = F.cross_entropy(logits, y)
        self.log("train_loss", loss, prog_bar=True)
        return loss

    def validation_step(self, val_batch, batch_idx):
        x, y = val_batch
        x = x.view(-1, 1, 28, 28)
        y = y.view([-1])
        logits = self(x)
        loss = F.cross_entropy(logits, y)
        self.log("val_loss", loss, prog_bar=True)

    def test_step(self, batch, batch_idx):
        x, y = batch
        x = x.view(-1, 1, 28, 28)
        y = y.view([-1])
        logits = self(x)
        loss = F.cross_entropy(logits, y)
        self.log("test_loss", loss, prog_bar=True)

    def predict_step(self, batch, batch_idx: int, dataloader_idx: int = None) -> Any:
        x, y = batch
        x = x.view(-1, 1, 28, 28)
        return self(x)


