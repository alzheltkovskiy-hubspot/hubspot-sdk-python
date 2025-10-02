# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PipelineUpdateParams"]


class PipelineUpdateParams(TypedDict, total=False):
    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    pipeline_id: Required[Annotated[str, PropertyInfo(alias="pipelineId")]]

    archived: bool

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]

    label: str

    metadata: Dict[str, str]
