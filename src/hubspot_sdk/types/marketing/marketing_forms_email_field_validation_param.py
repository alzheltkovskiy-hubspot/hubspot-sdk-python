# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["MarketingFormsEmailFieldValidationParam"]


class MarketingFormsEmailFieldValidationParam(TypedDict, total=False):
    blocked_email_domains: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="blockedEmailDomains")]]

    use_default_block_list: Required[Annotated[bool, PropertyInfo(alias="useDefaultBlockList")]]
