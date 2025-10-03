# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MarketingEmailsPublicEmailFromDetailsParam"]


class MarketingEmailsPublicEmailFromDetailsParam(TypedDict, total=False):
    custom_reply_to: Annotated[str, PropertyInfo(alias="customReplyTo")]

    from_name: Annotated[str, PropertyInfo(alias="fromName")]

    reply_to: Annotated[str, PropertyInfo(alias="replyTo")]
