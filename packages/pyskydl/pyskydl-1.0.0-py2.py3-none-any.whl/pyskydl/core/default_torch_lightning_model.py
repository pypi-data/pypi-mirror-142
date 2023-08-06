# -*- coding: utf-8 -*-
import torch
import pytorch_lightning as pl
from typing import Optional, Any
from pyskydl.core.enums import TrainPhaseEnum
from skydl.common.common_utils import CommonUtils
from skydl.common.annotations import PrintExecTime
from pyskydl.core.torch_modelv2 import TorchModelV2
from pytorch_lightning.utilities.cloud_io import load as pl_load
from pyskydl.core.dist_strategy_config import DistStrategyConfig
from pyskydl.core.default_torch_lightning_net import DefaultTorchLightningNet


class DefaultTorchLightningModel(TorchModelV2):
    """default pytorch-lightning model"""
    def __init__(self, name: str = None,
                 distribute_strategy_config: Optional[DistStrategyConfig] = None,
                 pl_trainer: Optional[pl.Trainer] = None,
                 loss=None,
                 optimizer=None,
                 metrics=None,
                 weights=None):
        super().__init__(name, loss, optimizer, metrics, weights, distribute_strategy_config)
        self.parser_args.checkpoint_path = self.get_model_checkpoint_dir()
        self.parser_args.last_checkpoint_file = self.parser_args.checkpoint_path + "/last.ckpt"
        if pl_trainer is None:
            # build python-lightning training
            self.trainer = pl.Trainer(
                precision=32,  # 训练精度，在GPU上可以选16，在CPU模式下选择32。可选项有：32、16
                limit_train_batches=1.0,  # 可用于小数据调试。e.g. 1.0、0.25
                max_epochs=self.parser_args.epochs,  # 最大训练周期数
                accelerator=self.parser_args.ddp_name,  # 加速模式选择"dp、ddp、ddp2"，而不是None或其它，在多gpu模式下resume_from_checkpoint才生效
                gpus=self.parser_args.ddp_num_gpus,  # 每个训练节点上的gpu个数
                num_nodes=self.parser_args.ddp_num_nodes,  # 训练节点个数
                resume_from_checkpoint=self.get_last_checkpoint_file_name()  # 从上次断点处恢复模型
            )
        else:
            self.pl_trainer = pl_trainer

    def adjust_parse_args_value(self):
        super().adjust_parse_args_value()
        self.parser_args.data_path = "/Users/tony/deep_learning_can_not_delete/data"
        self.parser_args.onnx_export_path = "/Users/tony/deep_learning_can_not_delete/saved_model"
        self.parser_args.use_cuda = True
        self.parser_args.init_from_saver = True
        self.parser_args.train_phase = TrainPhaseEnum.Fit.value
        self.parser_args.model_version = '20210825001'
        self.parser_args.epochs = 10
        self.parser_args.batch_size = 128
        self.parser_args.log_interval = 100
        self.parser_args.keep_prob = 0.25

    def build_network(self):
        # return DefaultTorchLightningNet(self.name if self.name else self.__class__.__name__, self.parser_args).to(self.device)
        return DefaultTorchLightningNet(self.name, self.parser_args)  # pytorch-lightning框架下不需要显示调用to(self.device)

    def get_last_checkpoint_file_name(self):
        """获取last checkpoint file name"""
        return self.parser_args.last_checkpoint_file if CommonUtils.path_exists(
            self.parser_args.last_checkpoint_file) and self.parser_args.init_from_saver else None

    def set_pl_trainer(self, pl_trainer: Optional[pl.Trainer] = None):
        """set pytorch-lightning trainer"""
        self.pl_trainer = pl_trainer
        return self

    @PrintExecTime(enable_print=True, time_unit="seconds")
    def fit(self, train_dataloaders, val_dataloaders):
        # fit model from checkpoint
        ckpt = pl_load(self.parser_args.last_checkpoint_file) if CommonUtils.path_exists(self.parser_args.last_checkpoint_file) and self.parser_args.init_from_saver else None
        ckpt_current_epoch = ckpt["epoch"] if ckpt is not None else 0
        if ckpt_current_epoch < self.parser_args.epochs:
            self.trainer.fit(self.net, train_dataloaders, val_dataloaders)
        else:
            self.log.warning(f"Skipping the fit process due to ckpt_current_epoch>=parser_args.epochs，ckpt_current_epoch：{ckpt_current_epoch}, parser_args.epochs：{self.parser_args.epochs}")

    def evaluate(self, test_dataloaders):
        """评估模型"""
        print(f"trainer.global_rank: {self.trainer.global_rank}")
        if self.trainer.global_rank is None or self.trainer.global_rank == 0:
            result = self.trainer.test(self.net, dataloaders=test_dataloaders)
            print(f"Testing result: {result}")

    @PrintExecTime
    def predict(self, predict_dataloaders) -> Any:
        """预测模型"""
        return self.trainer.predict(self.net, predict_dataloaders, return_predictions=True)

    def export_to_onnx(self, input_shape):
        """
        save model and export to onnx
        参考：https://github.com/PyTorchLightning/pytorch-lightning/blob/master/tests/models/test_onnx.py
        参考：Exporting PyTorch Lightning model to ONNX format https://tugot17.github.io/data-science-blog/onnx/tutorial/2020/09/21/Exporting-lightning-model-to-onnx.html
        :param input_shape 为model(input)的input的shape，shape顺序同[channel, height, width]或[channel, height*width] e.g. [1, 28, 28]
        :return:
        """
        export_path = self.parser_args.onnx_export_path + "/" + self.name
        CommonUtils.mkdirs(export_path)  # 如果路径不存在，就创建这个路径
        torch.save(self.net.state_dict(), export_path + "/" + self.name)
        self.log.info('The model was saved to: ' + export_path + "/" + self.name)
        save_to_onnx_path = export_path + "/" + self.name + ".onnx.pb"
        dummy_input = torch.Tensor(input_shape)  # or torch.randn(input_shape)
        torch.onnx.export(self.net, dummy_input, save_to_onnx_path, verbose=True)
        self.log.info(f"The model was exported to: {save_to_onnx_path}")











