# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FileUpdateParams"]


class FileUpdateParams(TypedDict, total=False):
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

    clear_expires: Annotated[bool, PropertyInfo(alias="clearExpires")]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAt", format="iso8601")]

    is_usable_in_content: Annotated[bool, PropertyInfo(alias="isUsableInContent")]

    name: str

    parent_folder_id: Annotated[str, PropertyInfo(alias="parentFolderId")]

    parent_folder_path: Annotated[str, PropertyInfo(alias="parentFolderPath")]
