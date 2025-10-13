# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OptionInputParam"]


class OptionInputParam(TypedDict, total=False):
    hidden: Required[bool]
    """
    If true, the option will not be shown in forms, bots, or meeting scheduling
    pages. Supported for contact, company, ticket, and custom object enumeration
    properties.
    """

    label: Required[str]
    """A human-readable option label that will be shown in HubSpot."""

    value: Required[str]
    """
    The internal value of the option, which must be used when setting the property
    value through the API.
    """

    description: str
    """A description of the option."""

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]
    """Options are shown in order starting with the lowest positive integer value.

    Values of -1 will cause the option to be displayed after any positive values.
    """
