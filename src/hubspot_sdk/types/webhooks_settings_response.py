# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .throttling_settings import ThrottlingSettings

__all__ = ["WebhooksSettingsResponse"]


class WebhooksSettingsResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")

    target_url: str = FieldInfo(alias="targetUrl")

    throttling: ThrottlingSettings

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
