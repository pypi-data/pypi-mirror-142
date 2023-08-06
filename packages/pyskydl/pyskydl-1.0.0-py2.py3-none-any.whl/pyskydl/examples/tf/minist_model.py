# -*- coding: utf-8 -*-
import tensorflow as tf
import tensorflow_datasets as tfds
from pyskydl.core.enums import TrainPhaseEnum
from pyskydl.core.tf_keras_modelv2 import TfKerasModelV2


class MnistModel(TfKerasModelV2):
    """
    实现卷积神经网络CNN对MNIST数字分类
    """
    def adjust_parse_args_value(self):
        super().adjust_parse_args_value()
        self.parser_args.data_path = "/Users/tony/deep_learning_can_not_delete/data"
        self.parser_args.use_cuda = True
        self.parser_args.init_from_saver = True
        self.parser_args.fit_initial_epoch = 0
        self.parser_args.train_phase = TrainPhaseEnum.Fit.value
        self.parser_args.model_version = '20210830001'
        self.parser_args.epochs = 1
        self.parser_args.batch_size = 128
        self.parser_args.log_interval = 1000

    def fit(self, train_dataloaders, val_dataloaders):
        if not self.is_training_phase():
            return self
        # TODO restore mode from lastest checkpoint
        # 参考：https://github.com/tensorflow/tensorflow/issues/27909
        if self.parser_args.init_from_saver:
            checkpoint = tf.train.get_checkpoint_state(self.get_model_checkpoint_dir(), latest_filename=self.latest_model_filename)
            if checkpoint and checkpoint.saved_model_path:
                # saver.restore(sess, checkpoint.saved_model_path)
                self.log.info("Restored and Init Session Variables from Saver......")
            else:
                self.log.info(
                    "*** Error Occurred in " + self.parser_args.train_phase + " phase(1), Can not find the model file: "
                    + self.get_model_checkpoint_dir() + "/" + self.latest_model_filename)
                self.log.info("And you can ignore this error, then the trainning will go on......")

        # train model
        self.net.fit(train_dataloaders, epochs=self.parser_args.epochs, callbacks=self._fit_callbacks())
        self.net.build(input_shape=tf.compat.v1.data.get_output_shapes(train_dataloaders)[0])  # since tensorflow>=2.3.0, need call build() before call sumary()
        self.net.summary()
        return self

    def evaluate(self, test_dataloaders):
        # test mode
        test_loss, test_acc = self.net.evaluate(test_dataloaders)
        self.net.build(input_shape=tf.compat.v1.data.get_output_shapes(test_dataloaders)[0])  # since tensorflow>=2.3.0, need call build() before call sumary()
        self.net.summary()
        print('\nTest accuracy:', test_acc)
        return self

    def serving(self, *args, **kwargs):
        # restore weights from latest checkpoint
        latest_checkpoint = tf.train.latest_checkpoint(self.get_model_checkpoint_dir())
        if latest_checkpoint:
            self.net.load_weights(latest_checkpoint)
        saved_serving_path = self.parser_args.saved_model_path + "/serving/models/" + self.net.name() + "/" + self.parser_args.model_version
        _, evaluate_dataset, _ = self.load_data()

        # prediction mode
        for batched_examples in tfds.as_numpy(evaluate_dataset.take(1)):
            test_batched_features, test_batched_labels = batched_examples
        # predictions = self.net.predict(test_batched_features)
        # print("serving predict, real:", np.argmax(predictions[0]), test_batched_labels[0])

        # save model for tf serving
        if not self.net.inputs:
            self.net._set_inputs(test_batched_features)
        tf.saved_model.save(self.net, saved_serving_path)
        return self

