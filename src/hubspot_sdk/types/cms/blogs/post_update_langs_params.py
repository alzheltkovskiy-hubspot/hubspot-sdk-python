# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PostUpdateLangsParams"]


class PostUpdateLangsParams(TypedDict, total=False):
    languages: Required[Dict[str, str]]

    primary_id: Required[Annotated[str, PropertyInfo(alias="primaryId")]]
