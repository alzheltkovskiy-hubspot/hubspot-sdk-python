# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .marketing_forms_legal_consent_checkbox import MarketingFormsLegalConsentCheckbox

__all__ = ["MarketingFormsLegalConsentOptionsImplicitConsentToProcess"]


class MarketingFormsLegalConsentOptionsImplicitConsentToProcess(BaseModel):
    communications_checkboxes: List[MarketingFormsLegalConsentCheckbox] = FieldInfo(alias="communicationsCheckboxes")

    privacy_text: str = FieldInfo(alias="privacyText")

    type: Literal["implicit_consent_to_process"]

    communication_consent_text: Optional[str] = FieldInfo(alias="communicationConsentText", default=None)

    consent_to_process_text: Optional[str] = FieldInfo(alias="consentToProcessText", default=None)
