# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MarketingEmailsPublicEmailSubscriptionDetailsParam"]


class MarketingEmailsPublicEmailSubscriptionDetailsParam(TypedDict, total=False):
    office_location_id: Annotated[str, PropertyInfo(alias="officeLocationId")]

    preferences_group_id: Annotated[str, PropertyInfo(alias="preferencesGroupId")]

    subscription_id: Annotated[str, PropertyInfo(alias="subscriptionId")]
