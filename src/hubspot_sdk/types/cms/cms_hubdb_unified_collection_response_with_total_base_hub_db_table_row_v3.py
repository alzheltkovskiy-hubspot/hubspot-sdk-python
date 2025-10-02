# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .cms_hubdb_streaming_collection_response_with_total_hub_db_table_row_v3 import (
    CmsHubdbStreamingCollectionResponseWithTotalHubDBTableRowV3,
)
from .cms_hubdb_random_access_collection_response_with_total_hub_db_table_row_v3 import (
    CmsHubdbRandomAccessCollectionResponseWithTotalHubDBTableRowV3,
)

__all__ = ["CmsHubdbUnifiedCollectionResponseWithTotalBaseHubDBTableRowV3"]

CmsHubdbUnifiedCollectionResponseWithTotalBaseHubDBTableRowV3: TypeAlias = Union[
    CmsHubdbRandomAccessCollectionResponseWithTotalHubDBTableRowV3,
    CmsHubdbStreamingCollectionResponseWithTotalHubDBTableRowV3,
]
