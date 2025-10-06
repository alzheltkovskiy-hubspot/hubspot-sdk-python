# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicAuditInfo"]


class PublicAuditInfo(BaseModel):
    action: str

    identifier: str

    portal_id: int = FieldInfo(alias="portalId")

    from_user_id: Optional[int] = FieldInfo(alias="fromUserId", default=None)

    message: Optional[str] = None

    raw_object: Optional[object] = FieldInfo(alias="rawObject", default=None)

    timestamp: Optional[datetime] = None
