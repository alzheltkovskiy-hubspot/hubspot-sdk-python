# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .marketing_forms_phone_field_validation import MarketingFormsPhoneFieldValidation

__all__ = ["MarketingFormsPhoneField"]


class MarketingFormsPhoneField(BaseModel):
    dependent_fields: List["MarketingFormsDependentField"] = FieldInfo(alias="dependentFields")

    field_type: Literal["phone"] = FieldInfo(alias="fieldType")

    hidden: bool

    label: str

    name: str

    object_type_id: str = FieldInfo(alias="objectTypeId")

    required: bool

    use_country_code_select: bool = FieldInfo(alias="useCountryCodeSelect")

    validation: MarketingFormsPhoneFieldValidation

    default_value: Optional[str] = FieldInfo(alias="defaultValue", default=None)

    placeholder: Optional[str] = None


from .marketing_forms_dependent_field import MarketingFormsDependentField
