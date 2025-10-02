# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .crm_pipelines_pipeline_stage import CRMPipelinesPipelineStage

__all__ = ["CRMPipelinesPipeline"]


class CRMPipelinesPipeline(BaseModel):
    id: str

    archived: bool

    created_at: datetime = FieldInfo(alias="createdAt")

    display_order: int = FieldInfo(alias="displayOrder")

    label: str

    stages: List[CRMPipelinesPipelineStage]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
