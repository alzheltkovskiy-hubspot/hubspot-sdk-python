# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MessageUpdateStatusParams"]


class MessageUpdateStatusParams(TypedDict, total=False):
    channel_id: Required[Annotated[str, PropertyInfo(alias="channelId")]]

    status_type: Required[Annotated[Literal["SENT", "FAILED", "READ"], PropertyInfo(alias="statusType")]]

    error_message: Annotated[str, PropertyInfo(alias="errorMessage")]
