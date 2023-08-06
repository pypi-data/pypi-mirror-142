from typing import Dict

import numpy as np

from .callbacks import Callback


class EarlyStopping(Callback):
    """
    The source code of this class is under the MIT License and was copied from the Keras project,
    and has been modified.

    Stop training when a monitored quantity has stopped improving.

    Args:
        monitor (str): Quantity to be monitored.
        min_delta (float): Minimum change in the monitored quantity to qualify as an improvement,
            i.e. an absolute change of less than min_delta, will count as no improvement.
            (Default value = 0)
        patience (int): Number of epochs with no improvement after which training will be stopped.
            (Default value = 0)
        verbose (bool): Whether to print when early stopping is done.
            (Default value = False)
        mode (str): One of {'min', 'max'}. In `min` mode, training will stop when the quantity
            monitored has stopped decreasing; in `max` mode it will stop when the quantity monitored has
            stopped increasing.
            (Default value = 'min')
    """

    def __init__(
        self,
        *,
        monitor: str = 'val_loss',
        min_delta: float = 0.0,
        patience: int = 0,
        verbose: bool = False,
        mode: str = 'min',
    ):
        super().__init__()

        self.monitor = monitor
        self.patience = patience
        self.verbose = verbose
        self.min_delta = min_delta
        self.wait = 0
        self.stopped_epoch = 0

        if mode not in ['min', 'max']:
            raise ValueError(f"Invalid mode '{mode}'")
        self.mode = mode

        if mode == 'min':
            self.min_delta *= -1
            self.monitor_op = np.less
        elif mode == 'max':
            self.min_delta *= 1
            self.monitor_op = np.greater

    def on_train_begin(self, logs: Dict):
        # Allow instances to be re-used
        self.wait = 0
        self.stopped_epoch = 0
        self.best = np.Inf if self.mode == 'min' else -np.Inf

    def on_epoch_end(self, epoch_number: int, logs: Dict):
        current = logs[self.monitor]
        if self.monitor_op(current - self.min_delta, self.best):
            self.best = current
            self.wait = 0
        else:
            self.wait += 1
            if self.wait >= self.patience:
                self.stopped_epoch = epoch_number
                self.model.stop_training = True
                if self.verbose:
                    print(f'Epoch {self.stopped_epoch}: early stopping')
