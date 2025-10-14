# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HubDBTableRowV3"]


class HubDBTableRowV3(BaseModel):
    values: Dict[str, object]
    """List of key value pairs with the column name and column value"""

    id: Optional[str] = None
    """The id of the table row"""

    child_table_id: Optional[str] = FieldInfo(alias="childTableId", default=None)
    """Specifies the value for the column child table id"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp at which the row is created"""

    name: Optional[str] = None
    """
    Specifies the value for `hs_name` column, which will be used as title in the
    dynamic pages
    """

    path: Optional[str] = None
    """
    Specifies the value for `hs_path` column, which will be used as slug in the
    dynamic pages
    """

    published_at: Optional[datetime] = FieldInfo(alias="publishedAt", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp at which the row is updated last time"""
