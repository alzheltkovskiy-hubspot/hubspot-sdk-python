# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ObjectTypeDefinitionLabelsParam"]


class ObjectTypeDefinitionLabelsParam(TypedDict, total=False):
    plural: str
    """The word for multiple objects. (There’s no way to change this later.)"""

    singular: str
    """The word for one object. (There’s no way to change this later.)"""
