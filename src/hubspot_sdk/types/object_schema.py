# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .property import Property
from .association_definition import AssociationDefinition
from .object_type_definition_labels import ObjectTypeDefinitionLabels

__all__ = ["ObjectSchema"]


class ObjectSchema(BaseModel):
    id: str

    associations: List[AssociationDefinition]

    labels: ObjectTypeDefinitionLabels

    name: str

    properties: List[Property]

    required_properties: List[str] = FieldInfo(alias="requiredProperties")

    archived: Optional[bool] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by_user_id: Optional[int] = FieldInfo(alias="createdByUserId", default=None)

    fully_qualified_name: Optional[str] = FieldInfo(alias="fullyQualifiedName", default=None)

    object_type_id: Optional[str] = FieldInfo(alias="objectTypeId", default=None)

    primary_display_property: Optional[str] = FieldInfo(alias="primaryDisplayProperty", default=None)

    searchable_properties: Optional[List[str]] = FieldInfo(alias="searchableProperties", default=None)

    secondary_display_properties: Optional[List[str]] = FieldInfo(alias="secondaryDisplayProperties", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    updated_by_user_id: Optional[int] = FieldInfo(alias="updatedByUserId", default=None)
