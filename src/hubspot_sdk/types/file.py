# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    id: str
    """File ID."""

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
    """File access. Can be PUBLIC_INDEXABLE, PUBLIC_NOT_INDEXABLE, PRIVATE."""

    archived: bool
    """If the file is deleted."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Creation time of the file object."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of the latest update to the file."""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """Deletion time of the file object."""

    default_hosting_url: Optional[str] = FieldInfo(alias="defaultHostingUrl", default=None)
    """Default hosting URL of the file.

    This will use one of HubSpot's provided URLs to serve the file.
    """

    encoding: Optional[str] = None
    """Encoding of the file."""

    expires_at: Optional[int] = FieldInfo(alias="expiresAt", default=None)
    """The timestamp indicating when the file will expire."""

    extension: Optional[str] = None
    """Extension of the file. ex: .jpg, .png, .gif, .pdf, etc."""

    file_md5: Optional[str] = FieldInfo(alias="fileMd5", default=None)
    """The MD5 hash of the file."""

    height: Optional[int] = None
    """For image and video files, the height of the content."""

    is_usable_in_content: Optional[bool] = FieldInfo(alias="isUsableInContent", default=None)
    """Previously "archied".

    Indicates if the file should be used when creating new content like web pages.
    """

    name: Optional[str] = None
    """Name of the file."""

    parent_folder_id: Optional[str] = FieldInfo(alias="parentFolderId", default=None)
    """ID of the folder the file is in."""

    path: Optional[str] = None
    """Path of the file in the file manager."""

    size: Optional[int] = None
    """Size of the file in bytes."""

    source_group: Optional[str] = FieldInfo(alias="sourceGroup", default=None)
    """The group from which the file originated."""

    type: Optional[str] = None
    """Type of the file. Can be IMG, DOCUMENT, AUDIO, MOVIE, or OTHER."""

    url: Optional[str] = None
    """URL of the given file.

    This URL can change depending on the domain settings of the account. Will use
    the select file hosting domain.
    """

    width: Optional[int] = None
    """For image and video files, the width of the content."""
