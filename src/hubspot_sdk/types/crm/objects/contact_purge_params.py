# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ContactPurgeParams"]


class ContactPurgeParams(TypedDict, total=False):
    object_id: Required[Annotated[str, PropertyInfo(alias="objectId")]]

    id_property: Annotated[str, PropertyInfo(alias="idProperty")]
