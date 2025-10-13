# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    after: str
    """Results will display maximum 100 users per page.

    Additional results will be on the next page.
    """

    limit: int
    """The number of users to retrieve"""
