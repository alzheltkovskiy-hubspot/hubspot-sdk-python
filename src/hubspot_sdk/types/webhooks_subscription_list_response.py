# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .webhooks_subscription_response import WebhooksSubscriptionResponse

__all__ = ["WebhooksSubscriptionListResponse"]


class WebhooksSubscriptionListResponse(BaseModel):
    results: List[WebhooksSubscriptionResponse]
