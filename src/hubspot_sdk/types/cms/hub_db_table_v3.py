# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .column import Column
from ..._models import BaseModel
from .simple_user import SimpleUser

__all__ = ["HubDBTableV3"]


class HubDBTableV3(BaseModel):
    deleted_at: datetime = FieldInfo(alias="deletedAt")

    label: str

    name: str

    id: Optional[str] = None

    allow_child_tables: Optional[bool] = FieldInfo(alias="allowChildTables", default=None)

    allow_public_api_access: Optional[bool] = FieldInfo(alias="allowPublicApiAccess", default=None)

    column_count: Optional[int] = FieldInfo(alias="columnCount", default=None)

    columns: Optional[List[Column]] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[SimpleUser] = FieldInfo(alias="createdBy", default=None)

    deleted: Optional[bool] = None

    dynamic_meta_tags: Optional[Dict[str, int]] = FieldInfo(alias="dynamicMetaTags", default=None)

    enable_child_table_pages: Optional[bool] = FieldInfo(alias="enableChildTablePages", default=None)

    is_ordered_manually: Optional[bool] = FieldInfo(alias="isOrderedManually", default=None)

    published: Optional[bool] = None

    published_at: Optional[datetime] = FieldInfo(alias="publishedAt", default=None)

    row_count: Optional[int] = FieldInfo(alias="rowCount", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    updated_by: Optional[SimpleUser] = FieldInfo(alias="updatedBy", default=None)

    use_for_pages: Optional[bool] = FieldInfo(alias="useForPages", default=None)
