 
import unittest

import torch
import torch.nn as nn

from  enaptorch import Model, EarlyStopping, Metric, Callback
from tests.framework.base import CaptureOutputBase
from tests.framework.tools import some_data_generator


class EarlyStoppingDummyMetric(Metric):
    __name__ = 'dummy'

    def __init__(self, values) -> None:
        super().__init__()
        self.values = values
        self.current_epoch = None

    def update(self, y_pred, y_true):
        pass

    def compute(self):
        return self.values[self.current_epoch - 1]

    def reset(self) -> None:
        pass


class DummyMetricCallback(Callback):
    def __init__(self, metric):
        super().__init__()
        self.metric = metric

    def on_epoch_begin(self, epoch_number: int, logs: dict):
        self.metric.current_epoch = epoch_number


class EarlyStoppingTest(CaptureOutputBase):
    batch_size = 20

    def setUp(self):
        torch.manual_seed(42)
        self.pytorch_network = nn.Linear(1, 1)
        self.loss_function = nn.MSELoss()
        self.optimizer = torch.optim.SGD(self.pytorch_network.parameters(), lr=1e-3)

    def test_integration(self):
        train_gen = some_data_generator(20)
        valid_gen = some_data_generator(20)
        earlystopper = EarlyStopping(monitor='val_loss', min_delta=0, patience=2, verbose=False)

        model = Model(self.pytorch_network, self.optimizer, self.loss_function)
        model.fit_generator(train_gen, valid_gen, epochs=10, steps_per_epoch=5, callbacks=[earlystopper])

    def test_early_stopping_patience_of_1(self):
        earlystopper = EarlyStopping(monitor='val_dummy', min_delta=0, patience=1, verbose=False)

        dummy_metric_values = [8, 4, 5, 2]
        early_stop_epoch = 3
        self._test_early_stopping(earlystopper, dummy_metric_values, early_stop_epoch)

    def test_early_stopping_with_delta(self):
        earlystopper = EarlyStopping(monitor='val_dummy', min_delta=3, patience=2, verbose=False)

        dummy_metric_values = [8, 4, 5, 2, 2]
        early_stop_epoch = 4
        self._test_early_stopping(earlystopper, dummy_metric_values, early_stop_epoch)

    def test_early_stopping_with_max(self):
        earlystopper = EarlyStopping(monitor='val_dummy', mode='max', min_delta=0, patience=2, verbose=False)

        dummy_metric_values = [2, 8, 4, 5, 2]
        early_stop_epoch = 4
        self._test_early_stopping(earlystopper, dummy_metric_values, early_stop_epoch)

    def test_mode_not_min_max_raise_error(self):
        with self.assertRaises(ValueError):
            invalid_mode = "a_mode"
            EarlyStopping(monitor='val_dummy', mode=invalid_mode, min_delta=0, patience=2, verbose=False)

    def test_early_stopping_with_verbose(self):
        earlystopper = EarlyStopping(monitor='val_dummy', mode='max', min_delta=0, patience=2, verbose=True)

        dummy_metric_values = [2, 8, 4, 5, 2]
        early_stop_epoch = 4

        self._capture_output()

        self._test_early_stopping(earlystopper, dummy_metric_values, early_stop_epoch)

        self.assertStdoutContains(['Epoch 4: early stopping'])

    def _test_early_stopping(self, earlystopper, dummy_metric_values, early_stop_epoch):
        dummy_metric = EarlyStoppingDummyMetric(dummy_metric_values)
        dummy_metric_callback = DummyMetricCallback(dummy_metric)

        train_gen = some_data_generator(EarlyStoppingTest.batch_size)
        valid_gen = some_data_generator(EarlyStoppingTest.batch_size)

        model = Model(self.pytorch_network, self.optimizer, self.loss_function, epoch_metrics=[dummy_metric])
        history = model.fit_generator(
            train_gen, valid_gen, epochs=10, steps_per_epoch=5, callbacks=[dummy_metric_callback, earlystopper]
        )
        self.assertEqual(len(history), early_stop_epoch)
        self.assertEqual(history[-1]['epoch'], early_stop_epoch)


if __name__ == '__main__':
    unittest.main()
