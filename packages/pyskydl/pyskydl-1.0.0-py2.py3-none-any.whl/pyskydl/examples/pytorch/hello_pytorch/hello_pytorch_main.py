# -*- coding: utf-8 -*-
from pyskydl.core.dist_strategy_config import TorchDistStrategyConfig
from pyskydl.examples.pytorch.hello_pytorch.hello_pytorch_model import HelloPyTorchModel
"""
run hello model with pytorch
参考：GETTING STARTED WITH DISTRIBUTED DATA PARALLEL https://pytorch.org/tutorials/intermediate/ddp_tutorial.html
"""


def run_model(rank: int, world_size: int):
    print(f"Running DDP on rank: {rank}, with world_size: {world_size}")
    model = HelloPyTorchModel(
        "my_torch_model",
        TorchDistStrategyConfig(
            name="ddp",
            init_method="tcp://127.0.0.1:12345",
            rank=rank,
            local_rank=rank,
            world_size=world_size
        )
    ).compile(
    )
    train_dataloader, val_dataloader = model.load_data()
    model.fit(train_dataloader, val_dataloader)
    model.evaluate(val_dataloader)


if __name__ == '__main__':
    HelloPyTorchModel.spawn(run_model, args=(2,), nprocs=2)  # 每节点2gpu、共使用2gpu、在1节点上开启2进程














