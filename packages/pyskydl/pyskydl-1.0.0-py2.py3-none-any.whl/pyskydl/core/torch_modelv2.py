# -*- coding: utf-8 -*-
import sys
import random
import torch
import argparse
import numpy as np
import torch.distributed as dist
import torch.multiprocessing as mp
from pyskydl.core.modelv2 import ModelV2
from pyskydl.core.torch_netv2 import TorchNetV2
from pyskydl.core.torch_utils import TorchUtils
from logbook import Logger, StreamHandler, FileHandler
from torch.nn.parallel import DistributedDataParallel as DDP
from skydl.common.annotations import DeveloperAPI, PrintExecTime
from pyskydl.core.dist_strategy_config import DistStrategyConfig


class TorchModelV2(ModelV2):
    """
    pytorch model
    在线教程：https://github.com/zergtant/pytorch-handbook
    pytorch中文教程网：https://www.pytorchtutorial.com/
    Pytorch Seq2Seq篇 https://fgc.stpi.narl.org.tw/activity/videoDetail/4b1141305df38a7c015e194f22f8015b
    https://forums.fast.ai/t/converting-a-pytorch-model-to-tensorflow-or-keras-for-production/14016
    """
    @property
    def net(self) -> torch.nn.Module:
        """定义keras.Model返回值类型便于IDE找到对应的静态类"""
        return self._model

    def __init__(self, name: str = None,
                 loss=None,
                 optimizer=None,
                 metrics=None,
                 weights=None,
                 distribute_strategy_config: DistStrategyConfig = None):
        StreamHandler(sys.stdout).push_application()
        self._name = name
        self._log = Logger(self.name if self.name else self.__class__.__name__)
        # 分布式训练策略
        self._distribute_strategy_config = DistStrategyConfig.new_build() if distribute_strategy_config is None else distribute_strategy_config
        print(f"_distribute_strategy_config: {self._distribute_strategy_config}")
        self._parser = argparse.ArgumentParser()
        self._parser_args = None
        self._device = None
        self._num_gpus = 0
        self.do_parse_args()
        self._model = None if self.parser_args.lazy_load_model else self.build_network()
        # loss, optimizer, metrics, weights
        self._loss = loss
        self._optimizer = optimizer
        self._metrics = metrics
        self._weights = weights

    def add_parser_argument(self):
        """
        增加parser参数项
        子类需要重写该方法
        # super().add_parser_argument()
        """
        super().add_parser_argument()
        # 参考[Pytorch]基于混和精度的模型加速 https://zhpmatrix.github.io/2019/07/01/model-mix-precision-acceleration/
        self.parser.add_argument('--fp16', type=bool, default=False, metavar='F', help='Whether to use 16-bit float precision instead of 32-bit')
        self.parser.add_argument('--fp16_opt_level', type=str, default="01", metavar='FO', help='fp16_opt_level')
        # pytorch ddp分布式训练参数，每个gpu启动1个进程。参考：GETTING STARTED WITH DISTRIBUTED DATA PARALLEL https://pytorch.org/tutorials/intermediate/ddp_tutorial.html
        # 1.单机8卡分布式训练。这时的world size=8，即有8个进程，其rank编号分别为0-7，而local_rank也为0-7。
        # 2.双机16卡分布式训练。这时每台机器是8卡，总共16卡，world_size = 16，即有16个进程，其rank编号为0-15。
        # 但是在每台机器上，local_rank还是0-7，这是local rank与rank的区别，local rank会对应到实际的GPU ID上。
        self.parser.add_argument('--ddp_name', type=str, default="dp", metavar='N', help='pytorch DistributedDataPrallel strategy name: e.g. "dp"、"ddp"、"ddp2"')
        self.parser.add_argument('--ddp_backend', type=str, default="nccl", metavar='N', help='pytorch DistributedDataPrallel backend: e.g. "nccl"、"tcp"、"mpi"、"gloo"')
        self.parser.add_argument('--ddp_init_method', type=str, default="tcp://127.0.0.1:23456", metavar='I', help='pytorch DistributedDataPrallel init_method。e.g. dist.init_process_group("nccl", init_method="tcp://10.1.1.20:23456", rank=args.rank, world_size=4)')
        self.parser.add_argument('--ddp_rank', type=int, default=0, metavar='R', help='pytorch DistributedDataPrallel rank。global gpu id in all nodes，0 for master')
        self.parser.add_argument('--ddp_local_rank', type=int, default=-1, metavar='L', help='pytorch DistributedDataPrallel local_rank。local gpu id in per node, local_rank=-1即cpu模式；0即选择单机第1个gpu、1即选择单机第2个gpu')
        self.parser.add_argument('--ddp_world_size', type=int, default=1, metavar='W', help='pytorch DistributedDataPrallel world_size。world_size = num_nodes * num_gpus_per_node')
        self.parser.add_argument('--ddp_num_gpus', type=int, default=0, metavar='W', help='pytorch DistributedDataPrallel num_gpus')
        self.parser.add_argument('--ddp_num_nodes', type=int, default=1, metavar='W', help='pytorch DistributedDataPrallel num_nodes')

    def do_parse_args(self):
        self.add_parser_argument()
        self._parser_args = self.parser.parse_args()
        self.adjust_parse_args_value()
        self._num_gpus = TorchUtils.check_available_gpus(show_info=True)
        if self.distribute_strategy_config.is_instance_of_pytorch():
            # pytorch ddp分布式训练参数，每个gpu启动1个进程
            self.parser_args.ddp_backend = self.distribute_strategy_config.backend
            self.parser_args.ddp_init_method = self.distribute_strategy_config.init_method
            self.parser_args.ddp_rank = self.distribute_strategy_config.rank
            self.parser_args.ddp_local_rank = self.distribute_strategy_config.local_rank
            self.parser_args.ddp_world_size = self.distribute_strategy_config.world_size
            self.parser_args.ddp_num_gpus = self.distribute_strategy_config.num_gpus
            self.parser_args.ddp_num_nodes = self.distribute_strategy_config.num_nodes
        # Setup CUDA, GPU & distributed training
        if not self.parser_args.ddp_local_rank == -1 and self.parser_args.use_cuda:
            # Initializes the distributed backend which will take care of sychronizing nodes/GPUs
            torch.cuda.set_device(self.parser_args.ddp_local_rank)
            self._device = torch.device("cuda", self.parser_args.ddp_local_rank)
            # initialize the process group, if need to destroy, just using dist.destroy_process_group() on cleanup()
            dist.init_process_group(backend=self.parser_args.ddp_backend,
                                    init_method=self.parser_args.ddp_init_method,
                                    rank=self.parser_args.ddp_rank,
                                    world_size=self.parser_args.ddp_world_size)
            self._num_gpus = 1  # 每个GPU开启1个进程
        else:
            self._device = TorchUtils.device("gpu" if self.parser_args.use_cuda else "cpu")
        if self.num_gpus > 0:
            if not self.parser_args.use_cuda:
                self.log.info(f"WARNING: You have {self._num_gpus} CUDA device, so you should probably run with --cuda")
                self._num_gpus = 0  # 不使用GPU加速
        else:
            self.parser_args.use_cuda = False
        self.set_seed(seed=self.parser_args.seed, num_gpus=self.num_gpus)    # Added here for reproductibility
        self.log.info("PyTorch Version: " + torch.__version__ + "\nMain function argparse: " + str(self.parser_args))
        self.log.warning(
            f"Process rank: {self.parser_args.ddp_local_rank}, device: {self.device}, num_gpus: {self.num_gpus}, distributed training: {bool(self.parser_args.ddp_local_rank != -1)}, 16-bits training: {self.parser_args.fp16}"
        )

    def build_network(self):
        # return TorchNetV2(self.name if self.name else self.__class__.__name__, self.parser_args).to(self.device)
        return TorchNetV2(self.name, self.parser_args)

    @DeveloperAPI
    def compile(self, loss=None, optimizer=None, metrics=None):
        """
        Configures the model for training
        compile a model before training/testing
        inference阶段不需要调用模型的compile函数
        @see keras.models.Model.compile()
        :param loss:
        :param optimizer:
        :param metrics:
        :return: self
        """
        super().compile(loss, optimizer, metrics)
        if not self.parser_args.ddp_local_rank == -1 and self.parser_args.use_cuda:
            # model = DDP(model, device_ids=[int(i) for i in self.parser_args.ddp_all_ranks.split(",")], output_device=self.parser_args.ddp_local_rank)
            # device_ids中的第一个GPU（即device_ids[0]）和model.cuda()或torch.cuda.set_device()中的第一个GPU序号应保持一致，否则会报错。
            self._model = DDP(self._model, device_ids=[self.parser_args.ddp_local_rank], output_device=self.parser_args.ddp_local_rank)
        return self

    def set_seed(self, seed: int = 1, num_gpus: int = 0):
        """
        设置random seed确保每次训练都可以获得相同唯一的的随机序列
        """
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        if num_gpus > 0:
            torch.cuda.manual_seed_all(seed)

    def fit(self, train_dataloaders, val_dataloaders):
        """
        训练模型
        e.g. fit(loaded_dataset=[training_dataset, validation_dataset, evaluate_dataset])
        """
        if not self.is_training_phase():
            return self
        return self

    def evaluate(self, test_dataloaders):
        """评估模型"""
        pass

    def predict(self, predict_dataloaders):
        """预测模型"""
        pass

    @staticmethod
    @PrintExecTime(enable_print=True, time_unit="seconds")
    def spawn(fn, args=(), nprocs=1, join=True, daemon=False):
        """
        pytorch多进程方法
        ```
        e.g.
        def run_model(rank: int, world_size: int):
            print(f"Running DDP on rank: {rank}, with world_size: {world_size}")
            ......
        world_size = 1
        MyPyTorchModel.spawn(run_model, args=(world_size,), nprocs=world_size)  # 每节点2gpu、共使用1gpu、在1节点上开启1进程
        或：MyPyTorchModel.spawn(run_model, args=(2,), nprocs=2)  # 每节点2gpu、共使用2gpu、在1节点上开启2进程
        ```
        Arguments:
            fn (function): Function is called as the entrypoint of the
                spawned process. This function must be defined at the top
                level of a module so it can be pickled and spawned. This
                is a requirement imposed by multiprocessing.

                The function is called as ``fn(i, *args)``, where ``i`` is
                the process index and ``args`` is the passed through tuple
                of arguments.

            args (tuple): Arguments passed to ``fn``.
            nprocs (int): Number of processes to spawn.
            join (bool): Perform a blocking join on all processes.
            daemon (bool): The spawned processes' daemon flag. If set to True,
                           daemonic processes will be created.

        Returns:
            None if ``join`` is ``True``,
            :class:`~SpawnContext` if ``join`` is ``False``
        """
        mp.spawn(fn, args=args, nprocs=nprocs, join=join, daemon=daemon)
