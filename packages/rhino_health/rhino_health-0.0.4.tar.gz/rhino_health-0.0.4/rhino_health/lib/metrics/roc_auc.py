from typing import Optional, Union

from rhino_health.lib.metrics.base_metric import BaseMetric
from rhino_health.lib.metrics.filter_variable import FilterVariable


class RocAuc(BaseMetric):
    y_true_variable: Union[str, FilterVariable]
    y_pred_variable: Union[str, FilterVariable]

    def metric_name(self):
        return "roc"


class RocAucWithCI(RocAuc):
    confidence_interval: int
    bootstrap_iterations: Optional[int] = None

    def metric_name(self):
        return "roc_with_ci"
