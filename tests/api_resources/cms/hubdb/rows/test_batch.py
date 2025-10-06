# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.cms import BatchResponseHubDBTableRowV3

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace(self, client: HubSpot) -> None:
        batch = client.cms.hubdb.rows.batch.replace(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: HubSpot) -> None:
        response = client.cms.hubdb.rows.batch.with_raw_response.replace(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: HubSpot) -> None:
        with client.cms.hubdb.rows.batch.with_streaming_response.replace(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.rows.batch.with_raw_response.replace(
                table_id_or_name="",
                inputs=[
                    {
                        "id": "id",
                        "values": {"foo": {}},
                    }
                ],
            )


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncHubSpot) -> None:
        batch = await async_client.cms.hubdb.rows.batch.replace(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.rows.batch.with_raw_response.replace(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.rows.batch.with_streaming_response.replace(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.rows.batch.with_raw_response.replace(
                table_id_or_name="",
                inputs=[
                    {
                        "id": "id",
                        "values": {"foo": {}},
                    }
                ],
            )
