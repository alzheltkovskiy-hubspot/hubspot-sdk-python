# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .marketing_forms_form_display_options_param import MarketingFormsFormDisplayOptionsParam
from .marketing_forms_legal_consent_options_none_param import MarketingFormsLegalConsentOptionsNoneParam
from .marketing_forms_hub_spot_form_configuration_param import MarketingFormsHubSpotFormConfigurationParam
from .marketing_forms_legal_consent_options_legitimate_interest_param import (
    MarketingFormsLegalConsentOptionsLegitimateInterestParam,
)
from .marketing_forms_legal_consent_options_explicit_consent_to_process_param import (
    MarketingFormsLegalConsentOptionsExplicitConsentToProcessParam,
)
from .marketing_forms_legal_consent_options_implicit_consent_to_process_param import (
    MarketingFormsLegalConsentOptionsImplicitConsentToProcessParam,
)

__all__ = ["FormUpdateParams", "LegalConsentOptions"]


class FormUpdateParams(TypedDict, total=False):
    archived: bool

    configuration: MarketingFormsHubSpotFormConfigurationParam

    display_options: Annotated[MarketingFormsFormDisplayOptionsParam, PropertyInfo(alias="displayOptions")]

    field_groups: Annotated[Iterable["MarketingFormsFieldGroupParam"], PropertyInfo(alias="fieldGroups")]

    legal_consent_options: Annotated[LegalConsentOptions, PropertyInfo(alias="legalConsentOptions")]

    name: str


LegalConsentOptions: TypeAlias = Union[
    MarketingFormsLegalConsentOptionsNoneParam,
    MarketingFormsLegalConsentOptionsLegitimateInterestParam,
    MarketingFormsLegalConsentOptionsExplicitConsentToProcessParam,
    MarketingFormsLegalConsentOptionsImplicitConsentToProcessParam,
]

from .marketing_forms_field_group_param import MarketingFormsFieldGroupParam
