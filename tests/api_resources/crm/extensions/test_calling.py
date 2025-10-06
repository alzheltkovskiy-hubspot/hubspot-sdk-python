# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm.extensions import (
    RecordingSettingsResponse,
    ChannelConnectionSettingsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        calling = client.crm.extensions.calling.create(
            app_id=0,
            is_ready=True,
            url="url",
        )
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.with_raw_response.create(
            app_id=0,
            is_ready=True,
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.with_streaming_response.create(
            app_id=0,
            is_ready=True,
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        calling = client.crm.extensions.calling.update(
            app_id=0,
        )
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        calling = client.crm.extensions.calling.update(
            app_id=0,
            is_ready=True,
            url="url",
        )
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.with_raw_response.update(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.with_streaming_response.update(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        calling = client.crm.extensions.calling.delete(
            0,
        )
        assert calling is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert calling is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert calling is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_url_format(self, client: HubSpot) -> None:
        calling = client.crm.extensions.calling.get_url_format(
            0,
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_url_format(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.with_raw_response.get_url_format(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_url_format(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.with_streaming_response.get_url_format(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_mark_as_ready(self, client: HubSpot) -> None:
        calling = client.crm.extensions.calling.mark_as_ready(
            engagement_id=0,
        )
        assert calling is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_mark_as_ready(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.with_raw_response.mark_as_ready(
            engagement_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert calling is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_mark_as_ready(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.with_streaming_response.mark_as_ready(
            engagement_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert calling is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read(self, client: HubSpot) -> None:
        calling = client.crm.extensions.calling.read(
            0,
        )
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.with_raw_response.read(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.with_streaming_response.read(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_url_format(self, client: HubSpot) -> None:
        calling = client.crm.extensions.calling.register_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_register_url_format(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.with_raw_response.register_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_register_url_format(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.with_streaming_response.register_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_url_format(self, client: HubSpot) -> None:
        calling = client.crm.extensions.calling.update_url_format(
            app_id=0,
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_url_format_with_all_params(self, client: HubSpot) -> None:
        calling = client.crm.extensions.calling.update_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_url_format(self, client: HubSpot) -> None:
        response = client.crm.extensions.calling.with_raw_response.update_url_format(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = response.parse()
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_url_format(self, client: HubSpot) -> None:
        with client.crm.extensions.calling.with_streaming_response.update_url_format(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = response.parse()
            assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCalling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        calling = await async_client.crm.extensions.calling.create(
            app_id=0,
            is_ready=True,
            url="url",
        )
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.create(
            app_id=0,
            is_ready=True,
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.create(
            app_id=0,
            is_ready=True,
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        calling = await async_client.crm.extensions.calling.update(
            app_id=0,
        )
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        calling = await async_client.crm.extensions.calling.update(
            app_id=0,
            is_ready=True,
            url="url",
        )
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.update(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.update(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        calling = await async_client.crm.extensions.calling.delete(
            0,
        )
        assert calling is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert calling is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert calling is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_url_format(self, async_client: AsyncHubSpot) -> None:
        calling = await async_client.crm.extensions.calling.get_url_format(
            0,
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_url_format(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.get_url_format(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_url_format(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.get_url_format(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_mark_as_ready(self, async_client: AsyncHubSpot) -> None:
        calling = await async_client.crm.extensions.calling.mark_as_ready(
            engagement_id=0,
        )
        assert calling is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_mark_as_ready(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.mark_as_ready(
            engagement_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert calling is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_mark_as_ready(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.mark_as_ready(
            engagement_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert calling is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncHubSpot) -> None:
        calling = await async_client.crm.extensions.calling.read(
            0,
        )
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.read(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.read(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert_matches_type(ChannelConnectionSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_url_format(self, async_client: AsyncHubSpot) -> None:
        calling = await async_client.crm.extensions.calling.register_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_register_url_format(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.register_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_register_url_format(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.register_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_url_format(self, async_client: AsyncHubSpot) -> None:
        calling = await async_client.crm.extensions.calling.update_url_format(
            app_id=0,
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_url_format_with_all_params(self, async_client: AsyncHubSpot) -> None:
        calling = await async_client.crm.extensions.calling.update_url_format(
            app_id=0,
            url_to_retrieve_authed_recording="urlToRetrieveAuthedRecording",
        )
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_url_format(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.extensions.calling.with_raw_response.update_url_format(
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calling = await response.parse()
        assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_url_format(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.extensions.calling.with_streaming_response.update_url_format(
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calling = await response.parse()
            assert_matches_type(RecordingSettingsResponse, calling, path=["response"])

        assert cast(Any, response.is_closed) is True
