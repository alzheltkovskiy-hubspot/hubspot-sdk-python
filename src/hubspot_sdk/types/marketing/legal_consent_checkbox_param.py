# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LegalConsentCheckboxParam"]


class LegalConsentCheckboxParam(TypedDict, total=False):
    label: Required[str]
    """The main label for the form field."""

    required: Required[bool]
    """Whether this checkbox is required when submitting the form."""

    subscription_type_id: Required[Annotated[int, PropertyInfo(alias="subscriptionTypeId")]]
