# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .crm_objects_simple_public_object import CRMObjectsSimplePublicObject

__all__ = ["CRMObjectsCollectionResponseWithTotalSimplePublicObject"]


class CRMObjectsCollectionResponseWithTotalSimplePublicObject(BaseModel):
    results: List[CRMObjectsSimplePublicObject]

    total: int

    paging: Optional[Paging] = None
