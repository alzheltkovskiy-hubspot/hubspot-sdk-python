# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PublicSubscriptionStatus"]


class PublicSubscriptionStatus(BaseModel):
    id: str

    name: str

    source_of_status: Literal["PORTAL_WIDE_STATUS", "BRAND_WIDE_STATUS", "SUBSCRIPTION_STATUS"] = FieldInfo(
        alias="sourceOfStatus"
    )

    status: Literal["SUBSCRIBED", "NOT_SUBSCRIBED"]

    brand_id: Optional[int] = FieldInfo(alias="brandId", default=None)

    legal_basis: Optional[
        Literal[
            "LEGITIMATE_INTEREST_PQL",
            "LEGITIMATE_INTEREST_CLIENT",
            "PERFORMANCE_OF_CONTRACT",
            "CONSENT_WITH_NOTICE",
            "NON_GDPR",
            "PROCESS_AND_STORE",
            "LEGITIMATE_INTEREST_OTHER",
        ]
    ] = FieldInfo(alias="legalBasis", default=None)

    legal_basis_explanation: Optional[str] = FieldInfo(alias="legalBasisExplanation", default=None)

    preference_group_name: Optional[str] = FieldInfo(alias="preferenceGroupName", default=None)
