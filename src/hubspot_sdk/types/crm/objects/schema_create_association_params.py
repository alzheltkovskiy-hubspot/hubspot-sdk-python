# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SchemaCreateAssociationParams"]


class SchemaCreateAssociationParams(TypedDict, total=False):
    from_object_type_id: Required[Annotated[str, PropertyInfo(alias="fromObjectTypeId")]]
    """ID of the primary object type to link from."""

    to_object_type_id: Required[Annotated[str, PropertyInfo(alias="toObjectTypeId")]]
    """ID of the target object type to link to."""

    name: str
    """A unique name for this association."""
