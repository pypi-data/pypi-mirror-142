# -*- coding: utf-8 -*-
from dataclasses import dataclass
from skydl.common.annotations import Override


class DistStrategyConfig:
    """分布式训练策略配置"""
    name: str = ""  # 分布式策略名称

    def with_name(self, name) -> str:
        self.name = name
        return self

    def is_instance_of_pytorch(self) -> bool:
        """是否pytorch的子类"""
        return isinstance(self, TorchDistStrategyConfig)

    @staticmethod
    def new_build() -> "DistStrategyConfig":
        return DistStrategyConfig()

    def build(self) -> "DistStrategyConfig":
        return self


@dataclass
class TorchDistStrategyConfig(DistStrategyConfig):
    """Pytorch分布式训练策略配置"""
    name: str = "ddp"  # 分布式策略名称，可参考pytorch-lightning的加速模式accelerator参数值。e.g. dp、ddp
    backend: str = "nccl"  # 进程之间使用的通信框架，有nccl,mpi,gloo,tcp
    init_method: str = "tcp://127.0.0.1:23456"  # 主进程的端口地址
    rank: int = 0  # 全局gpu id
    local_rank: int = -1  # 本地的gpu id
    world_size: int = 0  # 所有节点的gpu个数。计算方法：每个训练节点上的gpu个数 * 训练节点个数
    num_gpus: int = 0  # 每个训练节点上的gpu个数
    num_nodes: int = 1  # 训练节点个数

    def __init__(self, name: str = "ddp",
                 backend: str = "nccl",
                 init_method: str = "tcp://127.0.0.1:23456",
                 rank: int = 0,
                 local_rank: int = -1,
                 world_size: int = 0,
                 num_gpus: int = 0,
                 num_nodes: int = 1):
        self.name = name
        self.backend = backend
        self.init_method = init_method
        self.rank = rank
        self.local_rank = local_rank
        self.world_size = world_size
        self.num_gpus = num_gpus
        self.num_nodes = num_nodes

    @staticmethod
    @Override(DistStrategyConfig)
    def new_build() -> "TorchDistStrategyConfig":
        return TorchDistStrategyConfig()

    def with_backend(self, backend: str = "nccl") -> "TorchDistStrategyConfig":
        self.backend = backend

    def with_init_method(self, init_method: str="tcp://127.0.0.1:23456") -> "TorchDistStrategyConfig":
        self.init_method = init_method
        return self

    def with_rank(self, rank: int = 0) -> "TorchDistStrategyConfig":
        self.rank = rank
        return self

    def with_local_rank(self, local_rank: int = -1) -> "TorchDistStrategyConfig":
        self.local_rank = local_rank
        return self

    def with_world_size(self, world_size: int = 0) -> "TorchDistStrategyConfig":
        self.world_size = world_size
        return self

    def with_num_gpus(self, num_gpus: int = 0) -> "TorchDistStrategyConfig":
        self.num_gpus = num_gpus
        return self

    def with_num_nodes(self, num_nodes: int = 1) -> "TorchDistStrategyConfig":
        self.num_nodes = num_nodes
        return self


if __name__ == '__main__':
    # build distribute strategy config
    dist_strategy_config = TorchDistStrategyConfig.new_build()\
        .with_name("ddp")\
        .with_rank(0) \
        .with_local_rank(0) \
        .with_world_size(1)\
        .with_num_gpus(2)\
        .with_num_nodes(1)\
        .build()
    print(f"is_instance_of_pytorch：{dist_strategy_config.is_instance_of_pytorch()}")
    # build distribute strategy config from __init__
    dist_strategy_config2 = TorchDistStrategyConfig(
        name="dp",
        num_gpus=0,
        num_nodes=1
    )
    print(f"is_instance_of_pytorch2：{dist_strategy_config.is_instance_of_pytorch()}")

