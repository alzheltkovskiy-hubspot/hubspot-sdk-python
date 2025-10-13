# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["UserCreateParams"]


class UserCreateParams(TypedDict, total=False):
    email: Required[str]
    """The created user's email"""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]

    last_name: Annotated[str, PropertyInfo(alias="lastName")]

    primary_team_id: Annotated[str, PropertyInfo(alias="primaryTeamId")]
    """The user's primary team"""

    role_id: Annotated[str, PropertyInfo(alias="roleId")]
    """The user's role"""

    secondary_team_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="secondaryTeamIds")]
    """The user's additional teams"""

    send_welcome_email: Annotated[bool, PropertyInfo(alias="sendWelcomeEmail")]
    """Whether to send a welcome email"""
