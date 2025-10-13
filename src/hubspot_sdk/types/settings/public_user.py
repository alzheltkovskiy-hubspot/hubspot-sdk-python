# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicUser"]


class PublicUser(BaseModel):
    id: str
    """The user's unique ID"""

    email: str
    """The user's email"""

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    primary_team_id: Optional[str] = FieldInfo(alias="primaryTeamId", default=None)
    """The user's primary team"""

    role_id: Optional[str] = FieldInfo(alias="roleId", default=None)
    """The user's role"""

    role_ids: Optional[List[str]] = FieldInfo(alias="roleIds", default=None)

    secondary_team_ids: Optional[List[str]] = FieldInfo(alias="secondaryTeamIds", default=None)
    """The user's additional teams"""

    send_welcome_email: Optional[bool] = FieldInfo(alias="sendWelcomeEmail", default=None)

    super_admin: Optional[bool] = FieldInfo(alias="superAdmin", default=None)
