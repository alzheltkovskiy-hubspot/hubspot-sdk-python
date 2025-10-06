# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .domain import Domain
from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalDomainForwardPaging"]


class CollectionResponseWithTotalDomainForwardPaging(BaseModel):
    results: List[Domain]

    total: int

    paging: Optional[ForwardPaging] = None
