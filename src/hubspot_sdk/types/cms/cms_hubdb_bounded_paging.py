# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .cms_hubdb_bounded_next_page import CmsHubdbBoundedNextPage

__all__ = ["CmsHubdbBoundedPaging"]


class CmsHubdbBoundedPaging(BaseModel):
    next: Optional[CmsHubdbBoundedNextPage] = None
