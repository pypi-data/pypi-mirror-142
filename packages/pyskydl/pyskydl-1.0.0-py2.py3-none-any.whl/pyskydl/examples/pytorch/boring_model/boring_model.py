# -*- coding: utf-8 -*-
from pyskydl.core.enums import TrainPhaseEnum
from pyskydl.core.default_torch_lightning_model import DefaultTorchLightningModel
from pyskydl.examples.pytorch.boring_model.boring_net import BoringNet


class BoringModel(DefaultTorchLightningModel):
    """boring pytorch model"""
    def adjust_parse_args_value(self):
        super().adjust_parse_args_value()
        self.parser_args.data_path = "/Users/tony/deep_learning_can_not_delete/data"
        self.parser_args.onnx_export_path = "/Users/tony/deep_learning_can_not_delete/saved_model"
        self.parser_args.use_cuda = True
        self.parser_args.init_from_saver = True
        self.parser_args.train_phase = TrainPhaseEnum.Fit.value
        self.parser_args.model_version = "20210825004"
        self.parser_args.epochs = 1
        self.parser_args.batch_size = 128
        self.parser_args.log_interval = 100
        self.parser_args.keep_prob = 0.25

    def build_network(self):
        # return BoringNet(self.name if self.name else self.__class__.__name__, self.parser_args).to(self.device)
        return BoringNet(self.name if self.name else self.__class__.__name__, self.parser_args)

