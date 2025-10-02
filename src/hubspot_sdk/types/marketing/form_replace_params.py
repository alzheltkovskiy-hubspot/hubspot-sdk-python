# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

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

__all__ = ["FormReplaceParams", "LegalConsentOptions"]


class FormReplaceParams(TypedDict, total=False):
    id: Required[str]

    archived: Required[bool]

    configuration: Required[MarketingFormsHubSpotFormConfigurationParam]

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]]

    display_options: Required[Annotated[MarketingFormsFormDisplayOptionsParam, PropertyInfo(alias="displayOptions")]]

    field_groups: Required[Annotated[Iterable["MarketingFormsFieldGroupParam"], PropertyInfo(alias="fieldGroups")]]

    form_type: Required[Annotated[Literal["hubspot"], PropertyInfo(alias="formType")]]

    legal_consent_options: Required[Annotated[LegalConsentOptions, PropertyInfo(alias="legalConsentOptions")]]

    name: Required[str]

    updated_at: Required[Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]]

    archived_at: Annotated[Union[str, datetime], PropertyInfo(alias="archivedAt", format="iso8601")]


LegalConsentOptions: TypeAlias = Union[
    MarketingFormsLegalConsentOptionsNoneParam,
    MarketingFormsLegalConsentOptionsLegitimateInterestParam,
    MarketingFormsLegalConsentOptionsExplicitConsentToProcessParam,
    MarketingFormsLegalConsentOptionsImplicitConsentToProcessParam,
]

from .marketing_forms_field_group_param import MarketingFormsFieldGroupParam
