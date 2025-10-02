# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .marketing_forms_form_style_param import MarketingFormsFormStyleParam

__all__ = ["MarketingFormsFormDisplayOptionsParam"]


class MarketingFormsFormDisplayOptionsParam(TypedDict, total=False):
    render_raw_html: Required[Annotated[bool, PropertyInfo(alias="renderRawHtml")]]

    style: Required[MarketingFormsFormStyleParam]

    submit_button_text: Required[Annotated[str, PropertyInfo(alias="submitButtonText")]]

    theme: Required[Literal["default_style", "canvas", "linear", "round", "sharp", "legacy"]]

    css_class: Annotated[str, PropertyInfo(alias="cssClass")]
