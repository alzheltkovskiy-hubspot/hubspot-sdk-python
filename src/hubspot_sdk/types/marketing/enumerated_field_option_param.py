# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EnumeratedFieldOptionParam"]


class EnumeratedFieldOptionParam(TypedDict, total=False):
    display_order: Required[Annotated[int, PropertyInfo(alias="displayOrder")]]
    """The order the choices will be displayed in."""

    label: Required[str]
    """The visible label for this choice."""

    value: Required[str]
    """The value which will be submitted if this choice is selected."""

    description: str
