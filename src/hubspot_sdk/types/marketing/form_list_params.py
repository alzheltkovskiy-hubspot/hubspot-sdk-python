# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FormListParams"]


class FormListParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results.
    """

    archived: bool
    """Whether to return only results that have been archived."""

    form_types: Annotated[
        List[Literal["hubspot", "captured", "flow", "blog_comment", "all"]], PropertyInfo(alias="formTypes")
    ]
    """The form types to be included in the results."""

    limit: int
    """The maximum number of results to display per page."""
