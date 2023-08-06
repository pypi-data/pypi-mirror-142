from rhino_health.lib.metrics.base_metric import BaseMetric
from rhino_health.lib.metrics.filter_variable import OptionalFilterVariableType


class Count(BaseMetric):
    variable: OptionalFilterVariableType

    def metric_name(self):
        return "count"


class Mean(BaseMetric):
    variable: OptionalFilterVariableType

    def metric_name(self):
        return "mean"


class StandardDeviation(BaseMetric):
    variable: OptionalFilterVariableType

    def metric_name(self):
        return "std"
