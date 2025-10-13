# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AssociationDefinition"]


class AssociationDefinition(BaseModel):
    id: str
    """A unique ID for this association."""

    from_object_type_id: str = FieldInfo(alias="fromObjectTypeId")
    """ID of the primary object type to link from."""

    to_object_type_id: str = FieldInfo(alias="toObjectTypeId")
    """ID of the target object type to link to."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the association was defined."""

    name: Optional[str] = None
    """A unique name for this association."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the association was last updated."""
