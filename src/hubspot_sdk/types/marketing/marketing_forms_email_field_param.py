# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .marketing_forms_email_field_validation_param import MarketingFormsEmailFieldValidationParam

__all__ = ["MarketingFormsEmailFieldParam"]


class MarketingFormsEmailFieldParam(TypedDict, total=False):
    dependent_fields: Required[
        Annotated[Iterable["MarketingFormsDependentFieldParam"], PropertyInfo(alias="dependentFields")]
    ]

    field_type: Required[Annotated[Literal["email"], PropertyInfo(alias="fieldType")]]

    hidden: Required[bool]

    label: Required[str]

    name: Required[str]

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    required: Required[bool]

    validation: Required[MarketingFormsEmailFieldValidationParam]

    default_value: Annotated[str, PropertyInfo(alias="defaultValue")]

    placeholder: str


from .marketing_forms_dependent_field_param import MarketingFormsDependentFieldParam
