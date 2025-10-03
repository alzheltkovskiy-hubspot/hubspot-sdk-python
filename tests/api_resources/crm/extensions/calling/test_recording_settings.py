# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm.extensions import CRMExtensionsCallingRecordingSettingsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecordingSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_url_format(self, client: HubSpot) -> None:
        recording_setting = client.crm.extensions.calling.recording_settings.get_url_format(
            0,
        )
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_url_format(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.recording_settings.with_raw_response.get_url_format(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording_setting = response.parse()
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_url_format(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.recording_settings.with_streaming_response.get_url_format(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording_setting = response.parse()
            assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_mark_as_ready(self, client: HubSpot) -> None:
        recording_setting = client.crm.extensions.calling.recording_settings.mark_as_ready(
            engagement_id=0,
        )
        assert recording_setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_mark_as_ready(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.recording_settings.with_raw_response.mark_as_ready(
            engagement_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording_setting = response.parse()
        assert recording_setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_mark_as_ready(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.recording_settings.with_streaming_response.mark_as_ready(
            engagement_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording_setting = response.parse()
            assert recording_setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_url_format(self, client: HubSpot) -> None:
        recording_setting = client.crm.extensions.calling.recording_settings.register_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_register_url_format(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.recording_settings.with_raw_response.register_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording_setting = response.parse()
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_register_url_format(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.recording_settings.with_streaming_response.register_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording_setting = response.parse()
            assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_url_format(self, client: HubSpot) -> None:
        recording_setting = client.crm.extensions.calling.recording_settings.update_url_format(
            app_id=0,
        )
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_url_format_with_all_params(self, client: HubSpot) -> None:
        recording_setting = client.crm.extensions.calling.recording_settings.update_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_url_format(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.recording_settings.with_raw_response.update_url_format(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording_setting = response.parse()
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_url_format(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.recording_settings.with_streaming_response.update_url_format(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording_setting = response.parse()
            assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRecordingSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_url_format(self, async_client: AsyncHubSpot) -> None:
        recording_setting = await async_client.crm.extensions.calling.recording_settings.get_url_format(
            0,
        )
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_url_format(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.recording_settings.with_raw_response.get_url_format(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording_setting = await response.parse()
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_url_format(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.recording_settings.with_streaming_response.get_url_format(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording_setting = await response.parse()
            assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_mark_as_ready(self, async_client: AsyncHubSpot) -> None:
        recording_setting = await async_client.crm.extensions.calling.recording_settings.mark_as_ready(
            engagement_id=0,
        )
        assert recording_setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_mark_as_ready(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.recording_settings.with_raw_response.mark_as_ready(
            engagement_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording_setting = await response.parse()
        assert recording_setting is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_mark_as_ready(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.recording_settings.with_streaming_response.mark_as_ready(
            engagement_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording_setting = await response.parse()
            assert recording_setting is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_url_format(self, async_client: AsyncHubSpot) -> None:
        recording_setting = await async_client.crm.extensions.calling.recording_settings.register_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_register_url_format(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.recording_settings.with_raw_response.register_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording_setting = await response.parse()
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_register_url_format(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.recording_settings.with_streaming_response.register_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording_setting = await response.parse()
            assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_url_format(self, async_client: AsyncHubSpot) -> None:
        recording_setting = await async_client.crm.extensions.calling.recording_settings.update_url_format(
            app_id=0,
        )
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_url_format_with_all_params(self, async_client: AsyncHubSpot) -> None:
        recording_setting = await async_client.crm.extensions.calling.recording_settings.update_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_url_format(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.recording_settings.with_raw_response.update_url_format(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording_setting = await response.parse()
        assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_url_format(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.recording_settings.with_streaming_response.update_url_format(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording_setting = await response.parse()
            assert_matches_type(CRMExtensionsCallingRecordingSettingsResponse, recording_setting, path=["response"])

        assert cast(Any, response.is_closed) is True
