# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ...association_spec_param import AssociationSpecParam

__all__ = ["V4CreateParams"]


class V4CreateParams(TypedDict, total=False):
    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    object_id: Required[Annotated[str, PropertyInfo(alias="objectId")]]

    to_object_type: Required[Annotated[str, PropertyInfo(alias="toObjectType")]]

    body: Required[Iterable[AssociationSpecParam]]
