# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..settings.public_team import PublicTeam

__all__ = ["PublicOwner"]


class PublicOwner(BaseModel):
    id: str
    """The unique ID for the owner."""

    archived: bool
    """Whether the owner is archived."""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The timestamp when the owner was created, in ISO 8601 format."""

    type: Literal["PERSON", "QUEUE"]
    """The type of owner. Accepted values are: PERSON, QUEUE."""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The timestamp when the owner was last updated, in ISO 8601 format."""

    email: Optional[str] = None
    """The owner's email address."""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)
    """The owner's first name."""

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)
    """The owner's last name."""

    teams: Optional[List[PublicTeam]] = None

    user_id: Optional[int] = FieldInfo(alias="userId", default=None)
    """The ID of the active HubSpot user associated with the owner."""

    user_id_including_inactive: Optional[int] = FieldInfo(alias="userIdIncludingInactive", default=None)
    """The user ID, including inactive users."""
