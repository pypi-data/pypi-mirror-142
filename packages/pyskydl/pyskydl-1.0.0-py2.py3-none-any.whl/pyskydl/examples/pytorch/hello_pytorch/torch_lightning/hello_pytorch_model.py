# -*- coding: utf-8 -*-
import torch
from torch.autograd.variable import Variable

from pyskydl.core.enums import TrainPhaseEnum
from pyskydl.core.default_torch_lightning_model import DefaultTorchLightningModel
from pyskydl.examples.pytorch.hello_pytorch.torch_lightning.hello_pytorch_net import HelloPyTorchNet
from skydl.common.common_utils import CommonUtils


class HelloPyTorchModel(DefaultTorchLightningModel):
    """My Pytorch Model"""
    def adjust_parse_args_value(self):
        super().adjust_parse_args_value()
        self.parser_args.data_path = "/Users/tony/deep_learning_can_not_delete/data"
        self.parser_args.onnx_export_path = "/Users/tony/deep_learning_can_not_delete/saved_model"
        self.parser_args.use_cuda = True
        self.parser_args.init_from_saver = False
        self.parser_args.train_phase = TrainPhaseEnum.Fit.value
        self.parser_args.model_version = '20210701001'
        self.parser_args.epochs = 1
        self.parser_args.batch_size = 128
        self.parser_args.log_interval = 100
        self.parser_args.keep_prob = 0.25

    def build_network(self):
        return HelloPyTorchNet(self.name, self.parser_args)

    def export_to_onnx(self, input_shape):
        """
        save model and export to onnx
        参考：https://github.com/PyTorchLightning/pytorch-lightning/blob/master/tests/models/test_onnx.py
        :param input_shape 为model(input)的input的shape，shape顺序同[channel, height, width]或[channel, height*width] e.g. [1, 28, 28]
        :return:
        """
        export_path = self.parser_args.onnx_export_path + "/" + self.name
        CommonUtils.mkdirs(export_path)  # 如果路径不存在，就创建这个路径
        torch.save(self.net.state_dict(), export_path + "/" + self.name)
        self.log.info('The model was saved to: ' + export_path + "/" + self.name)
        save_to_onnx_path = export_path + "/" + self.name + ".onnx.pb"
        # dummy_input = torch.Tensor(input_shape)  # or torch.randn(input_shape)
        num_total = 1
        dummy_input = Variable(torch.randn(num_total, *input_shape).zero_())
        torch.onnx.export(self.net, dummy_input, save_to_onnx_path, verbose=True)
        self.log.info(f"The model was exported to: {save_to_onnx_path}")

