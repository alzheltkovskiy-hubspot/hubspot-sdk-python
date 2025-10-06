# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CallingUpdateParams"]


class CallingUpdateParams(TypedDict, total=False):
    is_ready: Annotated[bool, PropertyInfo(alias="isReady")]

    url: str
