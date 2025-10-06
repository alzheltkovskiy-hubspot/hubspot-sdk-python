# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CustomChannelsResource", "AsyncCustomChannelsResource"]


class CustomChannelsResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CustomChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CustomChannelsResourceWithStreamingResponse(self)


class AsyncCustomChannelsResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomChannelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomChannelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomChannelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCustomChannelsResourceWithStreamingResponse(self)


class CustomChannelsResourceWithRawResponse:
    def __init__(self, custom_channels: CustomChannelsResource) -> None:
        self._custom_channels = custom_channels

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._custom_channels.messages)


class AsyncCustomChannelsResourceWithRawResponse:
    def __init__(self, custom_channels: AsyncCustomChannelsResource) -> None:
        self._custom_channels = custom_channels

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._custom_channels.messages)


class CustomChannelsResourceWithStreamingResponse:
    def __init__(self, custom_channels: CustomChannelsResource) -> None:
        self._custom_channels = custom_channels

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._custom_channels.messages)


class AsyncCustomChannelsResourceWithStreamingResponse:
    def __init__(self, custom_channels: AsyncCustomChannelsResource) -> None:
        self._custom_channels = custom_channels

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._custom_channels.messages)
