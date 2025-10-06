# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.conversations import PublicConversationsMessage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        message = client.conversations.custom_channels.messages.create(
            channel_id="channelId",
            attachments=[
                {
                    "file_id": "fileId",
                    "type": "FILE",
                }
            ],
            channel_account_id="channelAccountId",
            integration_thread_id="integrationThreadId",
            message_direction="INCOMING",
            recipients=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    }
                }
            ],
            senders=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    }
                }
            ],
            text="text",
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        message = client.conversations.custom_channels.messages.create(
            channel_id="channelId",
            attachments=[
                {
                    "file_id": "fileId",
                    "type": "FILE",
                    "file_usage_type": "fileUsageType",
                }
            ],
            channel_account_id="channelAccountId",
            integration_thread_id="integrationThreadId",
            message_direction="INCOMING",
            recipients=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    },
                    "name": "name",
                }
            ],
            senders=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    },
                    "name": "name",
                }
            ],
            text="text",
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            in_reply_to_id="inReplyToId",
            integration_idempotency_id="integrationIdempotencyId",
            pre_resolved_contacts={
                "contacts": [
                    {
                        "contact_properties_leading_to_match": ["string"],
                        "contact_vid": 0,
                    }
                ]
            },
            rich_text="richText",
        )
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.conversations.custom_channels.messages.with_raw_response.create(
            channel_id="channelId",
            attachments=[
                {
                    "file_id": "fileId",
                    "type": "FILE",
                }
            ],
            channel_account_id="channelAccountId",
            integration_thread_id="integrationThreadId",
            message_direction="INCOMING",
            recipients=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    }
                }
            ],
            senders=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    }
                }
            ],
            text="text",
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.conversations.custom_channels.messages.with_streaming_response.create(
            channel_id="channelId",
            attachments=[
                {
                    "file_id": "fileId",
                    "type": "FILE",
                }
            ],
            channel_account_id="channelAccountId",
            integration_thread_id="integrationThreadId",
            message_direction="INCOMING",
            recipients=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    }
                }
            ],
            senders=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    }
                }
            ],
            text="text",
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(PublicConversationsMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.conversations.custom_channels.messages.with_raw_response.create(
                channel_id="",
                attachments=[
                    {
                        "file_id": "fileId",
                        "type": "FILE",
                    }
                ],
                channel_account_id="channelAccountId",
                integration_thread_id="integrationThreadId",
                message_direction="INCOMING",
                recipients=[
                    {
                        "delivery_identifier": {
                            "type": "type",
                            "value": "value",
                        }
                    }
                ],
                senders=[
                    {
                        "delivery_identifier": {
                            "type": "type",
                            "value": "value",
                        }
                    }
                ],
                text="text",
                timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        message = client.conversations.custom_channels.messages.get(
            message_id="messageId",
            channel_id="channelId",
        )
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.conversations.custom_channels.messages.with_raw_response.get(
            message_id="messageId",
            channel_id="channelId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.conversations.custom_channels.messages.with_streaming_response.get(
            message_id="messageId",
            channel_id="channelId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(PublicConversationsMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.conversations.custom_channels.messages.with_raw_response.get(
                message_id="messageId",
                channel_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.conversations.custom_channels.messages.with_raw_response.get(
                message_id="",
                channel_id="channelId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_status(self, client: HubSpot) -> None:
        message = client.conversations.custom_channels.messages.update_status(
            message_id="messageId",
            channel_id="channelId",
            status_type="SENT",
        )
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_status_with_all_params(self, client: HubSpot) -> None:
        message = client.conversations.custom_channels.messages.update_status(
            message_id="messageId",
            channel_id="channelId",
            status_type="SENT",
            error_message="errorMessage",
        )
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_status(self, client: HubSpot) -> None:
        response = client.conversations.custom_channels.messages.with_raw_response.update_status(
            message_id="messageId",
            channel_id="channelId",
            status_type="SENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_status(self, client: HubSpot) -> None:
        with client.conversations.custom_channels.messages.with_streaming_response.update_status(
            message_id="messageId",
            channel_id="channelId",
            status_type="SENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(PublicConversationsMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_status(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            client.conversations.custom_channels.messages.with_raw_response.update_status(
                message_id="messageId",
                channel_id="",
                status_type="SENT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.conversations.custom_channels.messages.with_raw_response.update_status(
                message_id="",
                channel_id="channelId",
                status_type="SENT",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        message = await async_client.conversations.custom_channels.messages.create(
            channel_id="channelId",
            attachments=[
                {
                    "file_id": "fileId",
                    "type": "FILE",
                }
            ],
            channel_account_id="channelAccountId",
            integration_thread_id="integrationThreadId",
            message_direction="INCOMING",
            recipients=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    }
                }
            ],
            senders=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    }
                }
            ],
            text="text",
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        message = await async_client.conversations.custom_channels.messages.create(
            channel_id="channelId",
            attachments=[
                {
                    "file_id": "fileId",
                    "type": "FILE",
                    "file_usage_type": "fileUsageType",
                }
            ],
            channel_account_id="channelAccountId",
            integration_thread_id="integrationThreadId",
            message_direction="INCOMING",
            recipients=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    },
                    "name": "name",
                }
            ],
            senders=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    },
                    "name": "name",
                }
            ],
            text="text",
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            in_reply_to_id="inReplyToId",
            integration_idempotency_id="integrationIdempotencyId",
            pre_resolved_contacts={
                "contacts": [
                    {
                        "contact_properties_leading_to_match": ["string"],
                        "contact_vid": 0,
                    }
                ]
            },
            rich_text="richText",
        )
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.conversations.custom_channels.messages.with_raw_response.create(
            channel_id="channelId",
            attachments=[
                {
                    "file_id": "fileId",
                    "type": "FILE",
                }
            ],
            channel_account_id="channelAccountId",
            integration_thread_id="integrationThreadId",
            message_direction="INCOMING",
            recipients=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    }
                }
            ],
            senders=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    }
                }
            ],
            text="text",
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.conversations.custom_channels.messages.with_streaming_response.create(
            channel_id="channelId",
            attachments=[
                {
                    "file_id": "fileId",
                    "type": "FILE",
                }
            ],
            channel_account_id="channelAccountId",
            integration_thread_id="integrationThreadId",
            message_direction="INCOMING",
            recipients=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    }
                }
            ],
            senders=[
                {
                    "delivery_identifier": {
                        "type": "type",
                        "value": "value",
                    }
                }
            ],
            text="text",
            timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(PublicConversationsMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.conversations.custom_channels.messages.with_raw_response.create(
                channel_id="",
                attachments=[
                    {
                        "file_id": "fileId",
                        "type": "FILE",
                    }
                ],
                channel_account_id="channelAccountId",
                integration_thread_id="integrationThreadId",
                message_direction="INCOMING",
                recipients=[
                    {
                        "delivery_identifier": {
                            "type": "type",
                            "value": "value",
                        }
                    }
                ],
                senders=[
                    {
                        "delivery_identifier": {
                            "type": "type",
                            "value": "value",
                        }
                    }
                ],
                text="text",
                timestamp=parse_datetime("2019-12-27T18:11:19.117Z"),
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        message = await async_client.conversations.custom_channels.messages.get(
            message_id="messageId",
            channel_id="channelId",
        )
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.conversations.custom_channels.messages.with_raw_response.get(
            message_id="messageId",
            channel_id="channelId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.conversations.custom_channels.messages.with_streaming_response.get(
            message_id="messageId",
            channel_id="channelId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(PublicConversationsMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.conversations.custom_channels.messages.with_raw_response.get(
                message_id="messageId",
                channel_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.conversations.custom_channels.messages.with_raw_response.get(
                message_id="",
                channel_id="channelId",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_status(self, async_client: AsyncHubSpot) -> None:
        message = await async_client.conversations.custom_channels.messages.update_status(
            message_id="messageId",
            channel_id="channelId",
            status_type="SENT",
        )
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_status_with_all_params(self, async_client: AsyncHubSpot) -> None:
        message = await async_client.conversations.custom_channels.messages.update_status(
            message_id="messageId",
            channel_id="channelId",
            status_type="SENT",
            error_message="errorMessage",
        )
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.conversations.custom_channels.messages.with_raw_response.update_status(
            message_id="messageId",
            channel_id="channelId",
            status_type="SENT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(PublicConversationsMessage, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncHubSpot) -> None:
        async with async_client.conversations.custom_channels.messages.with_streaming_response.update_status(
            message_id="messageId",
            channel_id="channelId",
            status_type="SENT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(PublicConversationsMessage, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel_id` but received ''"):
            await async_client.conversations.custom_channels.messages.with_raw_response.update_status(
                message_id="messageId",
                channel_id="",
                status_type="SENT",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.conversations.custom_channels.messages.with_raw_response.update_status(
                message_id="",
                channel_id="channelId",
                status_type="SENT",
            )
