# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .marketing_emails_public_font_style import MarketingEmailsPublicFontStyle

__all__ = ["MarketingEmailsPublicButtonStyleSettings"]


class MarketingEmailsPublicButtonStyleSettings(BaseModel):
    background_color: Optional[object] = FieldInfo(alias="backgroundColor", default=None)

    corner_radius: Optional[int] = FieldInfo(alias="cornerRadius", default=None)

    font_style: Optional[MarketingEmailsPublicFontStyle] = FieldInfo(alias="fontStyle", default=None)
