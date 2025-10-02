# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .crm_labels_between_object_pair import CRMLabelsBetweenObjectPair

__all__ = ["CRMCreatedResponseLabelsBetweenObjectPair"]


class CRMCreatedResponseLabelsBetweenObjectPair(BaseModel):
    created_resource_id: str = FieldInfo(alias="createdResourceId")

    entity: CRMLabelsBetweenObjectPair

    location: Optional[str] = None
