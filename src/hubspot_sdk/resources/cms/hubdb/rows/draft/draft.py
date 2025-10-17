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
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DraftResource", "AsyncDraftResource"]


class DraftResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> DraftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DraftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DraftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#with_streaming_response
        """
        return DraftResourceWithStreamingResponse(self)


class AsyncDraftResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDraftResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDraftResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDraftResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncDraftResourceWithStreamingResponse(self)


class DraftResourceWithRawResponse:
    def __init__(self, draft: DraftResource) -> None:
        self._draft = draft

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._draft.batch)


class AsyncDraftResourceWithRawResponse:
    def __init__(self, draft: AsyncDraftResource) -> None:
        self._draft = draft

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._draft.batch)


class DraftResourceWithStreamingResponse:
    def __init__(self, draft: DraftResource) -> None:
        self._draft = draft

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._draft.batch)


class AsyncDraftResourceWithStreamingResponse:
    def __init__(self, draft: AsyncDraftResource) -> None:
        self._draft = draft

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._draft.batch)
