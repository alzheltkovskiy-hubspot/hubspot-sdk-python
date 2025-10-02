# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .webhooks_subscription_batch_update_request_param import WebhooksSubscriptionBatchUpdateRequestParam

__all__ = ["WebhookUpdateBatchParams"]


class WebhookUpdateBatchParams(TypedDict, total=False):
    inputs: Required[Iterable[WebhooksSubscriptionBatchUpdateRequestParam]]
