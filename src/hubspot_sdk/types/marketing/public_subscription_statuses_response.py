# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_subscription_status import PublicSubscriptionStatus

__all__ = ["PublicSubscriptionStatusesResponse"]


class PublicSubscriptionStatusesResponse(BaseModel):
    recipient: str
    """Email address of the contact."""

    subscription_statuses: List[PublicSubscriptionStatus] = FieldInfo(alias="subscriptionStatuses")
    """A list of all of the contact's subscriptions statuses."""
