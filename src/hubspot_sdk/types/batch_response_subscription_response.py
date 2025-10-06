# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .subscription_response import SubscriptionResponse

__all__ = ["BatchResponseSubscriptionResponse"]


class BatchResponseSubscriptionResponse(BaseModel):
    completed_at: datetime = FieldInfo(alias="completedAt")

    results: List[SubscriptionResponse]

    started_at: datetime = FieldInfo(alias="startedAt")

    status: Literal["PENDING", "PROCESSING", "CANCELED", "COMPLETE"]

    links: Optional[Dict[str, str]] = None

    requested_at: Optional[datetime] = FieldInfo(alias="requestedAt", default=None)
