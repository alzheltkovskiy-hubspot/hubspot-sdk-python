# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PublicStatus"]


class PublicStatus(BaseModel):
    channel: Literal["EMAIL"]

    source: str

    status: Literal["SUBSCRIBED", "UNSUBSCRIBED", "NOT_SPECIFIED"]

    subscriber_id_string: str = FieldInfo(alias="subscriberIdString")

    subscription_id: int = FieldInfo(alias="subscriptionId")

    timestamp: datetime

    business_unit_id: Optional[int] = FieldInfo(alias="businessUnitId", default=None)

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

    set_status_success_reason: Optional[
        Literal[
            "RESUBSCRIBE_OCCURRED", "NO_STATUS_CHANGE", "UNSUBSCRIBE_FROM_ALL_OCCURRED", "REQUESTED_CHANGE_OCCURRED"
        ]
    ] = FieldInfo(alias="setStatusSuccessReason", default=None)

    subscription_name: Optional[str] = FieldInfo(alias="subscriptionName", default=None)
