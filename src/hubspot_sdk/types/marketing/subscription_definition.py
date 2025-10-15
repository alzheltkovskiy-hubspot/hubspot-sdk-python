# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubscriptionDefinition"]


class SubscriptionDefinition(BaseModel):
    id: str
    """The ID of the definition."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Time at which the definition was created."""

    description: str
    """A description of the subscription."""

    is_active: bool = FieldInfo(alias="isActive")
    """Whether the definition is active or archived."""

    is_default: bool = FieldInfo(alias="isDefault")
    """A subscription definition created by HubSpot."""

    is_internal: bool = FieldInfo(alias="isInternal")
    """A default description that is used by some HubSpot tools and cannot be edited."""

    name: str
    """The name of the subscription."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Time at which the definition was last updated."""

    business_unit_id: Optional[int] = FieldInfo(alias="businessUnitId", default=None)
    """The ID of the business unit associated with the subscription definition."""

    communication_method: Optional[str] = FieldInfo(alias="communicationMethod", default=None)
    """The method or technology used to contact."""

    purpose: Optional[str] = None
    """
    The purpose of this subscription or the department in your organization that
    uses it.
    """
