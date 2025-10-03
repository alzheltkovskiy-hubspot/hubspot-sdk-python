# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.crm.extensions.calling import (
    recording_setting_mark_as_ready_params,
    recording_setting_update_url_format_params,
    recording_setting_register_url_format_params,
)
from .....types.crm.extensions.crm_extensions_calling_recording_settings_response import (
    CRMExtensionsCallingRecordingSettingsResponse,
)

__all__ = ["RecordingSettingsResource", "AsyncRecordingSettingsResource"]


class RecordingSettingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecordingSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RecordingSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecordingSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return RecordingSettingsResourceWithStreamingResponse(self)

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
    ) -> CRMExtensionsCallingRecordingSettingsResponse:
        """
        Retrieve recording settings

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
            cast_to=CRMExtensionsCallingRecordingSettingsResponse,
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
        Mark recording as ready for transcription

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
                {"engagement_id": engagement_id},
                recording_setting_mark_as_ready_params.RecordingSettingMarkAsReadyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> CRMExtensionsCallingRecordingSettingsResponse:
        """
        Enable the app for call recording

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
                recording_setting_register_url_format_params.RecordingSettingRegisterURLFormatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMExtensionsCallingRecordingSettingsResponse,
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
    ) -> CRMExtensionsCallingRecordingSettingsResponse:
        """
        Update recording settings

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
                recording_setting_update_url_format_params.RecordingSettingUpdateURLFormatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMExtensionsCallingRecordingSettingsResponse,
        )


class AsyncRecordingSettingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecordingSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecordingSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecordingSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncRecordingSettingsResourceWithStreamingResponse(self)

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
    ) -> CRMExtensionsCallingRecordingSettingsResponse:
        """
        Retrieve recording settings

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
            cast_to=CRMExtensionsCallingRecordingSettingsResponse,
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
        Mark recording as ready for transcription

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
                {"engagement_id": engagement_id},
                recording_setting_mark_as_ready_params.RecordingSettingMarkAsReadyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
    ) -> CRMExtensionsCallingRecordingSettingsResponse:
        """
        Enable the app for call recording

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
                recording_setting_register_url_format_params.RecordingSettingRegisterURLFormatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMExtensionsCallingRecordingSettingsResponse,
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
    ) -> CRMExtensionsCallingRecordingSettingsResponse:
        """
        Update recording settings

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
                recording_setting_update_url_format_params.RecordingSettingUpdateURLFormatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMExtensionsCallingRecordingSettingsResponse,
        )


class RecordingSettingsResourceWithRawResponse:
    def __init__(self, recording_settings: RecordingSettingsResource) -> None:
        self._recording_settings = recording_settings

        self.get_url_format = to_raw_response_wrapper(
            recording_settings.get_url_format,
        )
        self.mark_as_ready = to_raw_response_wrapper(
            recording_settings.mark_as_ready,
        )
        self.register_url_format = to_raw_response_wrapper(
            recording_settings.register_url_format,
        )
        self.update_url_format = to_raw_response_wrapper(
            recording_settings.update_url_format,
        )


class AsyncRecordingSettingsResourceWithRawResponse:
    def __init__(self, recording_settings: AsyncRecordingSettingsResource) -> None:
        self._recording_settings = recording_settings

        self.get_url_format = async_to_raw_response_wrapper(
            recording_settings.get_url_format,
        )
        self.mark_as_ready = async_to_raw_response_wrapper(
            recording_settings.mark_as_ready,
        )
        self.register_url_format = async_to_raw_response_wrapper(
            recording_settings.register_url_format,
        )
        self.update_url_format = async_to_raw_response_wrapper(
            recording_settings.update_url_format,
        )


class RecordingSettingsResourceWithStreamingResponse:
    def __init__(self, recording_settings: RecordingSettingsResource) -> None:
        self._recording_settings = recording_settings

        self.get_url_format = to_streamed_response_wrapper(
            recording_settings.get_url_format,
        )
        self.mark_as_ready = to_streamed_response_wrapper(
            recording_settings.mark_as_ready,
        )
        self.register_url_format = to_streamed_response_wrapper(
            recording_settings.register_url_format,
        )
        self.update_url_format = to_streamed_response_wrapper(
            recording_settings.update_url_format,
        )


class AsyncRecordingSettingsResourceWithStreamingResponse:
    def __init__(self, recording_settings: AsyncRecordingSettingsResource) -> None:
        self._recording_settings = recording_settings

        self.get_url_format = async_to_streamed_response_wrapper(
            recording_settings.get_url_format,
        )
        self.mark_as_ready = async_to_streamed_response_wrapper(
            recording_settings.mark_as_ready,
        )
        self.register_url_format = async_to_streamed_response_wrapper(
            recording_settings.register_url_format,
        )
        self.update_url_format = async_to_streamed_response_wrapper(
            recording_settings.update_url_format,
        )
