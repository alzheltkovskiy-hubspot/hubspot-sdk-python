# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .pipeline_stage_input_param import PipelineStageInputParam

__all__ = ["PipelineCreateParams"]


class PipelineCreateParams(TypedDict, total=False):
    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]

    label: Required[str]

    stages: Required[Iterable[PipelineStageInputParam]]
