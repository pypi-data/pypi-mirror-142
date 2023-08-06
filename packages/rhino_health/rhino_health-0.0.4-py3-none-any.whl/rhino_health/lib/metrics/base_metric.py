import json
from typing import Any, Dict, List, Optional

from pydantic import BaseModel

from rhino_health.lib.metrics.filter_variable import FilterType


class DataFilter(BaseModel):
    filter_column: str  # What column in the DF to filter against
    filter_value: Any  # What value to match against
    filter_type: Optional[FilterType] = FilterType.EQUAL


class GroupingData(BaseModel):
    groupings: List[str] = []  # A list of columns to group metric results by
    dropna: Optional[
        bool
    ] = True  # Should na values be dropped if in a grouping key, see pandas.groupby


class BaseMetric(BaseModel):
    data_filters: Optional[List[DataFilter]] = []  # We will filter in the order passed in
    group_by: Optional[GroupingData] = None
    timeout_seconds: Optional[
        float
    ] = 600.0  # Metric calculations that take longer than this time will timeout

    def metric_name(self):
        raise NotImplementedError

    def data(self):
        data = {
            "metric": self.metric_name(),
            "arguments": self.json(exclude_none=True, exclude={"timeout_seconds"}),
        }
        if self.timeout_seconds is not None:
            data["timeout_seconds"] = self.timeout_seconds
        return data


MetricResultDataType = Dict[str, Any]


class MetricResponse(BaseModel):
    # TODO: objects for specific endpoints
    output: MetricResultDataType  # if group_by is specified in the arguments, is a map of group: output

    def __init__(self, **data):
        if isinstance(data["output"], str):
            data["output"] = json.loads(data["output"])
        if "null" in data["output"].keys() and len(data["output"].keys()) == 1:
            data["output"] = data["output"]["null"]
        super(MetricResponse, self).__init__(**data)
