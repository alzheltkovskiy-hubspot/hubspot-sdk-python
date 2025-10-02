# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CRMObjectsValueWithTimestamp"]


class CRMObjectsValueWithTimestamp(BaseModel):
    source_type: str = FieldInfo(alias="sourceType")

    timestamp: datetime

    value: str

    source_id: Optional[str] = FieldInfo(alias="sourceId", default=None)

    source_label: Optional[str] = FieldInfo(alias="sourceLabel", default=None)

    updated_by_user_id: Optional[int] = FieldInfo(alias="updatedByUserId", default=None)
