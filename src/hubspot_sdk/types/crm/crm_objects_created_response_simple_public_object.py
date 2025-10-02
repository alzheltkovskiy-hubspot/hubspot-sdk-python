# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .crm_objects_simple_public_object import CRMObjectsSimplePublicObject

__all__ = ["CRMObjectsCreatedResponseSimplePublicObject"]


class CRMObjectsCreatedResponseSimplePublicObject(BaseModel):
    created_resource_id: str = FieldInfo(alias="createdResourceId")

    entity: CRMObjectsSimplePublicObject

    location: Optional[str] = None
