# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["DealReadParams"]


class DealReadParams(TypedDict, total=False):
    archived: bool

    associations: SequenceNotStr[str]

    id_property: Annotated[str, PropertyInfo(alias="idProperty")]

    properties: SequenceNotStr[str]

    properties_with_history: Annotated[SequenceNotStr[str], PropertyInfo(alias="propertiesWithHistory")]
