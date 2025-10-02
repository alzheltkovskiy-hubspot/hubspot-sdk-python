# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CRMOption"]


class CRMOption(BaseModel):
    hidden: bool

    label: str

    value: str

    display_order: Optional[int] = FieldInfo(alias="displayOrder", default=None)
