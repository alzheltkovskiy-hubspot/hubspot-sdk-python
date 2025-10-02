# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .cms_blogs_tags_tag import CmsBlogsTagsTag
from ...shared.forward_paging import ForwardPaging

__all__ = ["CmsBlogsTagsCollectionResponseWithTotalTagForwardPaging"]


class CmsBlogsTagsCollectionResponseWithTotalTagForwardPaging(BaseModel):
    results: List[CmsBlogsTagsTag]

    total: int

    paging: Optional[ForwardPaging] = None
