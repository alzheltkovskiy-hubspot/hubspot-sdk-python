# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .cms_hubdb_bounded_paging import CmsHubdbBoundedPaging

__all__ = ["CmsHubdbRandomAccessCollectionResponseWithTotalHubDBTableRowV3"]


class CmsHubdbRandomAccessCollectionResponseWithTotalHubDBTableRowV3(BaseModel):
    results: List[object]

    total: int

    type: Literal["RANDOM_ACCESS"]

    paging: Optional[CmsHubdbBoundedPaging] = None
