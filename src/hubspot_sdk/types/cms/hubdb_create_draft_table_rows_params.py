# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .cms_hubdb_hub_db_table_row_v3_request_param import CmsHubdbHubDBTableRowV3RequestParam

__all__ = ["HubdbCreateDraftTableRowsParams"]


class HubdbCreateDraftTableRowsParams(TypedDict, total=False):
    inputs: Required[Iterable[CmsHubdbHubDBTableRowV3RequestParam]]
