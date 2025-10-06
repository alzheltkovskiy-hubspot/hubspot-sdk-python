# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..option import Option
from ..._models import BaseModel
from .foreign_id import ForeignID
from .simple_user import SimpleUser

__all__ = ["Column"]


class Column(BaseModel):
    label: str

    name: str

    type: Literal[
        "NULL",
        "TEXT",
        "NUMBER",
        "URL",
        "IMAGE",
        "SELECT",
        "MULTISELECT",
        "BOOLEAN",
        "LOCATION",
        "DATE",
        "DATETIME",
        "CURRENCY",
        "RICHTEXT",
        "FOREIGN_ID",
        "VIDEO",
        "CTA",
        "FILE",
        "JSON",
        "COMPOSITE",
        "CODE",
        "HUBSPOT_VIDEO",
        "EMBED",
    ]

    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[SimpleUser] = FieldInfo(alias="createdBy", default=None)

    created_by_user_id: Optional[int] = FieldInfo(alias="createdByUserId", default=None)

    deleted: Optional[bool] = None

    foreign_column_id: Optional[int] = FieldInfo(alias="foreignColumnId", default=None)

    foreign_ids: Optional[List[ForeignID]] = FieldInfo(alias="foreignIds", default=None)

    foreign_ids_by_id: Optional[Dict[str, ForeignID]] = FieldInfo(alias="foreignIdsById", default=None)

    foreign_ids_by_name: Optional[Dict[str, ForeignID]] = FieldInfo(alias="foreignIdsByName", default=None)

    foreign_table_id: Optional[int] = FieldInfo(alias="foreignTableId", default=None)

    option_count: Optional[int] = FieldInfo(alias="optionCount", default=None)

    options: Optional[List[Option]] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    updated_by: Optional[SimpleUser] = FieldInfo(alias="updatedBy", default=None)

    updated_by_user_id: Optional[int] = FieldInfo(alias="updatedByUserId", default=None)

    width: Optional[int] = None
