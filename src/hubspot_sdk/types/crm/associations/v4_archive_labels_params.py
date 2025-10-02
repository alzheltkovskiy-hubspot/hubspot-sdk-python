# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .crm_associations_v4_public_association_multi_post_param import CRMAssociationsV4PublicAssociationMultiPostParam

__all__ = ["V4ArchiveLabelsParams"]


class V4ArchiveLabelsParams(TypedDict, total=False):
    from_object_type: Required[Annotated[str, PropertyInfo(alias="fromObjectType")]]

    inputs: Required[Iterable[CRMAssociationsV4PublicAssociationMultiPostParam]]
