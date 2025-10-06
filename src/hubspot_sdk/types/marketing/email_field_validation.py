# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailFieldValidation"]


class EmailFieldValidation(BaseModel):
    blocked_email_domains: List[str] = FieldInfo(alias="blockedEmailDomains")

    use_default_block_list: bool = FieldInfo(alias="useDefaultBlockList")
