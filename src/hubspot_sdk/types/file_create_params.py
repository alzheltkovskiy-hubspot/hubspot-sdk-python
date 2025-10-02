# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    name: Required[str]

    parent_folder_id: Annotated[str, PropertyInfo(alias="parentFolderId")]

    parent_path: Annotated[str, PropertyInfo(alias="parentPath")]
