# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmailGetHistogramParams"]


class EmailGetHistogramParams(TypedDict, total=False):
    email_ids: Annotated[Iterable[int], PropertyInfo(alias="emailIds")]
    """Filter by email IDs. Only include statistics of emails with these IDs."""

    end_timestamp: Annotated[str, PropertyInfo(alias="endTimestamp")]
    """The end timestamp of the time span, in ISO8601 representation."""

    interval: Literal["YEAR", "QUARTER", "MONTH", "WEEK", "DAY", "HOUR", "QUARTER_HOUR", "MINUTE", "SECOND"]
    """The interval to aggregate statistics for."""

    start_timestamp: Annotated[str, PropertyInfo(alias="startTimestamp")]
    """The start timestamp of the time span, in ISO8601 representation."""
