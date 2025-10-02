# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.paging import Paging

__all__ = ["CmsHubdbStreamingCollectionResponseWithTotalHubDBTableRowV3"]


class CmsHubdbStreamingCollectionResponseWithTotalHubDBTableRowV3(BaseModel):
    results: List[object]

    total: int

    type: Literal["STREAMING"]

    paging: Optional[Paging] = None
