# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AuthOAuthTokenResponseIf"]


class AuthOAuthTokenResponseIf(BaseModel):
    access_token: str

    expires_in: int

    refresh_token: str

    token_type: str

    id_token: Optional[str] = None
