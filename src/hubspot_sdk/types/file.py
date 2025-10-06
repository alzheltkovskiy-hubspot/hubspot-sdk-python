# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    id: str

    access: Literal[
        "PUBLIC_INDEXABLE",
        "PUBLIC_NOT_INDEXABLE",
        "HIDDEN_INDEXABLE",
        "HIDDEN_NOT_INDEXABLE",
        "HIDDEN_PRIVATE",
        "PRIVATE",
        "HIDDEN_SENSITIVE",
        "SENSITIVE",
    ]

    archived: bool

    created_at: datetime = FieldInfo(alias="createdAt")

    updated_at: datetime = FieldInfo(alias="updatedAt")

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)

    default_hosting_url: Optional[str] = FieldInfo(alias="defaultHostingUrl", default=None)

    encoding: Optional[str] = None

    expires_at: Optional[int] = FieldInfo(alias="expiresAt", default=None)

    extension: Optional[str] = None

    file_md5: Optional[str] = FieldInfo(alias="fileMd5", default=None)

    height: Optional[int] = None

    is_usable_in_content: Optional[bool] = FieldInfo(alias="isUsableInContent", default=None)

    name: Optional[str] = None

    parent_folder_id: Optional[str] = FieldInfo(alias="parentFolderId", default=None)

    path: Optional[str] = None

    size: Optional[int] = None

    source_group: Optional[str] = FieldInfo(alias="sourceGroup", default=None)

    type: Optional[str] = None

    url: Optional[str] = None

    width: Optional[int] = None
