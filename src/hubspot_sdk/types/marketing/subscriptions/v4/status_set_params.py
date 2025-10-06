# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["StatusSetParams"]


class StatusSetParams(TypedDict, total=False):
    channel: Required[Literal["EMAIL"]]

    status_state: Required[
        Annotated[Literal["SUBSCRIBED", "UNSUBSCRIBED", "NOT_SPECIFIED"], PropertyInfo(alias="statusState")]
    ]

    subscription_id: Required[Annotated[int, PropertyInfo(alias="subscriptionId")]]

    legal_basis: Annotated[
        Literal[
            "LEGITIMATE_INTEREST_PQL",
            "LEGITIMATE_INTEREST_CLIENT",
            "PERFORMANCE_OF_CONTRACT",
            "CONSENT_WITH_NOTICE",
            "NON_GDPR",
            "PROCESS_AND_STORE",
            "LEGITIMATE_INTEREST_OTHER",
        ],
        PropertyInfo(alias="legalBasis"),
    ]

    legal_basis_explanation: Annotated[str, PropertyInfo(alias="legalBasisExplanation")]
