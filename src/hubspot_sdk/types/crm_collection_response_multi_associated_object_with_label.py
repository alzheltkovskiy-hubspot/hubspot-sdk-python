# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.paging import Paging
from .crm_multi_associated_object_with_label import CRMMultiAssociatedObjectWithLabel

__all__ = ["CRMCollectionResponseMultiAssociatedObjectWithLabel"]


class CRMCollectionResponseMultiAssociatedObjectWithLabel(BaseModel):
    results: List[CRMMultiAssociatedObjectWithLabel]

    paging: Optional[Paging] = None
