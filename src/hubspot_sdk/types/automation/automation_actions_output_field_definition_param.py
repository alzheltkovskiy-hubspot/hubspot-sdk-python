# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .automation_actions_field_type_definition_param import AutomationActionsFieldTypeDefinitionParam

__all__ = ["AutomationActionsOutputFieldDefinitionParam"]


class AutomationActionsOutputFieldDefinitionParam(TypedDict, total=False):
    type_definition: Required[
        Annotated[AutomationActionsFieldTypeDefinitionParam, PropertyInfo(alias="typeDefinition")]
    ]
