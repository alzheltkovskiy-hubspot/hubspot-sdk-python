# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .field_type_definition import FieldTypeDefinition

__all__ = ["InputFieldDefinition"]


class InputFieldDefinition(BaseModel):
    is_required: bool = FieldInfo(alias="isRequired")

    type_definition: FieldTypeDefinition = FieldInfo(alias="typeDefinition")

    automation_field_type: Optional[str] = FieldInfo(alias="automationFieldType", default=None)

    supported_value_types: Optional[
        List[
            Literal[
                "STATIC_VALUE", "OBJECT_PROPERTY", "FIELD_DATA", "FETCHED_OBJECT_PROPERTY", "ENROLLMENT_EVENT_PROPERTY"
            ]
        ]
    ] = FieldInfo(alias="supportedValueTypes", default=None)
