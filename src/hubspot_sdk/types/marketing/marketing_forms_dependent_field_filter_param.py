# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["MarketingFormsDependentFieldFilterParam"]


class MarketingFormsDependentFieldFilterParam(TypedDict, total=False):
    operator: Required[
        Literal[
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
    ]

    range_end: Required[Annotated[str, PropertyInfo(alias="rangeEnd")]]

    range_start: Required[Annotated[str, PropertyInfo(alias="rangeStart")]]

    value: Required[str]

    values: Required[SequenceNotStr[str]]
