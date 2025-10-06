# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .form_style import FormStyle

__all__ = ["FormDisplayOptions"]


class FormDisplayOptions(BaseModel):
    render_raw_html: bool = FieldInfo(alias="renderRawHtml")

    style: FormStyle

    submit_button_text: str = FieldInfo(alias="submitButtonText")

    theme: Literal["default_style", "canvas", "linear", "round", "sharp", "legacy"]

    css_class: Optional[str] = FieldInfo(alias="cssClass", default=None)
