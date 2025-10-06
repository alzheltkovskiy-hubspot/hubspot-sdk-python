# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PublicWideStatus"]


class PublicWideStatus(BaseModel):
    channel: Literal["EMAIL"]

    status: Literal["SUBSCRIBED", "UNSUBSCRIBED", "NOT_SPECIFIED"]

    subscriber_id_string: str = FieldInfo(alias="subscriberIdString")

    timestamp: datetime

    wide_status_type: Literal["PORTAL_WIDE", "BUSINESS_UNIT_WIDE"] = FieldInfo(alias="wideStatusType")

    business_unit_id: Optional[int] = FieldInfo(alias="businessUnitId", default=None)
