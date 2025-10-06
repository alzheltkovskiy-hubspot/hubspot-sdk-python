# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .object_type_definition_labels import ObjectTypeDefinitionLabels

__all__ = ["ObjectTypeDefinition"]


class ObjectTypeDefinition(BaseModel):
    id: str

    labels: ObjectTypeDefinitionLabels

    name: str

    required_properties: List[str] = FieldInfo(alias="requiredProperties")

    archived: Optional[bool] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    fully_qualified_name: Optional[str] = FieldInfo(alias="fullyQualifiedName", default=None)

    object_type_id: Optional[str] = FieldInfo(alias="objectTypeId", default=None)

    portal_id: Optional[int] = FieldInfo(alias="portalId", default=None)

    primary_display_property: Optional[str] = FieldInfo(alias="primaryDisplayProperty", default=None)

    searchable_properties: Optional[List[str]] = FieldInfo(alias="searchableProperties", default=None)

    secondary_display_properties: Optional[List[str]] = FieldInfo(alias="secondaryDisplayProperties", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
