# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketingEmailsPublicDividerStyleSettings"]


class MarketingEmailsPublicDividerStyleSettings(BaseModel):
    color: Optional[object] = None

    height: Optional[int] = None

    line_type: Optional[str] = FieldInfo(alias="lineType", default=None)
