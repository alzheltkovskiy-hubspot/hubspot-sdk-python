# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..marketing_subscriptions_subscription_definition import MarketingSubscriptionsSubscriptionDefinition

__all__ = ["MarketingSubscriptionsV3SubscriptionDefinitionsResponse"]


class MarketingSubscriptionsV3SubscriptionDefinitionsResponse(BaseModel):
    subscription_definitions: List[MarketingSubscriptionsSubscriptionDefinition] = FieldInfo(
        alias="subscriptionDefinitions"
    )
