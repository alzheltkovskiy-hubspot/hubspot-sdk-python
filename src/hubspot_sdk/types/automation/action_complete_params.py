# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ActionCompleteParams"]


class ActionCompleteParams(TypedDict, total=False):
    output_fields: Required[Annotated[Dict[str, str], PropertyInfo(alias="outputFields")]]
