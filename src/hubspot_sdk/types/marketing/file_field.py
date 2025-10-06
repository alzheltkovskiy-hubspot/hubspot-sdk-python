# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FileField"]


class FileField(BaseModel):
    allow_multiple_files: bool = FieldInfo(alias="allowMultipleFiles")

    dependent_fields: List["DependentField"] = FieldInfo(alias="dependentFields")

    field_type: Literal["file"] = FieldInfo(alias="fieldType")

    hidden: bool

    label: str

    name: str

    object_type_id: str = FieldInfo(alias="objectTypeId")

    required: bool

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)

    placeholder: Optional[str] = None


from .dependent_field import DependentField
