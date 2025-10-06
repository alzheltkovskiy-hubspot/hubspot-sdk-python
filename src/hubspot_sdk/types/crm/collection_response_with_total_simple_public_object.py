# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..marketing.paging import Paging
from .simple_public_object import SimplePublicObject

__all__ = ["CollectionResponseWithTotalSimplePublicObject"]


class CollectionResponseWithTotalSimplePublicObject(BaseModel):
    results: List[SimplePublicObject]

    total: int

    paging: Optional[Paging] = None
