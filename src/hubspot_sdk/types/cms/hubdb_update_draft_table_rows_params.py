# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .cms_hubdb_hub_db_table_row_v3_batch_update_request_param import CmsHubdbHubDBTableRowV3BatchUpdateRequestParam

__all__ = ["HubdbUpdateDraftTableRowsParams"]


class HubdbUpdateDraftTableRowsParams(TypedDict, total=False):
    inputs: Required[Iterable[CmsHubdbHubDBTableRowV3BatchUpdateRequestParam]]
