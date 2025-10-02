# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .marketing_forms_number_field_validation_param import MarketingFormsNumberFieldValidationParam

__all__ = ["MarketingFormsNumberFieldParam"]


class MarketingFormsNumberFieldParam(TypedDict, total=False):
    dependent_fields: Required[
        Annotated[Iterable["MarketingFormsDependentFieldParam"], PropertyInfo(alias="dependentFields")]
    ]

    field_type: Required[Annotated[Literal["number"], PropertyInfo(alias="fieldType")]]

    hidden: Required[bool]

    label: Required[str]

    name: Required[str]

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    required: Required[bool]

    default_value: Annotated[str, PropertyInfo(alias="defaultValue")]

    placeholder: str

    validation: MarketingFormsNumberFieldValidationParam


from .marketing_forms_dependent_field_param import MarketingFormsDependentFieldParam
