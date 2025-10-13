# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["RgbaColor"]


class RgbaColor(BaseModel):
    a: float
    """Alpha."""

    b: int
    """Blue."""

    g: int
    """Green."""

    r: int
    """Red."""
