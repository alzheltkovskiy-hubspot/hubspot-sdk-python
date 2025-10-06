# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .field_type_definition_param import FieldTypeDefinitionParam

__all__ = ["InputFieldDefinitionParam"]


class InputFieldDefinitionParam(TypedDict, total=False):
    is_required: Required[Annotated[bool, PropertyInfo(alias="isRequired")]]

    type_definition: Required[Annotated[FieldTypeDefinitionParam, PropertyInfo(alias="typeDefinition")]]

    automation_field_type: Annotated[str, PropertyInfo(alias="automationFieldType")]

    supported_value_types: Annotated[
        List[
            Literal[
                "STATIC_VALUE", "OBJECT_PROPERTY", "FIELD_DATA", "FETCHED_OBJECT_PROPERTY", "ENROLLMENT_EVENT_PROPERTY"
            ]
        ],
        PropertyInfo(alias="supportedValueTypes"),
    ]
