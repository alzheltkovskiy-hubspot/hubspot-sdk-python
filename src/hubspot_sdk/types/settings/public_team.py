# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicTeam"]


class PublicTeam(BaseModel):
    id: str

    name: str

    secondary_user_ids: List[str] = FieldInfo(alias="secondaryUserIds")

    user_ids: List[str] = FieldInfo(alias="userIds")
