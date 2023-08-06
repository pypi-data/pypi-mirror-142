# -*- coding: utf-8 -*-
import pytorch_lightning as pl
from pyskydl.core.dist_strategy_config import TorchDistStrategyConfig
from pyskydl.examples.pytorch.boring_model.boring_model import BoringModel
"""run boring model"""


def run_model():
    # build model
    model = BoringModel(
        "boring_model",
        TorchDistStrategyConfig(
            name="dp",
            num_gpus=2,
            num_nodes=1
        )
    ).compile()
    # set pytorch-lightning trainer to model
    model.set_pl_trainer(pl.Trainer(
        precision=32,  # 训练精度，在GPU上可以选16，在CPU模式下选择32。可选项有：32、16
        limit_train_batches=1.0,  # 可用于小数据调试。e.g. 1.0、0.25
        max_epochs=model.parser_args.epochs,  # 最大训练周期数
        accelerator=model.parser_args.ddp_name,  # 加速模式选择"dp、ddp、ddp2"，而不是None或其它，在多gpu模式下resume_from_checkpoint才生效
        gpus=model.parser_args.ddp_num_gpus,  # 每个训练节点上的gpu个数
        num_nodes=model.parser_args.ddp_num_nodes,  # 训练节点个数
        resume_from_checkpoint=model.get_last_checkpoint_file_name()  # 从上次断点处恢复模型
    ))
    # build data module
    train_dataloader = model.net.train_dataloader()
    val_dataloader = model.net.val_dataloader()
    test_dataloader = model.net.test_dataloader()
    # fit model
    model.fit(train_dataloader, val_dataloader)
    # evaluate model
    model.evaluate(test_dataloader)
    # export model to onnx
    batch = next(iter(model.net.val_dataloader()))
    input_data = batch[0]
    model.export_to_onnx(input_shape=input_data.shape)
    # predict model
    results = model.predict(model.net.predict_dataloader())
    print(f"predict results: {results}")


if __name__ == '__main__':
    run_model()
