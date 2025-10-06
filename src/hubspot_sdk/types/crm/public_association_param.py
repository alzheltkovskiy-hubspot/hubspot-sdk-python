# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..public_object_id_param import PublicObjectIDParam

__all__ = ["PublicAssociationParam"]

_PublicAssociationParamReservedKeywords = TypedDict(
    "_PublicAssociationParamReservedKeywords",
    {
        "from": PublicObjectIDParam,
    },
    total=False,
)


class PublicAssociationParam(_PublicAssociationParamReservedKeywords, total=False):
    to: Required[PublicObjectIDParam]

    type: Required[str]
