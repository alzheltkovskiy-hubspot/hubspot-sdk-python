# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebhooksThrottlingSettings"]


class WebhooksThrottlingSettings(BaseModel):
    max_concurrent_requests: int = FieldInfo(alias="maxConcurrentRequests")
