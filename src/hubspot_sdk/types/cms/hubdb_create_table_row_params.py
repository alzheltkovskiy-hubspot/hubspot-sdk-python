# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .cms_hubdb_variant_param import CmsHubdbVariantParam

__all__ = ["HubdbCreateTableRowParams"]


class HubdbCreateTableRowParams(TypedDict, total=False):
    values: Required[Dict[str, CmsHubdbVariantParam]]

    child_table_id: Annotated[int, PropertyInfo(alias="childTableId")]

    display_index: Annotated[int, PropertyInfo(alias="displayIndex")]

    name: str

    path: str
