# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .automation_actions_field_type_definition import AutomationActionsFieldTypeDefinition

__all__ = ["AutomationActionsOutputFieldDefinition"]


class AutomationActionsOutputFieldDefinition(BaseModel):
    type_definition: AutomationActionsFieldTypeDefinition = FieldInfo(alias="typeDefinition")
