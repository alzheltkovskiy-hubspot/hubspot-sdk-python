# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .legal_consent_checkbox import LegalConsentCheckbox

__all__ = ["LegalConsentOptionsExplicitConsentToProcess"]


class LegalConsentOptionsExplicitConsentToProcess(BaseModel):
    communications_checkboxes: List[LegalConsentCheckbox] = FieldInfo(alias="communicationsCheckboxes")

    privacy_text: str = FieldInfo(alias="privacyText")

    type: Literal["explicit_consent_to_process"]

    communication_consent_text: Optional[str] = FieldInfo(alias="communicationConsentText", default=None)

    consent_to_process_checkbox_label: Optional[str] = FieldInfo(alias="consentToProcessCheckboxLabel", default=None)

    consent_to_process_footer_text: Optional[str] = FieldInfo(alias="consentToProcessFooterText", default=None)

    consent_to_process_text: Optional[str] = FieldInfo(alias="consentToProcessText", default=None)
