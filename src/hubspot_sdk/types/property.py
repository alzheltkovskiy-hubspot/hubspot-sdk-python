# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .option import Option
from .._models import BaseModel
from .property_modification_metadata import PropertyModificationMetadata

__all__ = ["Property"]


class Property(BaseModel):
    field_type: str = FieldInfo(alias="fieldType")

    group_name: str = FieldInfo(alias="groupName")

    label: str

    name: str

    options: List[Option]

    type: str

    archived: Optional[bool] = None

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)

    calculated: Optional[bool] = None

    calculation_formula: Optional[str] = FieldInfo(alias="calculationFormula", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_user_id: Optional[str] = FieldInfo(alias="createdUserId", default=None)

    data_sensitivity: Optional[Literal["non_sensitive", "sensitive", "highly_sensitive"]] = FieldInfo(
        alias="dataSensitivity", default=None
    )

    display_order: Optional[int] = FieldInfo(alias="displayOrder", default=None)

    external_options: Optional[bool] = FieldInfo(alias="externalOptions", default=None)

    form_field: Optional[bool] = FieldInfo(alias="formField", default=None)

    has_unique_value: Optional[bool] = FieldInfo(alias="hasUniqueValue", default=None)

    hidden: Optional[bool] = None

    hubspot_defined: Optional[bool] = FieldInfo(alias="hubspotDefined", default=None)

    modification_metadata: Optional[PropertyModificationMetadata] = FieldInfo(
        alias="modificationMetadata", default=None
    )

    referenced_object_type: Optional[str] = FieldInfo(alias="referencedObjectType", default=None)

    sensitive_data_categories: Optional[List[str]] = FieldInfo(alias="sensitiveDataCategories", default=None)

    show_currency_symbol: Optional[bool] = FieldInfo(alias="showCurrencySymbol", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    updated_user_id: Optional[str] = FieldInfo(alias="updatedUserId", default=None)
