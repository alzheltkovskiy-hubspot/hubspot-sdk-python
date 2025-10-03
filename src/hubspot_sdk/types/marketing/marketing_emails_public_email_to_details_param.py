# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .marketing_emails_public_email_recipients_param import MarketingEmailsPublicEmailRecipientsParam

__all__ = ["MarketingEmailsPublicEmailToDetailsParam"]


class MarketingEmailsPublicEmailToDetailsParam(TypedDict, total=False):
    contact_ids: Annotated[MarketingEmailsPublicEmailRecipientsParam, PropertyInfo(alias="contactIds")]

    contact_ils_lists: Annotated[MarketingEmailsPublicEmailRecipientsParam, PropertyInfo(alias="contactIlsLists")]

    contact_lists: Annotated[MarketingEmailsPublicEmailRecipientsParam, PropertyInfo(alias="contactLists")]

    limit_send_frequency: Annotated[bool, PropertyInfo(alias="limitSendFrequency")]

    suppress_graymail: Annotated[bool, PropertyInfo(alias="suppressGraymail")]
