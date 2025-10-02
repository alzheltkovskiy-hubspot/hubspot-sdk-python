# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .automation_actions_public_action_labels import AutomationActionsPublicActionLabels
from .automation_actions_input_field_definition import AutomationActionsInputFieldDefinition
from .automation_actions_output_field_definition import AutomationActionsOutputFieldDefinition
from .automation_actions_public_object_request_options import AutomationActionsPublicObjectRequestOptions
from .automation_actions_public_single_field_dependency import AutomationActionsPublicSingleFieldDependency
from .automation_actions_public_action_function_identifier import AutomationActionsPublicActionFunctionIdentifier
from .automation_actions_public_execution_translation_rule import AutomationActionsPublicExecutionTranslationRule
from .automation_actions_public_conditional_single_field_dependency import (
    AutomationActionsPublicConditionalSingleFieldDependency,
)

__all__ = ["AutomationActionsPublicActionDefinition", "InputFieldDependency"]

InputFieldDependency: TypeAlias = Union[
    AutomationActionsPublicSingleFieldDependency, AutomationActionsPublicConditionalSingleFieldDependency
]


class AutomationActionsPublicActionDefinition(BaseModel):
    id: str

    action_url: str = FieldInfo(alias="actionUrl")

    functions: List[AutomationActionsPublicActionFunctionIdentifier]

    input_fields: List[AutomationActionsInputFieldDefinition] = FieldInfo(alias="inputFields")

    labels: Dict[str, AutomationActionsPublicActionLabels]

    object_types: List[str] = FieldInfo(alias="objectTypes")

    published: bool

    revision_id: str = FieldInfo(alias="revisionId")

    archived_at: Optional[int] = FieldInfo(alias="archivedAt", default=None)

    execution_rules: Optional[List[AutomationActionsPublicExecutionTranslationRule]] = FieldInfo(
        alias="executionRules", default=None
    )

    input_field_dependencies: Optional[List[InputFieldDependency]] = FieldInfo(
        alias="inputFieldDependencies", default=None
    )

    object_request_options: Optional[AutomationActionsPublicObjectRequestOptions] = FieldInfo(
        alias="objectRequestOptions", default=None
    )

    output_fields: Optional[List[AutomationActionsOutputFieldDefinition]] = FieldInfo(
        alias="outputFields", default=None
    )
