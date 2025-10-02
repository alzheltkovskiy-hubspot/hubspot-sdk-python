# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .crm_properties_property_group import CRMPropertiesPropertyGroup

__all__ = ["CRMPropertiesCreatedResponsePropertyGroup"]


class CRMPropertiesCreatedResponsePropertyGroup(BaseModel):
    created_resource_id: str = FieldInfo(alias="createdResourceId")

    entity: CRMPropertiesPropertyGroup

    location: Optional[str] = None
