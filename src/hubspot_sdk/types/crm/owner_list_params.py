# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OwnerListParams"]


class OwnerListParams(TypedDict, total=False):
    after: str
    """
    The paging cursor token of the last successfully read resource will be returned
    as the `paging.next.after` JSON property of a paged response containing more
    results (optional).
    """

    archived: bool
    """Whether to return only results that have been archived."""

    email: str
    """Filter by email address (optional)."""

    limit: int
    """The maximum number of results to display per page."""
