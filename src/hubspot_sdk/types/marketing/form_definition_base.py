# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .form_display_options import FormDisplayOptions
from .legal_consent_options_none import LegalConsentOptionsNone
from .hub_spot_form_configuration import HubSpotFormConfiguration
from .legal_consent_options_legitimate_interest import LegalConsentOptionsLegitimateInterest
from .legal_consent_options_explicit_consent_to_process import LegalConsentOptionsExplicitConsentToProcess
from .legal_consent_options_implicit_consent_to_process import LegalConsentOptionsImplicitConsentToProcess

__all__ = ["FormDefinitionBase", "LegalConsentOptions"]

LegalConsentOptions: TypeAlias = Union[
    LegalConsentOptionsNone,
    LegalConsentOptionsLegitimateInterest,
    LegalConsentOptionsExplicitConsentToProcess,
    LegalConsentOptionsImplicitConsentToProcess,
]


class FormDefinitionBase(BaseModel):
    id: str

    archived: bool

    configuration: HubSpotFormConfiguration

    created_at: datetime = FieldInfo(alias="createdAt")

    display_options: FormDisplayOptions = FieldInfo(alias="displayOptions")
    """Options for styling the form."""

    field_groups: List["FieldGroup"] = FieldInfo(alias="fieldGroups")

    form_type: Literal["hubspot"] = FieldInfo(alias="formType")

    legal_consent_options: LegalConsentOptions = FieldInfo(alias="legalConsentOptions")

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)


from .field_group import FieldGroup
