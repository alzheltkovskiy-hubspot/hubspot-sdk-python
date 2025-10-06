# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .tag import Tag
from ...._models import BaseModel
from ...shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalTagForwardPaging"]


class CollectionResponseWithTotalTagForwardPaging(BaseModel):
    results: List[Tag]

    total: int

    paging: Optional[ForwardPaging] = None
