# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .automation_actions_field_type_definition import AutomationActionsFieldTypeDefinition

__all__ = ["AutomationActionsInputFieldDefinition"]


class AutomationActionsInputFieldDefinition(BaseModel):
    is_required: bool = FieldInfo(alias="isRequired")

    type_definition: AutomationActionsFieldTypeDefinition = FieldInfo(alias="typeDefinition")

    automation_field_type: Optional[str] = FieldInfo(alias="automationFieldType", default=None)

    supported_value_types: Optional[
        List[
            Literal[
                "STATIC_VALUE", "OBJECT_PROPERTY", "FIELD_DATA", "FETCHED_OBJECT_PROPERTY", "ENROLLMENT_EVENT_PROPERTY"
            ]
        ]
    ] = FieldInfo(alias="supportedValueTypes", default=None)
