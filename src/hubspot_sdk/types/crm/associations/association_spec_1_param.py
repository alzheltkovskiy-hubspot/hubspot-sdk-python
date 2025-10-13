# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AssociationSpec1Param"]


class AssociationSpec1Param(TypedDict, total=False):
    association_category: Required[
        Annotated[
            Literal["HUBSPOT_DEFINED", "USER_DEFINED", "INTEGRATOR_DEFINED"], PropertyInfo(alias="associationCategory")
        ]
    ]
    """The category of the association, such as "HUBSPOT_DEFINED"."""

    association_type_id: Required[Annotated[int, PropertyInfo(alias="associationTypeId")]]
    """The ID representing the specific type of association."""
