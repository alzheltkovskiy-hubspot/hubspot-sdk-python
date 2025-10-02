# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .marketing_forms_form_display_options import MarketingFormsFormDisplayOptions
from .marketing_forms_legal_consent_options_none import MarketingFormsLegalConsentOptionsNone
from .marketing_forms_hub_spot_form_configuration import MarketingFormsHubSpotFormConfiguration
from .marketing_forms_legal_consent_options_legitimate_interest import (
    MarketingFormsLegalConsentOptionsLegitimateInterest,
)
from .marketing_forms_legal_consent_options_explicit_consent_to_process import (
    MarketingFormsLegalConsentOptionsExplicitConsentToProcess,
)
from .marketing_forms_legal_consent_options_implicit_consent_to_process import (
    MarketingFormsLegalConsentOptionsImplicitConsentToProcess,
)

__all__ = ["MarketingFormsHubSpotFormDefinition", "LegalConsentOptions"]

LegalConsentOptions: TypeAlias = Union[
    MarketingFormsLegalConsentOptionsNone,
    MarketingFormsLegalConsentOptionsLegitimateInterest,
    MarketingFormsLegalConsentOptionsExplicitConsentToProcess,
    MarketingFormsLegalConsentOptionsImplicitConsentToProcess,
]


class MarketingFormsHubSpotFormDefinition(BaseModel):
    id: str

    archived: bool

    configuration: MarketingFormsHubSpotFormConfiguration

    created_at: datetime = FieldInfo(alias="createdAt")

    display_options: MarketingFormsFormDisplayOptions = FieldInfo(alias="displayOptions")

    field_groups: List["MarketingFormsFieldGroup"] = FieldInfo(alias="fieldGroups")

    form_type: Literal["hubspot"] = FieldInfo(alias="formType")

    legal_consent_options: LegalConsentOptions = FieldInfo(alias="legalConsentOptions")

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)


from .marketing_forms_field_group import MarketingFormsFieldGroup
