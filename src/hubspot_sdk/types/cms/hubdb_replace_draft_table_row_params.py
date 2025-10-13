# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .variant_param import VariantParam

__all__ = ["HubdbReplaceDraftTableRowParams"]


class HubdbReplaceDraftTableRowParams(TypedDict, total=False):
    table_id_or_name: Required[Annotated[str, PropertyInfo(alias="tableIdOrName")]]

    values: Required[Dict[str, VariantParam]]

    child_table_id: Annotated[int, PropertyInfo(alias="childTableId")]

    display_index: Annotated[int, PropertyInfo(alias="displayIndex")]

    name: str

    path: str
