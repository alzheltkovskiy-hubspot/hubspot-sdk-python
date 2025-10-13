# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.crm.extensions import (
    calling_create_params,
    calling_update_params,
    calling_mark_as_ready_params,
    calling_update_url_format_params,
    calling_register_url_format_params,
)
from ....types.crm.extensions.recording_settings_response import RecordingSettingsResponse
from ....types.crm.extensions.channel_connection_settings_response import ChannelConnectionSettingsResponse

__all__ = ["CallingResource", "AsyncCallingResource"]


class CallingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CallingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CallingResourceWithStreamingResponse(self)

    def create(
        self,
        app_id: int,
        *,
        is_ready: bool,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelConnectionSettingsResponse:
        """
        Configure
        [channel connection settings](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#create-channel-connection-settings)
        for the app.

        Args:
          is_ready: If true, this app will be considered to support channel connection

          url: The URL to fetch phone numbers available for channel connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            body=maybe_transform(
                {
                    "is_ready": is_ready,
                    "url": url,
                },
                calling_create_params.CallingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelConnectionSettingsResponse,
        )

    def update(
        self,
        app_id: int,
        *,
        is_ready: bool | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelConnectionSettingsResponse:
        """
        Update existing
        [channel connection settings](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#manage-the-webhook-settings-for-channel-connection)
        for your app.

        Args:
          is_ready: If true, this app will be considered to support channel connection

          url: The URL to fetch phone numbers available for channel connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            body=maybe_transform(
                {
                    "is_ready": is_ready,
                    "url": url,
                },
                calling_update_params.CallingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelConnectionSettingsResponse,
        )

    def delete(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the
        [channel connection settings](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#delete-existing-channel-connection-settings)
        for the app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_url_format(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingSettingsResponse:
        """
        Retrieve the URL that is registered for
        [call recording](https://developers.hubspot.com/docs/guides/apps/extensions/calling-extensions/recordings-and-transcriptions#register-your-app-s-endpoint-with-hubspot-using-the-calling-settings-api).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/crm/v3/extensions/calling/{app_id}/settings/recording",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingSettingsResponse,
        )

    def mark_as_ready(
        self,
        *,
        engagement_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Mark a call recording as ready for transcription, specifying the call by its ID
        (`engagementid`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/crm/v3/extensions/calling/recordings/ready",
            body=maybe_transform(
                {"engagement_id": engagement_id}, calling_mark_as_ready_params.CallingMarkAsReadyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def read(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelConnectionSettingsResponse:
        """
        Retrieve the settings related to the app's
        [channel connection](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#fetch-existing-channel-connection-settings).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelConnectionSettingsResponse,
        )

    def register_url_format(
        self,
        app_id: int,
        *,
        url_to_retrieve_authed_recording: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingSettingsResponse:
        """
        Register an external URL that HubSpot will use to retrieve
        [call recordings](https://developers.hubspot.com/docs/guides/apps/extensions/calling-extensions/recordings-and-transcriptions#register-your-app-s-endpoint-with-hubspot-using-the-calling-settings-api).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/crm/v3/extensions/calling/{app_id}/settings/recording",
            body=maybe_transform(
                {"url_to_retrieve_authed_recording": url_to_retrieve_authed_recording},
                calling_register_url_format_params.CallingRegisterURLFormatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingSettingsResponse,
        )

    def update_url_format(
        self,
        app_id: int,
        *,
        url_to_retrieve_authed_recording: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingSettingsResponse:
        """
        Update the URL that HubSpot will use to retrieve
        [call recordings](https://developers.hubspot.com/docs/guides/apps/extensions/calling-extensions/recordings-and-transcriptions#register-your-app-s-endpoint-with-hubspot-using-the-calling-settings-api).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/crm/v3/extensions/calling/{app_id}/settings/recording",
            body=maybe_transform(
                {"url_to_retrieve_authed_recording": url_to_retrieve_authed_recording},
                calling_update_url_format_params.CallingUpdateURLFormatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingSettingsResponse,
        )


class AsyncCallingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCallingResourceWithStreamingResponse(self)

    async def create(
        self,
        app_id: int,
        *,
        is_ready: bool,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelConnectionSettingsResponse:
        """
        Configure
        [channel connection settings](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#create-channel-connection-settings)
        for the app.

        Args:
          is_ready: If true, this app will be considered to support channel connection

          url: The URL to fetch phone numbers available for channel connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            body=await async_maybe_transform(
                {
                    "is_ready": is_ready,
                    "url": url,
                },
                calling_create_params.CallingCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelConnectionSettingsResponse,
        )

    async def update(
        self,
        app_id: int,
        *,
        is_ready: bool | Omit = omit,
        url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelConnectionSettingsResponse:
        """
        Update existing
        [channel connection settings](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#manage-the-webhook-settings-for-channel-connection)
        for your app.

        Args:
          is_ready: If true, this app will be considered to support channel connection

          url: The URL to fetch phone numbers available for channel connection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            body=await async_maybe_transform(
                {
                    "is_ready": is_ready,
                    "url": url,
                },
                calling_update_params.CallingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelConnectionSettingsResponse,
        )

    async def delete(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete the
        [channel connection settings](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#delete-existing-channel-connection-settings)
        for the app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_url_format(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingSettingsResponse:
        """
        Retrieve the URL that is registered for
        [call recording](https://developers.hubspot.com/docs/guides/apps/extensions/calling-extensions/recordings-and-transcriptions#register-your-app-s-endpoint-with-hubspot-using-the-calling-settings-api).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/crm/v3/extensions/calling/{app_id}/settings/recording",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingSettingsResponse,
        )

    async def mark_as_ready(
        self,
        *,
        engagement_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Mark a call recording as ready for transcription, specifying the call by its ID
        (`engagementid`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/crm/v3/extensions/calling/recordings/ready",
            body=await async_maybe_transform(
                {"engagement_id": engagement_id}, calling_mark_as_ready_params.CallingMarkAsReadyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def read(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChannelConnectionSettingsResponse:
        """
        Retrieve the settings related to the app's
        [channel connection](https://developers.hubspot.com/docs/guides/api/crm/extensions/third-party-calling#fetch-existing-channel-connection-settings).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/crm/v3/extensions/calling/{app_id}/settings/channel-connection",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChannelConnectionSettingsResponse,
        )

    async def register_url_format(
        self,
        app_id: int,
        *,
        url_to_retrieve_authed_recording: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingSettingsResponse:
        """
        Register an external URL that HubSpot will use to retrieve
        [call recordings](https://developers.hubspot.com/docs/guides/apps/extensions/calling-extensions/recordings-and-transcriptions#register-your-app-s-endpoint-with-hubspot-using-the-calling-settings-api).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/crm/v3/extensions/calling/{app_id}/settings/recording",
            body=await async_maybe_transform(
                {"url_to_retrieve_authed_recording": url_to_retrieve_authed_recording},
                calling_register_url_format_params.CallingRegisterURLFormatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingSettingsResponse,
        )

    async def update_url_format(
        self,
        app_id: int,
        *,
        url_to_retrieve_authed_recording: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecordingSettingsResponse:
        """
        Update the URL that HubSpot will use to retrieve
        [call recordings](https://developers.hubspot.com/docs/guides/apps/extensions/calling-extensions/recordings-and-transcriptions#register-your-app-s-endpoint-with-hubspot-using-the-calling-settings-api).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/crm/v3/extensions/calling/{app_id}/settings/recording",
            body=await async_maybe_transform(
                {"url_to_retrieve_authed_recording": url_to_retrieve_authed_recording},
                calling_update_url_format_params.CallingUpdateURLFormatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecordingSettingsResponse,
        )


class CallingResourceWithRawResponse:
    def __init__(self, calling: CallingResource) -> None:
        self._calling = calling

        self.create = to_raw_response_wrapper(
            calling.create,
        )
        self.update = to_raw_response_wrapper(
            calling.update,
        )
        self.delete = to_raw_response_wrapper(
            calling.delete,
        )
        self.get_url_format = to_raw_response_wrapper(
            calling.get_url_format,
        )
        self.mark_as_ready = to_raw_response_wrapper(
            calling.mark_as_ready,
        )
        self.read = to_raw_response_wrapper(
            calling.read,
        )
        self.register_url_format = to_raw_response_wrapper(
            calling.register_url_format,
        )
        self.update_url_format = to_raw_response_wrapper(
            calling.update_url_format,
        )


class AsyncCallingResourceWithRawResponse:
    def __init__(self, calling: AsyncCallingResource) -> None:
        self._calling = calling

        self.create = async_to_raw_response_wrapper(
            calling.create,
        )
        self.update = async_to_raw_response_wrapper(
            calling.update,
        )
        self.delete = async_to_raw_response_wrapper(
            calling.delete,
        )
        self.get_url_format = async_to_raw_response_wrapper(
            calling.get_url_format,
        )
        self.mark_as_ready = async_to_raw_response_wrapper(
            calling.mark_as_ready,
        )
        self.read = async_to_raw_response_wrapper(
            calling.read,
        )
        self.register_url_format = async_to_raw_response_wrapper(
            calling.register_url_format,
        )
        self.update_url_format = async_to_raw_response_wrapper(
            calling.update_url_format,
        )


class CallingResourceWithStreamingResponse:
    def __init__(self, calling: CallingResource) -> None:
        self._calling = calling

        self.create = to_streamed_response_wrapper(
            calling.create,
        )
        self.update = to_streamed_response_wrapper(
            calling.update,
        )
        self.delete = to_streamed_response_wrapper(
            calling.delete,
        )
        self.get_url_format = to_streamed_response_wrapper(
            calling.get_url_format,
        )
        self.mark_as_ready = to_streamed_response_wrapper(
            calling.mark_as_ready,
        )
        self.read = to_streamed_response_wrapper(
            calling.read,
        )
        self.register_url_format = to_streamed_response_wrapper(
            calling.register_url_format,
        )
        self.update_url_format = to_streamed_response_wrapper(
            calling.update_url_format,
        )


class AsyncCallingResourceWithStreamingResponse:
    def __init__(self, calling: AsyncCallingResource) -> None:
        self._calling = calling

        self.create = async_to_streamed_response_wrapper(
            calling.create,
        )
        self.update = async_to_streamed_response_wrapper(
            calling.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            calling.delete,
        )
        self.get_url_format = async_to_streamed_response_wrapper(
            calling.get_url_format,
        )
        self.mark_as_ready = async_to_streamed_response_wrapper(
            calling.mark_as_ready,
        )
        self.read = async_to_streamed_response_wrapper(
            calling.read,
        )
        self.register_url_format = async_to_streamed_response_wrapper(
            calling.register_url_format,
        )
        self.update_url_format = async_to_streamed_response_wrapper(
            calling.update_url_format,
        )
