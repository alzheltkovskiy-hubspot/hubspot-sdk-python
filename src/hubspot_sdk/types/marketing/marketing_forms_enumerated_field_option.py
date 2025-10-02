# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketingFormsEnumeratedFieldOption"]


class MarketingFormsEnumeratedFieldOption(BaseModel):
    display_order: int = FieldInfo(alias="displayOrder")

    label: str

    value: str
