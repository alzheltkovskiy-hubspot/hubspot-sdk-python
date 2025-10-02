# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketingFormsLegalConsentOptionsLegitimateInterest"]


class MarketingFormsLegalConsentOptionsLegitimateInterest(BaseModel):
    lawful_basis: Literal["lead", "client", "other"] = FieldInfo(alias="lawfulBasis")

    privacy_text: str = FieldInfo(alias="privacyText")

    subscription_type_ids: List[int] = FieldInfo(alias="subscriptionTypeIds")

    type: Literal["legitimate_interest"]
