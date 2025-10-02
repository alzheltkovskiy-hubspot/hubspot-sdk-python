# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types import (
    WebhooksSettingsResponse,
    WebhooksSubscriptionResponse,
    WebhooksSubscriptionListResponse,
    WebhooksBatchResponseSubscriptionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        webhook = client.webhooks.create(
            app_id=0,
            event_type="contact.propertyChange",
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        webhook = client.webhooks.create(
            app_id=0,
            event_type="contact.propertyChange",
            active=True,
            object_type_id="objectTypeId",
            property_name="propertyName",
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.create(
            app_id=0,
            event_type="contact.propertyChange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.create(
            app_id=0,
            event_type="contact.propertyChange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        webhook = client.webhooks.update(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        webhook = client.webhooks.update(
            subscription_id=0,
            app_id=0,
            active=True,
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.update(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.update(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        webhook = client.webhooks.list(
            0,
        )
        assert_matches_type(WebhooksSubscriptionListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksSubscriptionListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksSubscriptionListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        webhook = client.webhooks.delete(
            subscription_id=0,
            app_id=0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.delete(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.delete(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clear(self, client: HubSpot) -> None:
        webhook = client.webhooks.clear(
            0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clear(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.clear(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clear(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.clear(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_configure(self, client: HubSpot) -> None:
        webhook = client.webhooks.configure(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )
        assert_matches_type(WebhooksSettingsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_configure(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.configure(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksSettingsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_configure(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.configure(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksSettingsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read(self, client: HubSpot) -> None:
        webhook = client.webhooks.read(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.read(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.read(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch(self, client: HubSpot) -> None:
        webhook = client.webhooks.update_batch(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )
        assert_matches_type(WebhooksBatchResponseSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_batch(self, client: HubSpot) -> None:
        response = client.webhooks.with_raw_response.update_batch(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhooksBatchResponseSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_batch(self, client: HubSpot) -> None:
        with client.webhooks.with_streaming_response.update_batch(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhooksBatchResponseSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.create(
            app_id=0,
            event_type="contact.propertyChange",
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.create(
            app_id=0,
            event_type="contact.propertyChange",
            active=True,
            object_type_id="objectTypeId",
            property_name="propertyName",
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.create(
            app_id=0,
            event_type="contact.propertyChange",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.create(
            app_id=0,
            event_type="contact.propertyChange",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.update(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.update(
            subscription_id=0,
            app_id=0,
            active=True,
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.update(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.update(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.list(
            0,
        )
        assert_matches_type(WebhooksSubscriptionListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksSubscriptionListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksSubscriptionListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.delete(
            subscription_id=0,
            app_id=0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.delete(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.delete(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clear(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.clear(
            0,
        )
        assert webhook is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clear(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.clear(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clear(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.clear(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_configure(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.configure(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )
        assert_matches_type(WebhooksSettingsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_configure(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.configure(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksSettingsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_configure(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.configure(
            app_id=0,
            target_url="targetUrl",
            throttling={"max_concurrent_requests": 0},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksSettingsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.read(
            subscription_id=0,
            app_id=0,
        )
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.read(
            subscription_id=0,
            app_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.read(
            subscription_id=0,
            app_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch(self, async_client: AsyncHubSpot) -> None:
        webhook = await async_client.webhooks.update_batch(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )
        assert_matches_type(WebhooksBatchResponseSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.webhooks.with_raw_response.update_batch(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhooksBatchResponseSubscriptionResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.webhooks.with_streaming_response.update_batch(
            app_id=0,
            inputs=[
                {
                    "id": 0,
                    "active": True,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhooksBatchResponseSubscriptionResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True
