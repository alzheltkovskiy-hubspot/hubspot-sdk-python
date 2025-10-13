# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EnumeratedFieldOption"]


class EnumeratedFieldOption(BaseModel):
    display_order: int = FieldInfo(alias="displayOrder")
    """The order the choices will be displayed in."""

    label: str
    """The visible label for this choice."""

    value: str
    """The value which will be submitted if this choice is selected."""

    description: Optional[str] = None
