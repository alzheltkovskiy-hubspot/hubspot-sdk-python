# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List

from pydantic import Field as FieldInfo

from .styles import Styles
from ...._models import BaseModel
from .row_meta_data import RowMetaData

__all__ = ["LayoutSection"]


class LayoutSection(BaseModel):
    cells: List["LayoutSection"]

    css_class: str = FieldInfo(alias="cssClass")

    css_id: str = FieldInfo(alias="cssId")

    css_style: str = FieldInfo(alias="cssStyle")

    label: str

    name: str

    params: Dict[str, object]

    row_meta_data: List[RowMetaData] = FieldInfo(alias="rowMetaData")

    rows: List[Dict[str, "LayoutSection"]]

    styles: Styles

    type: str

    w: int

    x: int
