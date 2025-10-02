# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AutomationActionsPublicConditionalSingleFieldDependency"]


class AutomationActionsPublicConditionalSingleFieldDependency(BaseModel):
    controlling_field_name: str = FieldInfo(alias="controllingFieldName")

    controlling_field_value: str = FieldInfo(alias="controllingFieldValue")

    dependency_type: Literal["CONDITIONAL_SINGLE_FIELD"] = FieldInfo(alias="dependencyType")

    dependent_field_names: List[str] = FieldInfo(alias="dependentFieldNames")
