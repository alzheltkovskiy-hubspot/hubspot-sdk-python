# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketingFormsDependentFieldFilter"]


class MarketingFormsDependentFieldFilter(BaseModel):
    operator: Literal[
        "eq",
        "neq",
        "contains",
        "doesnt_contain",
        "str_starts_with",
        "str_ends_with",
        "lt",
        "lte",
        "gt",
        "gte",
        "between",
        "not_between",
        "within_time_reverse",
        "within_time",
        "set_any",
        "set_not_any",
        "set_all",
        "set_not_all",
        "set_eq",
        "set_neq",
        "is_not_empty",
    ]

    range_end: str = FieldInfo(alias="rangeEnd")

    range_start: str = FieldInfo(alias="rangeStart")

    value: str

    values: List[str]
