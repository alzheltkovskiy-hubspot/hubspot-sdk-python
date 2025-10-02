# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.auth import AuthOAuthTokenResponseIf, AuthOAuthRefreshTokenInfoResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        oauth = client.auth.oauth.create()
        assert_matches_type(AuthOAuthTokenResponseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        oauth = client.auth.oauth.create(
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            grant_type="authorization_code",
            redirect_uri="redirect_uri",
            refresh_token="refresh_token",
        )
        assert_matches_type(AuthOAuthTokenResponseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.auth.oauth.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(AuthOAuthTokenResponseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.auth.oauth.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(AuthOAuthTokenResponseIf, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        oauth = client.auth.oauth.delete(
            "token",
        )
        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.auth.oauth.with_raw_response.delete(
            "token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.auth.oauth.with_streaming_response.delete(
            "token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert oauth is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.auth.oauth.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        oauth = client.auth.oauth.get(
            "token",
        )
        assert_matches_type(AuthOAuthRefreshTokenInfoResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.auth.oauth.with_raw_response.get(
            "token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(AuthOAuthRefreshTokenInfoResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.auth.oauth.with_streaming_response.get(
            "token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(AuthOAuthRefreshTokenInfoResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.auth.oauth.with_raw_response.get(
                "",
            )


class TestAsyncOAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        oauth = await async_client.auth.oauth.create()
        assert_matches_type(AuthOAuthTokenResponseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        oauth = await async_client.auth.oauth.create(
            client_id="client_id",
            client_secret="client_secret",
            code="code",
            grant_type="authorization_code",
            redirect_uri="redirect_uri",
            refresh_token="refresh_token",
        )
        assert_matches_type(AuthOAuthTokenResponseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.auth.oauth.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(AuthOAuthTokenResponseIf, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.auth.oauth.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(AuthOAuthTokenResponseIf, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        oauth = await async_client.auth.oauth.delete(
            "token",
        )
        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.auth.oauth.with_raw_response.delete(
            "token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert oauth is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.auth.oauth.with_streaming_response.delete(
            "token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert oauth is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.auth.oauth.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        oauth = await async_client.auth.oauth.get(
            "token",
        )
        assert_matches_type(AuthOAuthRefreshTokenInfoResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.auth.oauth.with_raw_response.get(
            "token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(AuthOAuthRefreshTokenInfoResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.auth.oauth.with_streaming_response.get(
            "token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(AuthOAuthRefreshTokenInfoResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.auth.oauth.with_raw_response.get(
                "",
            )
