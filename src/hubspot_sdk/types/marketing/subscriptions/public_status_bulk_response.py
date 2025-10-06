# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .public_status import PublicStatus

__all__ = ["PublicStatusBulkResponse"]


class PublicStatusBulkResponse(BaseModel):
    statuses: List[PublicStatus]

    subscriber_id_string: str = FieldInfo(alias="subscriberIdString")
