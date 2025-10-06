# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    email: Required[str]

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    primary_team_id: Annotated[str, PropertyInfo(alias="primaryTeamId")]

    role_id: Annotated[str, PropertyInfo(alias="roleId")]

    secondary_team_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="secondaryTeamIds")]

    send_welcome_email: Annotated[bool, PropertyInfo(alias="sendWelcomeEmail")]
