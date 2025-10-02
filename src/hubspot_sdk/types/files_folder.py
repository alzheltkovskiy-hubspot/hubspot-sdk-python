# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FilesFolder"]


class FilesFolder(BaseModel):
    id: str

    archived: bool

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)

    name: Optional[str] = None

    parent_folder_id: Optional[str] = FieldInfo(alias="parentFolderId", default=None)

    path: Optional[str] = None
