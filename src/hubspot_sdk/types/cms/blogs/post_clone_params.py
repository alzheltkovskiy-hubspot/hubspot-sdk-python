# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PostCloneParams"]


class PostCloneParams(TypedDict, total=False):
    id: Required[str]

    clone_name: Annotated[str, PropertyInfo(alias="cloneName")]
