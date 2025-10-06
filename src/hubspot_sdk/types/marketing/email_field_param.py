# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .email_field_validation_param import EmailFieldValidationParam

__all__ = ["EmailFieldParam"]


class EmailFieldParam(TypedDict, total=False):
    dependent_fields: Required[Annotated[Iterable["DependentFieldParam"], PropertyInfo(alias="dependentFields")]]

    field_type: Required[Annotated[Literal["email"], PropertyInfo(alias="fieldType")]]

    hidden: Required[bool]

    label: Required[str]

    name: Required[str]

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    required: Required[bool]

    validation: Required[EmailFieldValidationParam]

    default_value: Annotated[str, PropertyInfo(alias="defaultValue")]

    placeholder: str


from .dependent_field_param import DependentFieldParam
