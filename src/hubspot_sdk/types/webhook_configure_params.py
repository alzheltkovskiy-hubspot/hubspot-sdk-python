# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .webhooks_throttling_settings_param import WebhooksThrottlingSettingsParam

__all__ = ["WebhookConfigureParams"]


class WebhookConfigureParams(TypedDict, total=False):
    target_url: Required[Annotated[str, PropertyInfo(alias="targetUrl")]]

    throttling: Required[WebhooksThrottlingSettingsParam]
