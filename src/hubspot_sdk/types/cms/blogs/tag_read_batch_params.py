# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["TagReadBatchParams"]


class TagReadBatchParams(TypedDict, total=False):
    inputs: Required[SequenceNotStr[str]]
    """Strings to input."""

    archived: bool
    """Specifies whether to return deleted Blog Tags. Defaults to `false`."""
