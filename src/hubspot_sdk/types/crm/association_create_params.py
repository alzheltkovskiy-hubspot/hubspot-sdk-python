# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .crm_associations_public_association_param import CRMAssociationsPublicAssociationParam

__all__ = ["AssociationCreateParams"]


class AssociationCreateParams(TypedDict, total=False):
    from_object_type: Required[Annotated[str, PropertyInfo(alias="fromObjectType")]]

    inputs: Required[Iterable[CRMAssociationsPublicAssociationParam]]
