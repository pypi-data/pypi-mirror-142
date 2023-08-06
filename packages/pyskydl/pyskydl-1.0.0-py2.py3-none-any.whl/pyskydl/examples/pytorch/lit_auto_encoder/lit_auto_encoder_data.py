# -*- coding: utf-8 -*-
import pytorch_lightning as pl
from torchvision import transforms
from torchvision.datasets import MNIST
from torch.utils.data import random_split, DataLoader


class LitAutoEncoderDataModule(pl.LightningDataModule):
    """pytorch data module"""
    def __init__(self, data_path: str = "", batch_size: int = 128):
        super().__init__()
        dataset = MNIST(data_path, train=True, download=True, transform=transforms.ToTensor())
        self.test_data = MNIST(data_path, train=False, download=True, transform=transforms.ToTensor())
        self.train_data, self.val_data = random_split(dataset, [55000, 5000])
        self.batch_size = batch_size

    def train_dataloader(self):
        return DataLoader(self.train_data, batch_size=self.batch_size)

    def val_dataloader(self):
        return DataLoader(self.val_data, batch_size=self.batch_size)

    def test_dataloader(self):
        return DataLoader(self.test_data, batch_size=self.batch_size)

    def predict_dataloader(self):
        return DataLoader(self.test_data, batch_size=self.batch_size)



