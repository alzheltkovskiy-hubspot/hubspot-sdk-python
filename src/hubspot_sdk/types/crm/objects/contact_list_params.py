# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["ContactListParams"]


class ContactListParams(TypedDict, total=False):
    after: str

    archived: bool

    associations: SequenceNotStr[str]

    limit: int

    properties: SequenceNotStr[str]

    properties_with_history: Annotated[SequenceNotStr[str], PropertyInfo(alias="propertiesWithHistory")]
