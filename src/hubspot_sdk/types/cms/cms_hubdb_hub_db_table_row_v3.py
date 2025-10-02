# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CmsHubdbHubDBTableRowV3"]


class CmsHubdbHubDBTableRowV3(BaseModel):
    values: Dict[str, object]

    id: Optional[str] = None

    child_table_id: Optional[str] = FieldInfo(alias="childTableId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    name: Optional[str] = None

    path: Optional[str] = None

    published_at: Optional[datetime] = FieldInfo(alias="publishedAt", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
