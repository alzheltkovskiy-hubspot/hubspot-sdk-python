# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OptionInputParam"]


class OptionInputParam(TypedDict, total=False):
    hidden: Required[bool]

    label: Required[str]

    value: Required[str]

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]
