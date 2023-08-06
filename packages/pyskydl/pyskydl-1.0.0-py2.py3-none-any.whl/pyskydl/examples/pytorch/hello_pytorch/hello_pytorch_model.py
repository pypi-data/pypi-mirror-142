# -*- coding: utf-8 -*-
import torch
import os, datetime
import torch.optim as optim
import torch.nn.functional as F
from torch.autograd import Variable
from torchvision import datasets, transforms
from pyskydl.core.enums import TrainPhaseEnum
from pyskydl.core.torch_utils import TorchUtils
from skydl.common.annotations import PrintExecTime
from pyskydl.core.torch_modelv2 import TorchModelV2
from torch.utils.data import RandomSampler, DistributedSampler
from pyskydl.examples.pytorch.hello_pytorch.hello_pytorch_net import HelloPyTorchNet


class HelloPyTorchModel(TorchModelV2):
    """My Pytorch Model"""
    def adjust_parse_args_value(self):
        super().adjust_parse_args_value()
        self.parser_args.data_path = "/Users/tony/deep_learning_can_not_delete/data"
        self.parser_args.onnx_export_path = "/Users/tony/deep_learning_can_not_delete/saved_model"
        self.parser_args.use_cuda = True
        self.parser_args.init_from_saver = True
        self.parser_args.train_phase = TrainPhaseEnum.Fit.value
        self.parser_args.model_version = '20210701001'
        self.parser_args.epochs = 1
        self.parser_args.batch_size = 128
        self.parser_args.log_interval = 100
        self.parser_args.keep_prob = 0.25

    def build_network(self):
        return HelloPyTorchNet(self.name if self.name else self.__class__.__name__, self.parser_args).to(self.device)

    def load_data(self):
        # DistributedSampler
        dataset = datasets.MNIST(self.parser_args.data_path, train=True, download=True,
                           transform=transforms.Compose([
                               transforms.ToTensor(),
                               transforms.Normalize((0.1307,), (0.3081,))
                           ]))
        dataset_sampler = RandomSampler(dataset) if self.parser_args.ddp_local_rank == -1 else DistributedSampler(dataset)
        # Data loaders
        # kwargs = {'num_workers': 1, 'pin_memory': True} if self.parser_args.use_cuda else {}
        kwargs = {}
        train_loader = torch.utils.data.DataLoader(dataset, sampler=dataset_sampler, batch_size=self.parser_args.batch_size, shuffle=False, **kwargs)
        test_loader = torch.utils.data.DataLoader(
            datasets.MNIST(self.parser_args.data_path, train=False, download=True, transform=transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize((0.1307,), (0.3081,))
            ])),
            batch_size=self.parser_args.batch_size, shuffle=True, **kwargs)
        return train_loader, test_loader

    @PrintExecTime(enable_print=True, time_unit="seconds")
    def fit(self, train_dataloaders, val_dataloaders):
        train_data, test_data = train_dataloaders, val_dataloaders
        valid_data = test_data  # xxx
        print('[' + self.name + ']==>>> total training batch number: {}'.format(len(train_data)))
        print('[' + self.name + ']==>>> total validation batch number: {}'.format(len(valid_data)))
        print('[' + self.name + ']==>>> total testing batch number: {}'.format(len(test_data)))
        print(self.name + ", begin to fitting model, Time: {}".format(datetime.datetime.now()))
        optimizer = optim.SGD(self.net.parameters(), lr=self.parser_args.learning_rate, momentum=self.parser_args.momentum)
        for epoch in range(self.parser_args.epochs):
            print(f"epoch>>>{epoch}")
            self.do_train_from_numpy_data(self.net, self.device, train_data, len(train_data) * self.parser_args.batch_size, optimizer, epoch)
            # self.model.do_train_from_numpy_data(self.model, self.device, valid_data, len(test_data), optimizer, epoch)
        self.do_test_from_numpy_data(self.net, self.device, test_data, len(test_data) * self.parser_args.batch_size)
        self.export_to_onnx(self.net, [1, 28, 28])

    def evaluate(self, test_dataloaders):
        pass

    def predict(self, *args, **kwargs):
        pass

    def export_to_onnx(self, model, input_shape_channel_height_width):
        """
        save model and export to onnx
        :param model 继承SuperPytorchNet(nn.Module)
        :param input_channel_height_width_shape 为model(input)的input的shape e.g. 【1, 28, 28】
        :return:
        """
        export_path = self.parser_args.onnx_export_path + "/" + self.name
        if not os.path.exists(export_path):
            os.makedirs(export_path)
        torch.save(model.state_dict(), export_path + "/" + self.name)
        print('The model was saved to: ' + export_path + "/" + self.name)
        model.eval()
        num_total = 1
        dummy_input = Variable(torch.randn(num_total, *input_shape_channel_height_width).zero_().to(self.device))
        torch.onnx.export(model, dummy_input, export_path + "/" + self.name + ".onnx.pb", verbose=False)
        print('The model was exported to: ' + export_path + "/" + self.name + ".onnx.pb")

    def do_train_from_numpy_data(self, model, device, np_train_data, num_total, optimizer, epoch):
        """
        子类可以重写该方法
        :param args:
        :param model: SuperPytorchNet(nn.Module)
        :param device:
        :param train_loader:
        :param optimizer:
        :param epoch:
        :return:
        """
        self.net.train(True)
        for batch_idx, (data, label) in enumerate(np_train_data):
            # data, label = TorchUtils.np_to_tensor(data).to(device), torch.nn.functional.one_hot(TorchUtils.np_to_tensor(label)).to(device)
            data, label = TorchUtils.np_to_tensor(data).to(device, dtype=torch.float32), TorchUtils.np_to_tensor(label).to(device, dtype=torch.int32)
            data = data.view(-1, 1, 28, 28)
            label = label.view([-1])
            # to avoid: CUDA error: out of memory
            data, label = Variable(data), Variable(label).long()
            optimizer.zero_grad()
            output = model(data)  # 调用SuperPytorchNet(nn.Module)的__call__方法, 执行net类的forward方法
            loss = F.cross_entropy(output, label).to(device)
            loss.backward()
            optimizer.step()
            if batch_idx % self.parser_args.log_interval == 0:
                print('Train Epoch: {} [{}/{} ({:.2f}%)]\tLoss: {:.6f}'.format(
                    epoch, batch_idx * len(data), num_total, 100.00 * batch_idx / num_total, loss.item()))

    def do_test_from_numpy_data(self, model, device, np_test_data, num_total):
        """
        子类可以重写该方法
        :param args:
        :param model:
        :param device:
        :param test_loader:
        :return:
        """
        self.net.eval()
        test_loss = 0
        correct = 0
        with torch.no_grad():
            for batch_idx, (data, label) in enumerate(np_test_data):
                data, label = TorchUtils.np_to_tensor(data).to(device, dtype=torch.float32), TorchUtils.np_to_tensor(label).to(device, dtype=torch.int32)
                data = data.view(-1, 1, 28, 28)
                label = label.view([-1])
                # # to avoid: CUDA error: out of memory
                data, label = Variable(data), Variable(label).long()
                output = model(data)
                test_loss += F.nll_loss(output, label, reduction='sum').item()  # sum up batch loss
                pred = output.max(1, keepdim=True)[1]  # get the index of the max log-probability
                correct += pred.eq(label.view_as(pred)).sum().item()
        test_loss /= num_total
        print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.2f}%)\n'.format(
            test_loss, correct, num_total,
            100.00 * correct / num_total))


