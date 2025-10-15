# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["HubdbReadDraftBatchParams"]


class HubdbReadDraftBatchParams(TypedDict, total=False):
    inputs: Required[SequenceNotStr[str]]
    """Strings to input."""
