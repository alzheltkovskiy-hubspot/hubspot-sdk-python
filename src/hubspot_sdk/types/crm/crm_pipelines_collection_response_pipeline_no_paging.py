# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .crm_pipelines_pipeline import CRMPipelinesPipeline

__all__ = ["CRMPipelinesCollectionResponsePipelineNoPaging"]


class CRMPipelinesCollectionResponsePipelineNoPaging(BaseModel):
    results: List[CRMPipelinesPipeline]
