# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketingEmailsPublicEmailFromDetails"]


class MarketingEmailsPublicEmailFromDetails(BaseModel):
    custom_reply_to: Optional[str] = FieldInfo(alias="customReplyTo", default=None)

    from_name: Optional[str] = FieldInfo(alias="fromName", default=None)

    reply_to: Optional[str] = FieldInfo(alias="replyTo", default=None)
