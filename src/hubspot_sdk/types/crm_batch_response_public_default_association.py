# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .crm_public_default_association import CRMPublicDefaultAssociation
from .crm.associations.crm_associations_v4_standard_error_1 import CRMAssociationsV4StandardError1

__all__ = ["CRMBatchResponsePublicDefaultAssociation"]


class CRMBatchResponsePublicDefaultAssociation(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")

    results: List[CRMPublicDefaultAssociation]

    started_at: datetime = FieldInfo(alias="startedAt")

    status: Literal["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]

    errors: Optional[List[CRMAssociationsV4StandardError1]] = None

    links: Optional[Dict[str, str]] = None

    num_errors: Optional[int] = FieldInfo(alias="numErrors", default=None)

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
