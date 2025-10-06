# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .public_wide_status import PublicWideStatus

__all__ = ["PublicWideStatusBulkResponse"]


class PublicWideStatusBulkResponse(BaseModel):
    subscriber_id_string: str = FieldInfo(alias="subscriberIdString")

    wide_statuses: List[PublicWideStatus] = FieldInfo(alias="wideStatuses")
