# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .property_group import PropertyGroup

__all__ = ["CreatedResponsePropertyGroup"]


class CreatedResponsePropertyGroup(BaseModel):
    created_resource_id: str = FieldInfo(alias="createdResourceId")

    entity: PropertyGroup

    location: Optional[str] = None
