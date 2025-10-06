# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ..filter_group_param import FilterGroupParam

__all__ = ["CompanySearchParams"]


class CompanySearchParams(TypedDict, total=False):
    after: str

    filter_groups: Annotated[Iterable[FilterGroupParam], PropertyInfo(alias="filterGroups")]

    limit: int

    properties: SequenceNotStr[str]

    query: str

    sorts: SequenceNotStr[str]
