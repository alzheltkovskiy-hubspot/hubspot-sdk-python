# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.marketing.subscriptions import (
    BatchResponsePublicStatus,
    ActionResponseWithResultsPublicStatus,
    BatchResponsePublicStatusBulkResponse,
    ActionResponseWithResultsPublicWideStatus,
    BatchResponsePublicWideStatusBulkResponse,
    BatchResponsePublicBulkOptOutFromAllResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatuses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            client.marketing.subscriptions.v4.statuses.with_raw_response.get(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_batch(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.get_batch(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_batch_with_all_params(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.get_batch(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
        )
        assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_batch(self, client: HubSpot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.get_batch(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_batch(self, client: HubSpot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.get_batch(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_unsubscribe_all_status(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_unsubscribe_all_status_with_all_params(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_unsubscribe_all_status(self, client: HubSpot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_unsubscribe_all_status(self, client: HubSpot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_unsubscribe_all_status(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            client.marketing.subscriptions.v4.statuses.with_raw_response.get_unsubscribe_all_status(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_unsubscribe_all_status_batch(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.get_unsubscribe_all_status_batch(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_unsubscribe_all_status_batch_with_all_params(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.get_unsubscribe_all_status_batch(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
        )
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_unsubscribe_all_status_batch(self, client: HubSpot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.get_unsubscribe_all_status_batch(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_unsubscribe_all_status_batch(self, client: HubSpot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.get_unsubscribe_all_status_batch(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.set(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="SUBSCRIBED",
            subscription_id=0,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_with_all_params(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.set(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="SUBSCRIBED",
            subscription_id=0,
            legal_basis="LEGITIMATE_INTEREST_PQL",
            legal_basis_explanation="legalBasisExplanation",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set(self, client: HubSpot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.set(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="SUBSCRIBED",
            subscription_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set(self, client: HubSpot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.set(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="SUBSCRIBED",
            subscription_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_set(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            client.marketing.subscriptions.v4.statuses.with_raw_response.set(
                subscriber_id_string="",
                channel="EMAIL",
                status_state="SUBSCRIBED",
                subscription_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unsubscribe_all(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unsubscribe_all_with_all_params(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unsubscribe_all(self, client: HubSpot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unsubscribe_all(self, client: HubSpot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unsubscribe_all(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            client.marketing.subscriptions.v4.statuses.with_raw_response.unsubscribe_all(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unsubscribe_all_batch(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.unsubscribe_all_batch(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unsubscribe_all_batch_with_all_params(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.unsubscribe_all_batch(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unsubscribe_all_batch(self, client: HubSpot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.unsubscribe_all_batch(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unsubscribe_all_batch(self, client: HubSpot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.unsubscribe_all_batch(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch(self, client: HubSpot) -> None:
        status = client.marketing.subscriptions.v4.statuses.update_batch(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "SUBSCRIBED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        )
        assert_matches_type(BatchResponsePublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_batch(self, client: HubSpot) -> None:
        response = client.marketing.subscriptions.v4.statuses.with_raw_response.update_batch(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "SUBSCRIBED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(BatchResponsePublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_batch(self, client: HubSpot) -> None:
        with client.marketing.subscriptions.v4.statuses.with_streaming_response.update_batch(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "SUBSCRIBED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(BatchResponsePublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatuses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.get(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            await async_client.marketing.subscriptions.v4.statuses.with_raw_response.get(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_batch(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.get_batch(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_batch_with_all_params(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.get_batch(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
        )
        assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.get_batch(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.get_batch(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(BatchResponsePublicStatusBulkResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_unsubscribe_all_status(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_unsubscribe_all_status_with_all_params(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_unsubscribe_all_status(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_unsubscribe_all_status(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.get_unsubscribe_all_status(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(ActionResponseWithResultsPublicWideStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_unsubscribe_all_status(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            await async_client.marketing.subscriptions.v4.statuses.with_raw_response.get_unsubscribe_all_status(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_unsubscribe_all_status_batch(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.get_unsubscribe_all_status_batch(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_unsubscribe_all_status_batch_with_all_params(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.get_unsubscribe_all_status_batch(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
        )
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_unsubscribe_all_status_batch(self, async_client: AsyncHubSpot) -> None:
        response = (
            await async_client.marketing.subscriptions.v4.statuses.with_raw_response.get_unsubscribe_all_status_batch(
                channel="EMAIL",
                inputs=["string"],
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_unsubscribe_all_status_batch(self, async_client: AsyncHubSpot) -> None:
        async with (
            async_client.marketing.subscriptions.v4.statuses.with_streaming_response.get_unsubscribe_all_status_batch(
                channel="EMAIL",
                inputs=["string"],
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(BatchResponsePublicWideStatusBulkResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.set(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="SUBSCRIBED",
            subscription_id=0,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_with_all_params(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.set(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="SUBSCRIBED",
            subscription_id=0,
            legal_basis="LEGITIMATE_INTEREST_PQL",
            legal_basis_explanation="legalBasisExplanation",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.set(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="SUBSCRIBED",
            subscription_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.set(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            status_state="SUBSCRIBED",
            subscription_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_set(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            await async_client.marketing.subscriptions.v4.statuses.with_raw_response.set(
                subscriber_id_string="",
                channel="EMAIL",
                status_state="SUBSCRIBED",
                subscription_id=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unsubscribe_all(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unsubscribe_all_with_all_params(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unsubscribe_all(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unsubscribe_all(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.unsubscribe_all(
            subscriber_id_string="subscriberIdString",
            channel="EMAIL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(ActionResponseWithResultsPublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unsubscribe_all(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscriber_id_string` but received ''"):
            await async_client.marketing.subscriptions.v4.statuses.with_raw_response.unsubscribe_all(
                subscriber_id_string="",
                channel="EMAIL",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unsubscribe_all_batch(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.unsubscribe_all_batch(
            channel="EMAIL",
            inputs=["string"],
        )
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unsubscribe_all_batch_with_all_params(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.unsubscribe_all_batch(
            channel="EMAIL",
            inputs=["string"],
            business_unit_id=0,
            verbose=True,
        )
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unsubscribe_all_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.unsubscribe_all_batch(
            channel="EMAIL",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unsubscribe_all_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.unsubscribe_all_batch(
            channel="EMAIL",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(BatchResponsePublicBulkOptOutFromAllResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch(self, async_client: AsyncHubSpot) -> None:
        status = await async_client.marketing.subscriptions.v4.statuses.update_batch(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "SUBSCRIBED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        )
        assert_matches_type(BatchResponsePublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.subscriptions.v4.statuses.with_raw_response.update_batch(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "SUBSCRIBED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(BatchResponsePublicStatus, status, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.subscriptions.v4.statuses.with_streaming_response.update_batch(
            inputs=[
                {
                    "channel": "EMAIL",
                    "status_state": "SUBSCRIBED",
                    "subscriber_id_string": "subscriberIdString",
                    "subscription_id": 0,
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(BatchResponsePublicStatus, status, path=["response"])

        assert cast(Any, response.is_closed) is True
