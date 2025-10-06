# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .value_with_timestamp import ValueWithTimestamp

__all__ = ["SimplePublicUpsertObject"]


class SimplePublicUpsertObject(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    new: bool

    properties: Dict[str, str]

    updated_at: datetime = FieldInfo(alias="updatedAt")

    archived: Optional[bool] = None

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)

    object_write_trace_id: Optional[str] = FieldInfo(alias="objectWriteTraceId", default=None)

    properties_with_history: Optional[Dict[str, List[ValueWithTimestamp]]] = FieldInfo(
        alias="propertiesWithHistory", default=None
    )
