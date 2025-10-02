# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .automation_actions_public_action_labels_param import AutomationActionsPublicActionLabelsParam
from .automation_actions_input_field_definition_param import AutomationActionsInputFieldDefinitionParam
from .automation_actions_output_field_definition_param import AutomationActionsOutputFieldDefinitionParam
from .automation_actions_public_object_request_options_param import AutomationActionsPublicObjectRequestOptionsParam
from .automation_actions_public_single_field_dependency_param import AutomationActionsPublicSingleFieldDependencyParam
from .automation_actions_public_execution_translation_rule_param import (
    AutomationActionsPublicExecutionTranslationRuleParam,
)
from .automation_actions_public_conditional_single_field_dependency_param import (
    AutomationActionsPublicConditionalSingleFieldDependencyParam,
)

__all__ = ["ActionUpdateParams", "InputFieldDependency"]


class ActionUpdateParams(TypedDict, total=False):
    app_id: Required[Annotated[int, PropertyInfo(alias="appId")]]

    action_url: Annotated[str, PropertyInfo(alias="actionUrl")]

    execution_rules: Annotated[
        Iterable[AutomationActionsPublicExecutionTranslationRuleParam], PropertyInfo(alias="executionRules")
    ]

    input_field_dependencies: Annotated[Iterable[InputFieldDependency], PropertyInfo(alias="inputFieldDependencies")]

    input_fields: Annotated[Iterable[AutomationActionsInputFieldDefinitionParam], PropertyInfo(alias="inputFields")]

    labels: Dict[str, AutomationActionsPublicActionLabelsParam]

    object_request_options: Annotated[
        AutomationActionsPublicObjectRequestOptionsParam, PropertyInfo(alias="objectRequestOptions")
    ]

    object_types: Annotated[SequenceNotStr[str], PropertyInfo(alias="objectTypes")]

    output_fields: Annotated[Iterable[AutomationActionsOutputFieldDefinitionParam], PropertyInfo(alias="outputFields")]

    published: bool


InputFieldDependency: TypeAlias = Union[
    AutomationActionsPublicSingleFieldDependencyParam, AutomationActionsPublicConditionalSingleFieldDependencyParam
]
