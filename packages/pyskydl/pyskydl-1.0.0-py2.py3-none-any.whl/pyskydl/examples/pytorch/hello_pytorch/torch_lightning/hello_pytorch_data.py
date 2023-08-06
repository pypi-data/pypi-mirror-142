# -*- coding: utf-8 -*-
import pytorch_lightning as pl
from torchvision import datasets
from torchvision import transforms
from torch.utils.data import random_split, DataLoader
from pyskydl.core.default_data_module import DefaultDataModule


class HelloPytorchDataModule(pl.LightningDataModule, DefaultDataModule):
    """pytorch data module"""
    def __init__(self, data_path: str = "", batch_size: int = 128):
        super().__init__()
        dataset = datasets.MNIST(data_path, train=True, download=True,
                                 transform=transforms.Compose([
                                     transforms.ToTensor(),
                                     transforms.Normalize((0.1307,), (0.3081,))
                                 ]))
        # self.dataset_sampler = RandomSampler(dataset)
        self.dataset_sampler = None
        # kwargs = {'num_workers': 1, 'pin_memory': True} if self.parser_args.use_cuda else {}
        self.kwargs = {}
        self.train_data, self.val_data = random_split(dataset, [55000, 5000])
        self.test_loader = DataLoader(
            datasets.MNIST(data_path, train=False, download=True, transform=transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize((0.1307,), (0.3081,))
            ])),
            batch_size=batch_size, shuffle=True, **self.kwargs)
        self.batch_size = batch_size

    def train_dataloader(self):
        return DataLoader(self.train_data, sampler=self.dataset_sampler, batch_size=self.batch_size, shuffle=False, **self.kwargs)

    def val_dataloader(self):
        return DataLoader(self.val_data, batch_size=self.batch_size)

    def test_dataloader(self):
        return self.test_loader

    def predict_dataloader(self):
        return DataLoader(self.val_data, batch_size=self.batch_size)



