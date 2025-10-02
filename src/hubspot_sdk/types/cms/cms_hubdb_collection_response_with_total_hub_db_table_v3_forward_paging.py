# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .cms_hubdb_hub_db_table_v3 import CmsHubdbHubDBTableV3

__all__ = ["CmsHubdbCollectionResponseWithTotalHubDBTableV3ForwardPaging"]


class CmsHubdbCollectionResponseWithTotalHubDBTableV3ForwardPaging(BaseModel):
    results: List[CmsHubdbHubDBTableV3]

    total: int

    paging: Optional[ForwardPaging] = None
