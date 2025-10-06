# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SignedURL"]


class SignedURL(BaseModel):
    expires_at: datetime = FieldInfo(alias="expiresAt")

    extension: str

    name: str

    size: int

    type: str

    url: str

    height: Optional[int] = None

    width: Optional[int] = None
