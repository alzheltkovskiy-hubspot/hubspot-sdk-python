# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...public_object_id_param import PublicObjectIDParam
from .association_spec_1_param import AssociationSpec1Param

__all__ = ["PublicAssociationMultiPostParam"]

_PublicAssociationMultiPostParamReservedKeywords = TypedDict(
    "_PublicAssociationMultiPostParamReservedKeywords",
    {
        "from": PublicObjectIDParam,
    },
    total=False,
)


class PublicAssociationMultiPostParam(_PublicAssociationMultiPostParamReservedKeywords, total=False):
    to: Required[PublicObjectIDParam]

    types: Required[Iterable[AssociationSpec1Param]]
