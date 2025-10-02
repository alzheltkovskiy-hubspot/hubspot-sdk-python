# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .crm_pipelines_public_audit_info import CRMPipelinesPublicAuditInfo

__all__ = ["CRMPipelinesCollectionResponsePublicAuditInfoNoPaging"]


class CRMPipelinesCollectionResponsePublicAuditInfoNoPaging(BaseModel):
    results: List[CRMPipelinesPublicAuditInfo]
