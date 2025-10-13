# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ChannelConnectionSettingsResponse"]


class ChannelConnectionSettingsResponse(BaseModel):
    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp this setting was created"""

    is_ready: bool = FieldInfo(alias="isReady")
    """If true, this app will be considered to support channel connection"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The timestamp this setting was last updated"""

    url: str
    """The URL to fetch phone numbers available for channel connection"""
