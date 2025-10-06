# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..public_object_id_param import PublicObjectIDParam

__all__ = ["AssociationReadParams"]


class AssociationReadParams(TypedDict, total=False):
    from_object_type: Required[Annotated[str, PropertyInfo(alias="fromObjectType")]]

    inputs: Required[Iterable[PublicObjectIDParam]]
