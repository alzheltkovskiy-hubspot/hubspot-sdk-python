# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RowsResource", "AsyncRowsResource"]


class RowsResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> RowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return RowsResourceWithStreamingResponse(self)


class AsyncRowsResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncRowsResourceWithStreamingResponse(self)


class RowsResourceWithRawResponse:
    def __init__(self, rows: RowsResource) -> None:
        self._rows = rows

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._rows.batch)


class AsyncRowsResourceWithRawResponse:
    def __init__(self, rows: AsyncRowsResource) -> None:
        self._rows = rows

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._rows.batch)


class RowsResourceWithStreamingResponse:
    def __init__(self, rows: RowsResource) -> None:
        self._rows = rows

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._rows.batch)


class AsyncRowsResourceWithStreamingResponse:
    def __init__(self, rows: AsyncRowsResource) -> None:
        self._rows = rows

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._rows.batch)
