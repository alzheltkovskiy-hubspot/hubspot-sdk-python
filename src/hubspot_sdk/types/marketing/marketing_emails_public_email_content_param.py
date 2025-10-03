# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .marketing_emails_smart_email_field_param import MarketingEmailsSmartEmailFieldParam
from .marketing_emails_public_email_style_settings_param import MarketingEmailsPublicEmailStyleSettingsParam

__all__ = ["MarketingEmailsPublicEmailContentParam"]


class MarketingEmailsPublicEmailContentParam(TypedDict, total=False):
    flex_areas: Annotated[Dict[str, object], PropertyInfo(alias="flexAreas")]

    plain_text_version: Annotated[str, PropertyInfo(alias="plainTextVersion")]

    smart_fields: Annotated[Dict[str, MarketingEmailsSmartEmailFieldParam], PropertyInfo(alias="smartFields")]

    style_settings: Annotated[MarketingEmailsPublicEmailStyleSettingsParam, PropertyInfo(alias="styleSettings")]

    template_path: Annotated[str, PropertyInfo(alias="templatePath")]

    theme_settings_values: Annotated[Dict[str, object], PropertyInfo(alias="themeSettingsValues")]

    widget_containers: Annotated[Dict[str, object], PropertyInfo(alias="widgetContainers")]

    widgets: Dict[str, object]
