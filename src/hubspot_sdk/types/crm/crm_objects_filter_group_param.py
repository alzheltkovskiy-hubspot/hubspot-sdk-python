# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .crm_objects_filter_param import CRMObjectsFilterParam

__all__ = ["CRMObjectsFilterGroupParam"]


class CRMObjectsFilterGroupParam(TypedDict, total=False):
    filters: Required[Iterable[CRMObjectsFilterParam]]
