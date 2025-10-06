# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .hub_db_table_row_v3 import HubDBTableRowV3

__all__ = ["BatchResponseHubDBTableRowV3"]


class BatchResponseHubDBTableRowV3(BaseModel):
    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)

    links: Optional[Dict[str, str]] = None

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)

    results: Optional[List[HubDBTableRowV3]] = None

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)

    status: Optional[Literal["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]] = None
