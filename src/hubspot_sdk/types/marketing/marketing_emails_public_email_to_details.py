# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .marketing_emails_public_email_recipients import MarketingEmailsPublicEmailRecipients

__all__ = ["MarketingEmailsPublicEmailToDetails"]


class MarketingEmailsPublicEmailToDetails(BaseModel):
    contact_ids: Optional[MarketingEmailsPublicEmailRecipients] = FieldInfo(alias="contactIds", default=None)

    contact_ils_lists: Optional[MarketingEmailsPublicEmailRecipients] = FieldInfo(alias="contactIlsLists", default=None)

    contact_lists: Optional[MarketingEmailsPublicEmailRecipients] = FieldInfo(alias="contactLists", default=None)

    limit_send_frequency: Optional[bool] = FieldInfo(alias="limitSendFrequency", default=None)

    suppress_graymail: Optional[bool] = FieldInfo(alias="suppressGraymail", default=None)
