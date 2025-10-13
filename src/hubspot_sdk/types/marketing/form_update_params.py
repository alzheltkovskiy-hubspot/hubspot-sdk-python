# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .form_display_options_param import FormDisplayOptionsParam
from .legal_consent_options_none_param import LegalConsentOptionsNoneParam
from .hub_spot_form_configuration_param import HubSpotFormConfigurationParam
from .legal_consent_options_legitimate_interest_param import LegalConsentOptionsLegitimateInterestParam
from .legal_consent_options_explicit_consent_to_process_param import LegalConsentOptionsExplicitConsentToProcessParam
from .legal_consent_options_implicit_consent_to_process_param import LegalConsentOptionsImplicitConsentToProcessParam

__all__ = ["FormUpdateParams", "LegalConsentOptions"]


class FormUpdateParams(TypedDict, total=False):
    archived: bool
    """Whether this form is archived."""

    configuration: HubSpotFormConfigurationParam

    display_options: Annotated[FormDisplayOptionsParam, PropertyInfo(alias="displayOptions")]
    """Options for styling the form."""

    field_groups: Annotated[Iterable["FieldGroupParam"], PropertyInfo(alias="fieldGroups")]
    """The fields in the form, grouped in rows."""

    legal_consent_options: Annotated[LegalConsentOptions, PropertyInfo(alias="legalConsentOptions")]

    name: str
    """The name of the form. Expected to be unique for a hub."""


LegalConsentOptions: TypeAlias = Union[
    LegalConsentOptionsNoneParam,
    LegalConsentOptionsLegitimateInterestParam,
    LegalConsentOptionsExplicitConsentToProcessParam,
    LegalConsentOptionsImplicitConsentToProcessParam,
]

from .field_group_param import FieldGroupParam
