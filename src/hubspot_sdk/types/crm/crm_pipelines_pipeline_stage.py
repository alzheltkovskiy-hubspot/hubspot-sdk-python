# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CRMPipelinesPipelineStage"]


class CRMPipelinesPipelineStage(BaseModel):
    id: str

    archived: bool

    created_at: datetime = FieldInfo(alias="createdAt")

    display_order: int = FieldInfo(alias="displayOrder")

    label: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)

    metadata: Optional[Dict[str, str]] = None

    write_permissions: Optional[Literal["CRM_PERMISSIONS_ENFORCEMENT", "READ_ONLY", "INTERNAL_ONLY"]] = FieldInfo(
        alias="writePermissions", default=None
    )
