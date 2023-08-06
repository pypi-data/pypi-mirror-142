import torch.nn.functional as F

from .metrics_registering import do_register_metric_func

do_register_metric_func(F.cross_entropy)
do_register_metric_func(F.kl_div)
do_register_metric_func(F.binary_cross_entropy, ['binary_cross_entropy', 'bce'], unique_name='bce')
do_register_metric_func(
    F.binary_cross_entropy_with_logits,
    ['binary_cross_entropy_with_logits', 'bce_with_logits'],
    unique_name='bce_with_logits',
)
do_register_metric_func(F.poisson_nll_loss, unique_name='poisson_nll')
do_register_metric_func(F.hinge_embedding_loss, unique_name='hinge_embedding')
do_register_metric_func(F.l1_loss, unique_name='l1')
do_register_metric_func(F.mse_loss, unique_name='mse')
do_register_metric_func(F.multilabel_margin_loss, unique_name='multilabel_margin')
do_register_metric_func(F.multilabel_soft_margin_loss, unique_name='multilabel_soft_margin')
do_register_metric_func(F.multi_margin_loss, unique_name='multi_margin')
do_register_metric_func(F.nll_loss, unique_name='nll')
do_register_metric_func(F.smooth_l1_loss, unique_name='smooth_l1')
do_register_metric_func(F.soft_margin_loss, unique_name='soft_margin')
