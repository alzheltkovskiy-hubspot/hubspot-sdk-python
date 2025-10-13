# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ObjectTypeDefinitionLabels"]


class ObjectTypeDefinitionLabels(BaseModel):
    plural: Optional[str] = None
    """The word for multiple objects. (There’s no way to change this later.)"""

    singular: Optional[str] = None
    """The word for one object. (There’s no way to change this later.)"""
