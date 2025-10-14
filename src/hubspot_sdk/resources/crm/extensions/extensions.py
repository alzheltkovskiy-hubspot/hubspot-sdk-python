# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .calling import (
    CallingResource,
    AsyncCallingResource,
    CallingResourceWithRawResponse,
    AsyncCallingResourceWithRawResponse,
    CallingResourceWithStreamingResponse,
    AsyncCallingResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ExtensionsResource", "AsyncExtensionsResource"]


class ExtensionsResource(SyncAPIResource):
    @cached_property
    def calling(self) -> CallingResource:
        return CallingResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExtensionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExtensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtensionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return ExtensionsResourceWithStreamingResponse(self)


class AsyncExtensionsResource(AsyncAPIResource):
    @cached_property
    def calling(self) -> AsyncCallingResource:
        return AsyncCallingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExtensionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtensionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncExtensionsResourceWithStreamingResponse(self)


class ExtensionsResourceWithRawResponse:
    def __init__(self, extensions: ExtensionsResource) -> None:
        self._extensions = extensions

    @cached_property
    def calling(self) -> CallingResourceWithRawResponse:
        return CallingResourceWithRawResponse(self._extensions.calling)


class AsyncExtensionsResourceWithRawResponse:
    def __init__(self, extensions: AsyncExtensionsResource) -> None:
        self._extensions = extensions

    @cached_property
    def calling(self) -> AsyncCallingResourceWithRawResponse:
        return AsyncCallingResourceWithRawResponse(self._extensions.calling)


class ExtensionsResourceWithStreamingResponse:
    def __init__(self, extensions: ExtensionsResource) -> None:
        self._extensions = extensions

    @cached_property
    def calling(self) -> CallingResourceWithStreamingResponse:
        return CallingResourceWithStreamingResponse(self._extensions.calling)


class AsyncExtensionsResourceWithStreamingResponse:
    def __init__(self, extensions: AsyncExtensionsResource) -> None:
        self._extensions = extensions

    @cached_property
    def calling(self) -> AsyncCallingResourceWithStreamingResponse:
        return AsyncCallingResourceWithStreamingResponse(self._extensions.calling)
