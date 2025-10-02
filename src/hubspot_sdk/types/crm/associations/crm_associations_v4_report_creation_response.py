# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .crm_associations_v4_date_time import CRMAssociationsV4DateTime

__all__ = ["CRMAssociationsV4ReportCreationResponse"]


class CRMAssociationsV4ReportCreationResponse(BaseModel):
    enqueue_time: CRMAssociationsV4DateTime = FieldInfo(alias="enqueueTime")

    user_email: str = FieldInfo(alias="userEmail")

    user_id: int = FieldInfo(alias="userId")
