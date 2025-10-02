# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .marketing_forms_form_style import MarketingFormsFormStyle

__all__ = ["MarketingFormsFormDisplayOptions"]


class MarketingFormsFormDisplayOptions(BaseModel):
    render_raw_html: bool = FieldInfo(alias="renderRawHtml")

    style: MarketingFormsFormStyle

    submit_button_text: str = FieldInfo(alias="submitButtonText")

    theme: Literal["default_style", "canvas", "linear", "round", "sharp", "legacy"]

    css_class: Optional[str] = FieldInfo(alias="cssClass", default=None)
