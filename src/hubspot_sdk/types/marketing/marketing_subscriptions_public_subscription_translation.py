# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketingSubscriptionsPublicSubscriptionTranslation"]


class MarketingSubscriptionsPublicSubscriptionTranslation(BaseModel):
    created_at: int = FieldInfo(alias="createdAt")

    language_code: str = FieldInfo(alias="languageCode")

    name: str

    subscription_id: int = FieldInfo(alias="subscriptionId")

    updated_at: int = FieldInfo(alias="updatedAt")
