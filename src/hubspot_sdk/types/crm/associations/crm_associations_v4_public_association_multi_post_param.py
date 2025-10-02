# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...crm_association_spec_param import CRMAssociationSpecParam
from ...crm_public_object_id_param import CRMPublicObjectIDParam

__all__ = ["CRMAssociationsV4PublicAssociationMultiPostParam"]

_CRMAssociationsV4PublicAssociationMultiPostParamReservedKeywords = TypedDict(
    "_CRMAssociationsV4PublicAssociationMultiPostParamReservedKeywords",
    {
        "from": CRMPublicObjectIDParam,
    },
    total=False,
)


class CRMAssociationsV4PublicAssociationMultiPostParam(
    _CRMAssociationsV4PublicAssociationMultiPostParamReservedKeywords, total=False
):
    to: Required[CRMPublicObjectIDParam]

    types: Required[Iterable[CRMAssociationSpecParam]]
