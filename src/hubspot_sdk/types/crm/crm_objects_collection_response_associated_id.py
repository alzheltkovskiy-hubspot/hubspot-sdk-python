# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.paging import Paging
from ..crm_associated_id import CRMAssociatedID

__all__ = ["CRMObjectsCollectionResponseAssociatedID"]


class CRMObjectsCollectionResponseAssociatedID(BaseModel):
    results: List[CRMAssociatedID]

    paging: Optional[Paging] = None
