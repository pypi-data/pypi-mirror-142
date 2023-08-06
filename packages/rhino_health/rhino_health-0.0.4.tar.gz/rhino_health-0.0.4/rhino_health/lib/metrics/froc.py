from typing import Optional

from rhino_health.lib.metrics.base_metric import BaseMetric
from rhino_health.lib.metrics.filter_variable import FilterVariable


class FRoc(BaseMetric):
    y_true_variable: FilterVariable
    y_pred_variable: FilterVariable
    specimen_variable: FilterVariable

    def metric_name(self):
        return "froc"


class FRocWithCI(FRoc):
    confidence_interval: int
    bootstrap_iterations: Optional[int] = None

    def metric_name(self):
        return "froc_with_ci"
