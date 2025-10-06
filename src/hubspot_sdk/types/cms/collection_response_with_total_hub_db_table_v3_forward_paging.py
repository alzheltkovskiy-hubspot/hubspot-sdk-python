# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .hub_db_table_v3 import HubDBTableV3
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseWithTotalHubDBTableV3ForwardPaging"]


class CollectionResponseWithTotalHubDBTableV3ForwardPaging(BaseModel):
    results: List[HubDBTableV3]

    total: int

    paging: Optional[ForwardPaging] = None
