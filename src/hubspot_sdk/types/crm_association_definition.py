# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CRMAssociationDefinition"]


class CRMAssociationDefinition(BaseModel):
    id: str

    from_object_type_id: str = FieldInfo(alias="fromObjectTypeId")

    to_object_type_id: str = FieldInfo(alias="toObjectTypeId")

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    name: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
