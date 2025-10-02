# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..crm_public_object_id_param import CRMPublicObjectIDParam

__all__ = ["CRMAssociationsPublicAssociationParam"]

_CRMAssociationsPublicAssociationParamReservedKeywords = TypedDict(
    "_CRMAssociationsPublicAssociationParamReservedKeywords",
    {
        "from": CRMPublicObjectIDParam,
    },
    total=False,
)


class CRMAssociationsPublicAssociationParam(_CRMAssociationsPublicAssociationParamReservedKeywords, total=False):
    to: Required[CRMPublicObjectIDParam]

    type: Required[str]
