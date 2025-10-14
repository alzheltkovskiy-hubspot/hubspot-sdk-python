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
    """Label of the table"""

    name: str
    """Name of the table"""

    id: Optional[str] = None
    """Id of the table"""

    allow_child_tables: Optional[bool] = FieldInfo(alias="allowChildTables", default=None)
    """Specifies whether child tables can be created"""

    allow_public_api_access: Optional[bool] = FieldInfo(alias="allowPublicApiAccess", default=None)
    """Specifies whether the table can be read by public without authorization"""

    column_count: Optional[int] = FieldInfo(alias="columnCount", default=None)
    """Number of columns including deleted"""

    columns: Optional[List[Column]] = None
    """List of columns in the table"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp at which the table is created"""

    created_by: Optional[SimpleUser] = FieldInfo(alias="createdBy", default=None)

    deleted: Optional[bool] = None

    dynamic_meta_tags: Optional[Dict[str, int]] = FieldInfo(alias="dynamicMetaTags", default=None)
    """
    Specifies the key value pairs of the
    [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
    with the associated column IDs.
    """

    enable_child_table_pages: Optional[bool] = FieldInfo(alias="enableChildTablePages", default=None)
    """Specifies creation of multi-level dynamic pages using child tables"""

    is_ordered_manually: Optional[bool] = FieldInfo(alias="isOrderedManually", default=None)

    published: Optional[bool] = None

    published_at: Optional[datetime] = FieldInfo(alias="publishedAt", default=None)
    """Timestamp at which the table is published recently"""

    row_count: Optional[int] = FieldInfo(alias="rowCount", default=None)
    """Number of rows in the table"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp at which the table is updated recently"""

    updated_by: Optional[SimpleUser] = FieldInfo(alias="updatedBy", default=None)

    use_for_pages: Optional[bool] = FieldInfo(alias="useForPages", default=None)
    """Specifies whether the table can be used for creation of dynamic pages"""
