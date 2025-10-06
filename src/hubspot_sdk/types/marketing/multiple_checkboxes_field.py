# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .enumerated_field_option import EnumeratedFieldOption

__all__ = ["MultipleCheckboxesField"]


class MultipleCheckboxesField(BaseModel):
    default_values: List[str] = FieldInfo(alias="defaultValues")

    dependent_fields: List["DependentField"] = FieldInfo(alias="dependentFields")

    field_type: Literal["multiple_checkboxes"] = FieldInfo(alias="fieldType")

    hidden: bool

    label: str

    name: str

    object_type_id: str = FieldInfo(alias="objectTypeId")

    options: List[EnumeratedFieldOption]

    required: bool


from .dependent_field import DependentField
