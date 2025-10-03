# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .marketing_emails_public_font_style_param import MarketingEmailsPublicFontStyleParam

__all__ = ["MarketingEmailsPublicButtonStyleSettingsParam"]


class MarketingEmailsPublicButtonStyleSettingsParam(TypedDict, total=False):
    background_color: Annotated[object, PropertyInfo(alias="backgroundColor")]

    corner_radius: Annotated[int, PropertyInfo(alias="cornerRadius")]

    font_style: Annotated[MarketingEmailsPublicFontStyleParam, PropertyInfo(alias="fontStyle")]
