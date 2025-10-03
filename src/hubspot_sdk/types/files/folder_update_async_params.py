# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FolderUpdateAsyncParams"]


class FolderUpdateAsyncParams(TypedDict, total=False):
    id: Required[str]

    name: str

    parent_folder_id: Annotated[int, PropertyInfo(alias="parentFolderId")]
