# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .marketing_subscriptions_v3_public_subscription_status import MarketingSubscriptionsV3PublicSubscriptionStatus

__all__ = ["MarketingSubscriptionsV3PublicSubscriptionStatusesResponse"]


class MarketingSubscriptionsV3PublicSubscriptionStatusesResponse(BaseModel):
    recipient: str

    subscription_statuses: List[MarketingSubscriptionsV3PublicSubscriptionStatus] = FieldInfo(
        alias="subscriptionStatuses"
    )
