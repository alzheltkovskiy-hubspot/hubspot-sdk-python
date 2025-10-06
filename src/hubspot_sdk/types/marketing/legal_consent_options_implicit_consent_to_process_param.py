# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .legal_consent_checkbox_param import LegalConsentCheckboxParam

__all__ = ["LegalConsentOptionsImplicitConsentToProcessParam"]


class LegalConsentOptionsImplicitConsentToProcessParam(TypedDict, total=False):
    communications_checkboxes: Required[
        Annotated[Iterable[LegalConsentCheckboxParam], PropertyInfo(alias="communicationsCheckboxes")]
    ]

    privacy_text: Required[Annotated[str, PropertyInfo(alias="privacyText")]]

    type: Required[Literal["implicit_consent_to_process"]]

    communication_consent_text: Annotated[str, PropertyInfo(alias="communicationConsentText")]

    consent_to_process_text: Annotated[str, PropertyInfo(alias="consentToProcessText")]
