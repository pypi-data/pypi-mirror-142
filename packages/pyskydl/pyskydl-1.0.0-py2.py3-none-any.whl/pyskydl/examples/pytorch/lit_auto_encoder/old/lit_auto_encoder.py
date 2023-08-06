import torch
from torch import nn
import pytorch_lightning as pl
from torch.nn import functional as F
from torch.utils.data import DataLoader
from torch.utils.data import random_split
from torchmetrics import Accuracy
from torchvision.datasets import MNIST
from torchvision import transforms
from skydl.common.common_utils import CommonUtils
from pytorch_lightning.callbacks import ModelCheckpoint, EarlyStopping
from pytorch_lightning.utilities.cloud_io import load as pl_load
"""
参考：https://github.com/PyTorchLightning/pytorch-lightning/blob/master/pl_examples/basic_examples/autoencoder.py
参考：https://github.com/PyTorchLightning/pytorch-lightning/blob/0c0b24c0319a4bb788836b1a4652a686fa919780/tests/helpers/simple_models.py
"""


class CheckpointEveryEpoch(pl.Callback):
    def __init__(self, start_epoch, save_path, ):
        self.start_epoch = start_epoch
        self.save_path = save_path

    def on_epoch_end(self, trainer: pl.Trainer, _):
        """ Check if we should save a checkpoint after every train epoch """
        current_epoch = trainer.current_epoch
        if current_epoch >= self.start_epoch:
            trainer.save_checkpoint(self.save_path)


class LitAutoEncoder(pl.LightningModule):
    def __init__(self):
        super().__init__()
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

    def forward(self, x):
        embedding = self.encoder(x)
        return embedding

    def configure_callbacks(self):
        # early_stop_callback = EarlyStopping(monitor="train_loss", mode="min")
        # saves a file like: my/path/sample-mnist-epoch=02-val_loss=0.32.ckpt
        checkpoint_callback = ModelCheckpoint(
            monitor="val_loss",
            verbose=True,
            dirpath="/Users/tony/deep_learning_can_not_delete/saved_model/pytorch_lightning_hello",
            filename="sample-mnist-{epoch:02d}-{val_loss:.2f}",
            save_last=True,
            # save_top_k=3,
            mode="min",
            # every_n_epochs=1,
            # save_on_train_epoch_end=True
        )
        return [checkpoint_callback,
                CheckpointEveryEpoch(1, "/Users/tony/deep_learning_can_not_delete/saved_model/pytorch_lightning_hello/example.ckpt")]

    # def loss(self, batch, prediction):
    #     # An arbitrary loss to have a loss that updates the model weights during `Trainer.fit` calls
    #     return torch.nn.functional.mse_loss(prediction, torch.ones_like(prediction))

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
        # self.log("test_acc", self.test_acc(x_hat, y), prog_bar=True)


class MyDataModule(pl.LightningDataModule):
    def __init__(self, batch_size: int = 32):
        super().__init__()
        dataset = MNIST('', train=True, download=True, transform=transforms.ToTensor())
        self.test_data = MNIST("", train=False, download=True, transform=transforms.ToTensor())
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


if __name__ == '__main__':
    # build hparams
    MAX_EPOCH = 5
    CKPT_ENABLED = False
    LAST_CKPT_FILE = "/Users/tony/deep_learning_can_not_delete/saved_model/pytorch_lightning_hello/last.ckpt"

    # build dataset
    mnist_dataset = MyDataModule(32)

    # build model
    model = LitAutoEncoder()

    # training
    trainer = pl.Trainer(
        max_epochs=MAX_EPOCH,  # 最大训练周期数
        accelerator="dp",  # 加速模式选择"ddp"，而不是None或其它，在多gpu模式下resume_from_checkpoint才生效
        gpus=2,  # 每个训练节点上的gpu个数
        num_nodes=1,  # 训练节点个数
        precision=32,  # 训练精度，在GPU上可以选16
        limit_train_batches=0.25,  # 用于小数据调试
        resume_from_checkpoint=LAST_CKPT_FILE if CommonUtils.path_exists(LAST_CKPT_FILE) and CKPT_ENABLED else None
    )

    # fit model from checkpoint
    ckpt = pl_load(LAST_CKPT_FILE) if CommonUtils.path_exists(LAST_CKPT_FILE) and CKPT_ENABLED else None
    ckpt_current_epoch = ckpt["epoch"] if ckpt is not None else 0
    if ckpt_current_epoch < MAX_EPOCH:
        trainer.fit(model, mnist_dataset.train_dataloader(), mnist_dataset.val_dataloader())

    # test or predict
    print(f"trainer.global_rank: {trainer.global_rank}")
    if trainer.global_rank is None or trainer.global_rank == 0:
        # 评估模型
        result = trainer.test(model, dataloaders=mnist_dataset.test_dataloader())
        print(f"test result: {result}")
        # 预测
        data, label = next(iter(mnist_dataset.test_data))
        model.eval()
        print("*********")
        # trainer.predict(model, dataloaders=mnist_val, return_predictions=True)
        y = model.to("cpu")(data.view(784))
        print(f"Softmax(y)：{torch.argsort(y)}, label：{label}")
    print("end!")

