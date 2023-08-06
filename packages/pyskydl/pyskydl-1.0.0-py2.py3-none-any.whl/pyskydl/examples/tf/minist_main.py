# -*- coding: utf-8 -*-
from tensorflow import keras
from pyskydl.examples.tf.minist_model import MnistModel
from pyskydl.examples.tf.minist_data import MinistDataModule
from pyskydl.core.tf_keras_lossesv2 import CustomTfKerasLossV2
from pyskydl.core.tf_keras_layersv2 import TfReLU, CustomDenseTfLayer, my_relu_def


def run_model():
    """run model"""
    # build model
    model = MnistModel("tf_mnist_model", [
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dropout(0.1),
        CustomDenseTfLayer(units=128, activation=TfReLU(my_relu_def)),
        CustomDenseTfLayer(units=10, activation="softmax")
    ]).compile(
        loss=keras.losses.sparse_categorical_crossentropy,
        # loss=CustomTfKerasLossV2(),
        # optimizer=keras.optimizers.Adam(),
        optimizer="adam",
        metrics=['accuracy']
        # ['accuracy', keras.metrics.Precision(), keras.metrics.Recall()]
    )
    # build data module
    data_module = MinistDataModule(model.parser_args.batch_size, model.parser_args.epochs)
    # fit model
    model.fit(data_module.train_dataloader(), data_module.val_dataloader())
    # evaluate model
    model.evaluate(data_module.test_dataloader())


if __name__ == '__main__':
    run_model()
