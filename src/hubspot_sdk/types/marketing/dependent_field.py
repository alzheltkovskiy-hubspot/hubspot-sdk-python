# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .dependent_field_filter import DependentFieldFilter

__all__ = ["DependentField"]


class DependentField(BaseModel):
    dependent_condition: DependentFieldFilter = FieldInfo(alias="dependentCondition")

    dependent_field: DependentField = FieldInfo(alias="dependentField")
