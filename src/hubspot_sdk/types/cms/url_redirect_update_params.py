# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["URLRedirectUpdateParams"]


class URLRedirectUpdateParams(TypedDict, total=False):
    id: Required[str]

    destination: Required[str]

    is_match_full_url: Required[Annotated[bool, PropertyInfo(alias="isMatchFullUrl")]]

    is_match_query_string: Required[Annotated[bool, PropertyInfo(alias="isMatchQueryString")]]

    is_only_after_not_found: Required[Annotated[bool, PropertyInfo(alias="isOnlyAfterNotFound")]]

    is_pattern: Required[Annotated[bool, PropertyInfo(alias="isPattern")]]

    is_protocol_agnostic: Required[Annotated[bool, PropertyInfo(alias="isProtocolAgnostic")]]

    is_trailing_slash_optional: Required[Annotated[bool, PropertyInfo(alias="isTrailingSlashOptional")]]

    precedence: Required[int]

    redirect_style: Required[Annotated[int, PropertyInfo(alias="redirectStyle")]]

    route_prefix: Required[Annotated[str, PropertyInfo(alias="routePrefix")]]

    created: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    updated: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
