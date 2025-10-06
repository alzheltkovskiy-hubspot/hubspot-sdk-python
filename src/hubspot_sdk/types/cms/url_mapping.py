# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["URLMapping"]


class URLMapping(BaseModel):
    id: str

    destination: str

    is_match_full_url: bool = FieldInfo(alias="isMatchFullUrl")

    is_match_query_string: bool = FieldInfo(alias="isMatchQueryString")

    is_only_after_not_found: bool = FieldInfo(alias="isOnlyAfterNotFound")

    is_pattern: bool = FieldInfo(alias="isPattern")

    is_protocol_agnostic: bool = FieldInfo(alias="isProtocolAgnostic")

    is_trailing_slash_optional: bool = FieldInfo(alias="isTrailingSlashOptional")

    precedence: int

    redirect_style: int = FieldInfo(alias="redirectStyle")

    route_prefix: str = FieldInfo(alias="routePrefix")

    created: Optional[datetime] = None

    updated: Optional[datetime] = None
