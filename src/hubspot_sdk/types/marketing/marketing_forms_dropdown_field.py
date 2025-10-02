# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .marketing_forms_enumerated_field_option import MarketingFormsEnumeratedFieldOption

__all__ = ["MarketingFormsDropdownField"]


class MarketingFormsDropdownField(BaseModel):
    default_values: List[str] = FieldInfo(alias="defaultValues")

    dependent_fields: List["MarketingFormsDependentField"] = FieldInfo(alias="dependentFields")

    field_type: Literal["dropdown"] = FieldInfo(alias="fieldType")

    hidden: bool

    label: str

    name: str

    object_type_id: str = FieldInfo(alias="objectTypeId")

    options: List[MarketingFormsEnumeratedFieldOption]

    required: bool

    placeholder: Optional[str] = None


from .marketing_forms_dependent_field import MarketingFormsDependentField
