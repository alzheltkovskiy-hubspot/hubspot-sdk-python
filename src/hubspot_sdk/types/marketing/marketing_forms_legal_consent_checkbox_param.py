# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MarketingFormsLegalConsentCheckboxParam"]


class MarketingFormsLegalConsentCheckboxParam(TypedDict, total=False):
    label: Required[str]

    required: Required[bool]

    subscription_type_id: Required[Annotated[int, PropertyInfo(alias="subscriptionTypeId")]]
