# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["TagUpdateBatchParams"]


class TagUpdateBatchParams(TypedDict, total=False):
    inputs: Required[Iterable[object]]
    """JSON nodes to input."""

    archived: bool
    """Specifies whether to update deleted Blog Tags. Defaults to `false`."""
