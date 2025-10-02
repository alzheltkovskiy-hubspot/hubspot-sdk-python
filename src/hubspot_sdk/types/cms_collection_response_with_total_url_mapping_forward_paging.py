# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .cms_url_mapping import CmsURLMapping
from .shared.forward_paging import ForwardPaging

__all__ = ["CmsCollectionResponseWithTotalURLMappingForwardPaging"]


class CmsCollectionResponseWithTotalURLMappingForwardPaging(BaseModel):
    results: List[CmsURLMapping]

    total: int

    paging: Optional[ForwardPaging] = None
