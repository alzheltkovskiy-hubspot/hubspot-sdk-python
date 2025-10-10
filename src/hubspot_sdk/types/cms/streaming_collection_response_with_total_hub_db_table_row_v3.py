# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..marketing.marketing_emails_paging import MarketingEmailsPaging

__all__ = ["StreamingCollectionResponseWithTotalHubDBTableRowV3"]


class StreamingCollectionResponseWithTotalHubDBTableRowV3(BaseModel):
    results: List[object]

    total: int

    type: Literal["STREAMING"]

    paging: Optional[MarketingEmailsPaging] = None
