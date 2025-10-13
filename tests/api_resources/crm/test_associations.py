# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    BatchResponsePublicAssociation,
    BatchResponsePublicAssociationMulti,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssociations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        association = client.crm.associations.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )
        assert_matches_type(BatchResponsePublicAssociation, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.associations.with_raw_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert_matches_type(BatchResponsePublicAssociation, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.associations.with_streaming_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert_matches_type(BatchResponsePublicAssociation, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.with_raw_response.create(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.with_raw_response.create(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        association = client.crm.associations.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.associations.with_raw_response.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.associations.with_streaming_response.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.with_raw_response.delete(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.with_raw_response.delete(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read(self, client: HubSpot) -> None:
        association = client.crm.associations.read(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "37295"}],
        )
        assert_matches_type(BatchResponsePublicAssociationMulti, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: HubSpot) -> None:
        response = client.crm.associations.with_raw_response.read(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "37295"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = response.parse()
        assert_matches_type(BatchResponsePublicAssociationMulti, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: HubSpot) -> None:
        with client.crm.associations.with_streaming_response.read(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "37295"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = response.parse()
            assert_matches_type(BatchResponsePublicAssociationMulti, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            client.crm.associations.with_raw_response.read(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[{"id": "37295"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            client.crm.associations.with_raw_response.read(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[{"id": "37295"}],
            )


class TestAsyncAssociations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.associations.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )
        assert_matches_type(BatchResponsePublicAssociation, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.with_raw_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert_matches_type(BatchResponsePublicAssociation, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.with_streaming_response.create(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert_matches_type(BatchResponsePublicAssociation, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.create(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.create(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.associations.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.with_raw_response.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert association is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.with_streaming_response.delete(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[
                {
                    "from": {"id": "53628"},
                    "to": {"id": "12726"},
                    "type": "contact_to_company",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert association is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.delete(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.delete(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[
                    {
                        "from": {"id": "53628"},
                        "to": {"id": "12726"},
                        "type": "contact_to_company",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncHubSpot) -> None:
        association = await async_client.crm.associations.read(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "37295"}],
        )
        assert_matches_type(BatchResponsePublicAssociationMulti, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.associations.with_raw_response.read(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "37295"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        association = await response.parse()
        assert_matches_type(BatchResponsePublicAssociationMulti, association, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.associations.with_streaming_response.read(
            to_object_type="toObjectType",
            from_object_type="fromObjectType",
            inputs=[{"id": "37295"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            association = await response.parse()
            assert_matches_type(BatchResponsePublicAssociationMulti, association, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `from_object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.read(
                to_object_type="toObjectType",
                from_object_type="",
                inputs=[{"id": "37295"}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `to_object_type` but received ''"):
            await async_client.crm.associations.with_raw_response.read(
                to_object_type="",
                from_object_type="fromObjectType",
                inputs=[{"id": "37295"}],
            )
