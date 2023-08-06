# -*- coding: utf-8 -*-
import tensorflow as tf
import tensorflow_datasets as tfds
from pyskydl.core.default_data_module import DefaultDataModule
from pyskydl.core.super_tf_dataset_builder import SuperDatasetBuilder


class MinistDataModule(DefaultDataModule):

    def __init__(self, batch_size: int, epochs: int):
        def map_fn_feature_label(feature, label):
            feature = feature / 255
            feature = tf.squeeze(feature)
            return feature, label

        dateset_name = "mnist"
        self.train_data = SuperDatasetBuilder.load_batched_datasets(dateset_name,
                                                               map_fn_feature_label=map_fn_feature_label,
                                                               split=[tfds.Split.TRAIN],
                                                               batch_size=batch_size,
                                                               epochs=epochs)
        self.test_data = SuperDatasetBuilder.load_batched_datasets(dateset_name,
                                                              map_fn_feature_label=map_fn_feature_label,
                                                              split=[tfds.Split.TEST],
                                                              batch_size=SuperDatasetBuilder.get_num_examples(
                                                                  dateset_name, tfds.Split.TEST))
        self.data_info = SuperDatasetBuilder.get_info(dateset_name)

    def train_dataloader(self):
        return self.train_data

    def val_dataloader(self):
        return None

    def test_dataloader(self):
        return self.test_data

    def predict_dataloader(self):
        return None

