# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileImportFromURLParams"]


class FileImportFromURLParams(TypedDict, total=False):
    access: Required[
        Literal[
            "PUBLIC_INDEXABLE",
            "PUBLIC_NOT_INDEXABLE",
            "HIDDEN_INDEXABLE",
            "HIDDEN_NOT_INDEXABLE",
            "HIDDEN_PRIVATE",
            "PRIVATE",
            "HIDDEN_SENSITIVE",
            "SENSITIVE",
        ]
    ]

    url: Required[str]

    duplicate_validation_scope: Annotated[
        Literal["ENTIRE_PORTAL", "EXACT_FOLDER"], PropertyInfo(alias="duplicateValidationScope")
    ]

    duplicate_validation_strategy: Annotated[
        Literal["NONE", "REJECT", "RETURN_EXISTING"], PropertyInfo(alias="duplicateValidationStrategy")
    ]

    expires_at: Annotated[Union[str, datetime], PropertyInfo(alias="expiresAt", format="iso8601")]

    folder_id: Annotated[str, PropertyInfo(alias="folderId")]

    folder_path: Annotated[str, PropertyInfo(alias="folderPath")]

    name: str

    overwrite: bool

    ttl: str
