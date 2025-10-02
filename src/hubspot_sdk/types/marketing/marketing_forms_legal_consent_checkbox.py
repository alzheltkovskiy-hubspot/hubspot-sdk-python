# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketingFormsLegalConsentCheckbox"]


class MarketingFormsLegalConsentCheckbox(BaseModel):
    label: str

    required: bool

    subscription_type_id: int = FieldInfo(alias="subscriptionTypeId")
