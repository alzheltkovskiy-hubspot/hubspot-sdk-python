# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicUser"]


class PublicUser(BaseModel):
    id: str

    email: str

    first_name: Optional[str] = FieldInfo(alias="firstName", default=None)

    last_name: Optional[str] = FieldInfo(alias="lastName", default=None)

    primary_team_id: Optional[str] = FieldInfo(alias="primaryTeamId", default=None)

    role_id: Optional[str] = FieldInfo(alias="roleId", default=None)

    role_ids: Optional[List[str]] = FieldInfo(alias="roleIds", default=None)

    secondary_team_ids: Optional[List[str]] = FieldInfo(alias="secondaryTeamIds", default=None)

    send_welcome_email: Optional[bool] = FieldInfo(alias="sendWelcomeEmail", default=None)

    super_admin: Optional[bool] = FieldInfo(alias="superAdmin", default=None)
