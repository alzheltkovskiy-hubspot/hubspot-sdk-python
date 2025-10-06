# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PipelineStageInputParam"]


class PipelineStageInputParam(TypedDict, total=False):
    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]

    label: Required[str]

    metadata: Dict[str, str]
