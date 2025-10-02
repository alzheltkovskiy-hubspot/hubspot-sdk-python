# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["URLRedirectCreateParams"]


class URLRedirectCreateParams(TypedDict, total=False):
    destination: Required[str]

    redirect_style: Required[Annotated[int, PropertyInfo(alias="redirectStyle")]]

    route_prefix: Required[Annotated[str, PropertyInfo(alias="routePrefix")]]

    is_match_full_url: Annotated[bool, PropertyInfo(alias="isMatchFullUrl")]

    is_match_query_string: Annotated[bool, PropertyInfo(alias="isMatchQueryString")]

    is_only_after_not_found: Annotated[bool, PropertyInfo(alias="isOnlyAfterNotFound")]

    is_pattern: Annotated[bool, PropertyInfo(alias="isPattern")]

    is_protocol_agnostic: Annotated[bool, PropertyInfo(alias="isProtocolAgnostic")]

    is_trailing_slash_optional: Annotated[bool, PropertyInfo(alias="isTrailingSlashOptional")]

    precedence: int
