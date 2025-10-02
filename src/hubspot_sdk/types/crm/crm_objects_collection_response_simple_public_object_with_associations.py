# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from .crm_objects_simple_public_object_with_associations import CRMObjectsSimplePublicObjectWithAssociations

__all__ = ["CRMObjectsCollectionResponseSimplePublicObjectWithAssociations"]


class CRMObjectsCollectionResponseSimplePublicObjectWithAssociations(BaseModel):
    results: List[CRMObjectsSimplePublicObjectWithAssociations]

    paging: Optional[Paging] = None
