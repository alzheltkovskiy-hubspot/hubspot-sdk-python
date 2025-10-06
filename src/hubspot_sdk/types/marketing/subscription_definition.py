# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubscriptionDefinition"]


class SubscriptionDefinition(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    is_active: bool = FieldInfo(alias="isActive")

    is_default: bool = FieldInfo(alias="isDefault")

    is_internal: bool = FieldInfo(alias="isInternal")

    name: str

    updated_at: datetime = FieldInfo(alias="updatedAt")

    business_unit_id: Optional[int] = FieldInfo(alias="businessUnitId", default=None)

    communication_method: Optional[str] = FieldInfo(alias="communicationMethod", default=None)

    purpose: Optional[str] = None
