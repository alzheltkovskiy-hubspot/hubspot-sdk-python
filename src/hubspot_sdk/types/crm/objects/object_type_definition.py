# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .object_type_definition_labels import ObjectTypeDefinitionLabels

__all__ = ["ObjectTypeDefinition"]


class ObjectTypeDefinition(BaseModel):
    id: str
    """A unique ID for this object type. Will be defined as {meta-type}-{unique ID}."""

    labels: ObjectTypeDefinitionLabels
    """Singular and plural labels for the object. Used in CRM display."""

    name: str
    """A unique name for this object. For internal use only."""

    required_properties: List[str] = FieldInfo(alias="requiredProperties")
    """
    The names of properties that should be **required** when creating an object of
    this type.
    """

    archived: Optional[bool] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the object type was created."""

    description: Optional[str] = None

    fully_qualified_name: Optional[str] = FieldInfo(alias="fullyQualifiedName", default=None)

    object_type_id: Optional[str] = FieldInfo(alias="objectTypeId", default=None)

    portal_id: Optional[int] = FieldInfo(alias="portalId", default=None)
    """The ID of the account that this object type is specific to."""

    primary_display_property: Optional[str] = FieldInfo(alias="primaryDisplayProperty", default=None)
    """The name of the primary property for this object.

    This will be displayed as primary on the HubSpot record page for this object
    type.
    """

    searchable_properties: Optional[List[str]] = FieldInfo(alias="searchableProperties", default=None)
    """
    Names of properties that will be indexed for this object type in by HubSpot's
    product search.
    """

    secondary_display_properties: Optional[List[str]] = FieldInfo(alias="secondaryDisplayProperties", default=None)
    """The names of secondary properties for this object.

    These will be displayed as secondary on the HubSpot record page for this object
    type.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the object type was last updated."""
