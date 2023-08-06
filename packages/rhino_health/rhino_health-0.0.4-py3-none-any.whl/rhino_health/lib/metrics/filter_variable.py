from enum import Enum
from typing import Any, Optional, Union

from pydantic import BaseModel, validator


class FilterType(Enum):
    EQUAL = "="
    IN = "in"  # filter_value should be a list
    GREATER_THAN = ">"
    LESS_THAN = "<"
    GREATER_THAN_EQUAL = ">="
    LESS_THAN_EQUAL = "<="
    BETWEEN = "between"  # 2 conditions are specified and checked against


class FilterRangePair(BaseModel):
    filter_value: Any
    filter_type: FilterType  # A filter type (does not support BETWEEN and IN)

    @validator("filter_type")
    def only_base_operator_types(cls, value):
        if not value in [
            FilterType.EQUAL,
            FilterType.GREATER_THAN,
            FilterType.GREATER_THAN_EQUAL,
            FilterType.LESS_THAN,
            FilterType.LESS_THAN_EQUAL,
        ]:
            raise ValueError("Only base types are supported for ranges")


class FilterBetweenRange(BaseModel):
    lower: FilterRangePair  # A dict that defines the filter variable for the lower range
    upper: FilterRangePair  # A dict that defines the filter variable for the upper range


class FilterVariable(BaseModel):
    data_column: str  # The column in the remote cohort df to get data from
    filter_column: str  # The column in the remote cohort df to check against
    filter_value: Union[
        Any, FilterBetweenRange
    ]  # the value to match against or a FilterRange if filter_type is Between
    filter_type: Optional[FilterType] = FilterType.EQUAL


OptionalFilterVariableType = Union[str, FilterVariable]
