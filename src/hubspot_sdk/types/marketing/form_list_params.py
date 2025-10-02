# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FormListParams"]


class FormListParams(TypedDict, total=False):
    after: str

    archived: bool

    form_types: Annotated[
        List[Literal["hubspot", "captured", "flow", "blog_comment", "all"]], PropertyInfo(alias="formTypes")
    ]

    limit: int
