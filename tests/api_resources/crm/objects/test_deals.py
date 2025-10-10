# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm import (
    SimplePublicObject,
    CreatedResponseSimplePublicObject,
    SimplePublicObjectWithAssociations,
    CollectionResponseWithTotalSimplePublicObject,
    CollectionResponseSimplePublicObjectWithAssociations,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_by_object_type_id(self, client: HubSpot) -> None:
        deal = client.crm.objects.deals.create_by_object_type_id(
            properties={"foo": "string"},
        )
        assert_matches_type(CreatedResponseSimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_by_object_type_id_with_all_params(self, client: HubSpot) -> None:
        deal = client.crm.objects.deals.create_by_object_type_id(
            properties={"foo": "string"},
            associations=[
                {
                    "to": {"id": "id"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(CreatedResponseSimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_by_object_type_id(self, client: HubSpot) -> None:
        response = client.crm.objects.deals.with_raw_response.create_by_object_type_id(
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(CreatedResponseSimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_by_object_type_id(self, client: HubSpot) -> None:
        with client.crm.objects.deals.with_streaming_response.create_by_object_type_id(
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(CreatedResponseSimplePublicObject, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_by_object_type_id(self, client: HubSpot) -> None:
        deal = client.crm.objects.deals.delete_by_object_type_id(
            "dealId",
        )
        assert deal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_by_object_type_id(self, client: HubSpot) -> None:
        response = client.crm.objects.deals.with_raw_response.delete_by_object_type_id(
            "dealId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert deal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_by_object_type_id(self, client: HubSpot) -> None:
        with client.crm.objects.deals.with_streaming_response.delete_by_object_type_id(
            "dealId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert deal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_by_object_type_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deal_id` but received ''"):
            client.crm.objects.deals.with_raw_response.delete_by_object_type_id(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_object_type_id(self, client: HubSpot) -> None:
        deal = client.crm.objects.deals.get_by_object_type_id(
            deal_id="dealId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_object_type_id_with_all_params(self, client: HubSpot) -> None:
        deal = client.crm.objects.deals.get_by_object_type_id(
            deal_id="dealId",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_object_type_id(self, client: HubSpot) -> None:
        response = client.crm.objects.deals.with_raw_response.get_by_object_type_id(
            deal_id="dealId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_object_type_id(self, client: HubSpot) -> None:
        with client.crm.objects.deals.with_streaming_response.get_by_object_type_id(
            deal_id="dealId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_by_object_type_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deal_id` but received ''"):
            client.crm.objects.deals.with_raw_response.get_by_object_type_id(
                deal_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_by_object_type_id(self, client: HubSpot) -> None:
        deal = client.crm.objects.deals.list_by_object_type_id()
        assert_matches_type(CollectionResponseSimplePublicObjectWithAssociations, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_by_object_type_id_with_all_params(self, client: HubSpot) -> None:
        deal = client.crm.objects.deals.list_by_object_type_id(
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(CollectionResponseSimplePublicObjectWithAssociations, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_by_object_type_id(self, client: HubSpot) -> None:
        response = client.crm.objects.deals.with_raw_response.list_by_object_type_id()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(CollectionResponseSimplePublicObjectWithAssociations, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_by_object_type_id(self, client: HubSpot) -> None:
        with client.crm.objects.deals.with_streaming_response.list_by_object_type_id() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(CollectionResponseSimplePublicObjectWithAssociations, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_merge_by_object_type_id(self, client: HubSpot) -> None:
        deal = client.crm.objects.deals.merge_by_object_type_id(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )
        assert_matches_type(SimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_merge_by_object_type_id(self, client: HubSpot) -> None:
        response = client.crm.objects.deals.with_raw_response.merge_by_object_type_id(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(SimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_merge_by_object_type_id(self, client: HubSpot) -> None:
        with client.crm.objects.deals.with_streaming_response.merge_by_object_type_id(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(SimplePublicObject, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_by_object_type_id(self, client: HubSpot) -> None:
        deal = client.crm.objects.deals.search_by_object_type_id()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_by_object_type_id_with_all_params(self, client: HubSpot) -> None:
        deal = client.crm.objects.deals.search_by_object_type_id(
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "EQ",
                            "property_name": "propertyName",
                            "high_value": "highValue",
                            "value": "value",
                            "values": ["string"],
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            query="query",
            sorts=["string"],
        )
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search_by_object_type_id(self, client: HubSpot) -> None:
        response = client.crm.objects.deals.with_raw_response.search_by_object_type_id()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search_by_object_type_id(self, client: HubSpot) -> None:
        with client.crm.objects.deals.with_streaming_response.search_by_object_type_id() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_by_object_type_id(self, client: HubSpot) -> None:
        deal = client.crm.objects.deals.update_by_object_type_id(
            deal_id="dealId",
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_by_object_type_id_with_all_params(self, client: HubSpot) -> None:
        deal = client.crm.objects.deals.update_by_object_type_id(
            deal_id="dealId",
            properties={"foo": "string"},
            id_property="idProperty",
        )
        assert_matches_type(SimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_by_object_type_id(self, client: HubSpot) -> None:
        response = client.crm.objects.deals.with_raw_response.update_by_object_type_id(
            deal_id="dealId",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = response.parse()
        assert_matches_type(SimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_by_object_type_id(self, client: HubSpot) -> None:
        with client.crm.objects.deals.with_streaming_response.update_by_object_type_id(
            deal_id="dealId",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = response.parse()
            assert_matches_type(SimplePublicObject, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_by_object_type_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deal_id` but received ''"):
            client.crm.objects.deals.with_raw_response.update_by_object_type_id(
                deal_id="",
                properties={"foo": "string"},
            )


class TestAsyncDeals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        deal = await async_client.crm.objects.deals.create_by_object_type_id(
            properties={"foo": "string"},
        )
        assert_matches_type(CreatedResponseSimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_by_object_type_id_with_all_params(self, async_client: AsyncHubSpot) -> None:
        deal = await async_client.crm.objects.deals.create_by_object_type_id(
            properties={"foo": "string"},
            associations=[
                {
                    "to": {"id": "id"},
                    "types": [
                        {
                            "association_category": "HUBSPOT_DEFINED",
                            "association_type_id": 0,
                        }
                    ],
                }
            ],
        )
        assert_matches_type(CreatedResponseSimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.deals.with_raw_response.create_by_object_type_id(
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(CreatedResponseSimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.deals.with_streaming_response.create_by_object_type_id(
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(CreatedResponseSimplePublicObject, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        deal = await async_client.crm.objects.deals.delete_by_object_type_id(
            "dealId",
        )
        assert deal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.deals.with_raw_response.delete_by_object_type_id(
            "dealId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert deal is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.deals.with_streaming_response.delete_by_object_type_id(
            "dealId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert deal is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deal_id` but received ''"):
            await async_client.crm.objects.deals.with_raw_response.delete_by_object_type_id(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        deal = await async_client.crm.objects.deals.get_by_object_type_id(
            deal_id="dealId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_object_type_id_with_all_params(self, async_client: AsyncHubSpot) -> None:
        deal = await async_client.crm.objects.deals.get_by_object_type_id(
            deal_id="dealId",
            archived=True,
            associations=["string"],
            id_property="idProperty",
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.deals.with_raw_response.get_by_object_type_id(
            deal_id="dealId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.deals.with_streaming_response.get_by_object_type_id(
            deal_id="dealId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deal_id` but received ''"):
            await async_client.crm.objects.deals.with_raw_response.get_by_object_type_id(
                deal_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        deal = await async_client.crm.objects.deals.list_by_object_type_id()
        assert_matches_type(CollectionResponseSimplePublicObjectWithAssociations, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_by_object_type_id_with_all_params(self, async_client: AsyncHubSpot) -> None:
        deal = await async_client.crm.objects.deals.list_by_object_type_id(
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(CollectionResponseSimplePublicObjectWithAssociations, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.deals.with_raw_response.list_by_object_type_id()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(CollectionResponseSimplePublicObjectWithAssociations, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.deals.with_streaming_response.list_by_object_type_id() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(CollectionResponseSimplePublicObjectWithAssociations, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_merge_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        deal = await async_client.crm.objects.deals.merge_by_object_type_id(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )
        assert_matches_type(SimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_merge_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.deals.with_raw_response.merge_by_object_type_id(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(SimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_merge_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.deals.with_streaming_response.merge_by_object_type_id(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(SimplePublicObject, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        deal = await async_client.crm.objects.deals.search_by_object_type_id()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_by_object_type_id_with_all_params(self, async_client: AsyncHubSpot) -> None:
        deal = await async_client.crm.objects.deals.search_by_object_type_id(
            after="after",
            filter_groups=[
                {
                    "filters": [
                        {
                            "operator": "EQ",
                            "property_name": "propertyName",
                            "high_value": "highValue",
                            "value": "value",
                            "values": ["string"],
                        }
                    ]
                }
            ],
            limit=0,
            properties=["string"],
            query="query",
            sorts=["string"],
        )
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.deals.with_raw_response.search_by_object_type_id()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.deals.with_streaming_response.search_by_object_type_id() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        deal = await async_client.crm.objects.deals.update_by_object_type_id(
            deal_id="dealId",
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_by_object_type_id_with_all_params(self, async_client: AsyncHubSpot) -> None:
        deal = await async_client.crm.objects.deals.update_by_object_type_id(
            deal_id="dealId",
            properties={"foo": "string"},
            id_property="idProperty",
        )
        assert_matches_type(SimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.deals.with_raw_response.update_by_object_type_id(
            deal_id="dealId",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deal = await response.parse()
        assert_matches_type(SimplePublicObject, deal, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.deals.with_streaming_response.update_by_object_type_id(
            deal_id="dealId",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deal = await response.parse()
            assert_matches_type(SimplePublicObject, deal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_by_object_type_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `deal_id` but received ''"):
            await async_client.crm.objects.deals.with_raw_response.update_by_object_type_id(
                deal_id="",
                properties={"foo": "string"},
            )
