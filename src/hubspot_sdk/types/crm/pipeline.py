# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .pipeline_stage import PipelineStage

__all__ = ["Pipeline"]


class Pipeline(BaseModel):
    id: str

    archived: bool

    created_at: datetime = FieldInfo(alias="createdAt")

    display_order: int = FieldInfo(alias="displayOrder")

    label: str

    stages: List[PipelineStage]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
