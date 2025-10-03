# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .marketing_emails_public_email import MarketingEmailsPublicEmail
from .marketing_emails_version_user import MarketingEmailsVersionUser

__all__ = ["MarketingEmailsVersionPublicEmail"]


class MarketingEmailsVersionPublicEmail(BaseModel):
    id: str

    object: MarketingEmailsPublicEmail

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user: MarketingEmailsVersionUser
