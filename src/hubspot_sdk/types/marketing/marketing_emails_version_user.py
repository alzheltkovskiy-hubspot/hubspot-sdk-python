# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketingEmailsVersionUser"]


class MarketingEmailsVersionUser(BaseModel):
    id: str

    email: str

    full_name: str = FieldInfo(alias="fullName")
