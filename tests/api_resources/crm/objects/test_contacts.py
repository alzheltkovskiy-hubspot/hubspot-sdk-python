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
)
from hubspot_sdk.pagination import SyncPage, AsyncPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        contact = client.crm.objects.contacts.create(
            properties={"foo": "string"},
        )
        assert_matches_type(CreatedResponseSimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        contact = client.crm.objects.contacts.create(
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
        assert_matches_type(CreatedResponseSimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.objects.contacts.with_raw_response.create(
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(CreatedResponseSimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.objects.contacts.with_streaming_response.create(
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(CreatedResponseSimplePublicObject, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        contact = client.crm.objects.contacts.update(
            contact_id="contactId",
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.crm.objects.contacts.with_raw_response.update(
            contact_id="contactId",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(SimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.crm.objects.contacts.with_streaming_response.update(
            contact_id="contactId",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(SimplePublicObject, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.crm.objects.contacts.with_raw_response.update(
                contact_id="",
                properties={"foo": "string"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        contact = client.crm.objects.contacts.list()
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        contact = client.crm.objects.contacts.list(
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.objects.contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.crm.objects.contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(SyncPage[SimplePublicObjectWithAssociations], contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        contact = client.crm.objects.contacts.delete(
            "contactId",
        )
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.objects.contacts.with_raw_response.delete(
            "contactId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.objects.contacts.with_streaming_response.delete(
            "contactId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.crm.objects.contacts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_merge(self, client: HubSpot) -> None:
        contact = client.crm.objects.contacts.merge(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )
        assert_matches_type(SimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_merge(self, client: HubSpot) -> None:
        response = client.crm.objects.contacts.with_raw_response.merge(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(SimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_merge(self, client: HubSpot) -> None:
        with client.crm.objects.contacts.with_streaming_response.merge(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(SimplePublicObject, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_purge(self, client: HubSpot) -> None:
        contact = client.crm.objects.contacts.purge(
            object_id="objectId",
        )
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_purge_with_all_params(self, client: HubSpot) -> None:
        contact = client.crm.objects.contacts.purge(
            object_id="objectId",
            id_property="idProperty",
        )
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_purge(self, client: HubSpot) -> None:
        response = client.crm.objects.contacts.with_raw_response.purge(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_purge(self, client: HubSpot) -> None:
        with client.crm.objects.contacts.with_streaming_response.purge(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read(self, client: HubSpot) -> None:
        contact = client.crm.objects.contacts.read(
            contact_id="contactId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_with_all_params(self, client: HubSpot) -> None:
        contact = client.crm.objects.contacts.read(
            contact_id="contactId",
            archived=True,
            associations=["string"],
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: HubSpot) -> None:
        response = client.crm.objects.contacts.with_raw_response.read(
            contact_id="contactId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: HubSpot) -> None:
        with client.crm.objects.contacts.with_streaming_response.read(
            contact_id="contactId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.crm.objects.contacts.with_raw_response.read(
                contact_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: HubSpot) -> None:
        contact = client.crm.objects.contacts.search()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: HubSpot) -> None:
        contact = client.crm.objects.contacts.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: HubSpot) -> None:
        response = client.crm.objects.contacts.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: HubSpot) -> None:
        with client.crm.objects.contacts.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, contact, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        contact = await async_client.crm.objects.contacts.create(
            properties={"foo": "string"},
        )
        assert_matches_type(CreatedResponseSimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        contact = await async_client.crm.objects.contacts.create(
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
        assert_matches_type(CreatedResponseSimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.contacts.with_raw_response.create(
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(CreatedResponseSimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.contacts.with_streaming_response.create(
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(CreatedResponseSimplePublicObject, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        contact = await async_client.crm.objects.contacts.update(
            contact_id="contactId",
            properties={"foo": "string"},
        )
        assert_matches_type(SimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.contacts.with_raw_response.update(
            contact_id="contactId",
            properties={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(SimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.contacts.with_streaming_response.update(
            contact_id="contactId",
            properties={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(SimplePublicObject, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.crm.objects.contacts.with_raw_response.update(
                contact_id="",
                properties={"foo": "string"},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        contact = await async_client.crm.objects.contacts.list()
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        contact = await async_client.crm.objects.contacts.list(
            after="after",
            archived=True,
            associations=["string"],
            limit=0,
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.contacts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.contacts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(AsyncPage[SimplePublicObjectWithAssociations], contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        contact = await async_client.crm.objects.contacts.delete(
            "contactId",
        )
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.contacts.with_raw_response.delete(
            "contactId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.contacts.with_streaming_response.delete(
            "contactId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.crm.objects.contacts.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_merge(self, async_client: AsyncHubSpot) -> None:
        contact = await async_client.crm.objects.contacts.merge(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )
        assert_matches_type(SimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_merge(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.contacts.with_raw_response.merge(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(SimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_merge(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.contacts.with_streaming_response.merge(
            object_id_to_merge="objectIdToMerge",
            primary_object_id="primaryObjectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(SimplePublicObject, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_purge(self, async_client: AsyncHubSpot) -> None:
        contact = await async_client.crm.objects.contacts.purge(
            object_id="objectId",
        )
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_purge_with_all_params(self, async_client: AsyncHubSpot) -> None:
        contact = await async_client.crm.objects.contacts.purge(
            object_id="objectId",
            id_property="idProperty",
        )
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_purge(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.contacts.with_raw_response.purge(
            object_id="objectId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert contact is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_purge(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.contacts.with_streaming_response.purge(
            object_id="objectId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncHubSpot) -> None:
        contact = await async_client.crm.objects.contacts.read(
            contact_id="contactId",
        )
        assert_matches_type(SimplePublicObjectWithAssociations, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncHubSpot) -> None:
        contact = await async_client.crm.objects.contacts.read(
            contact_id="contactId",
            archived=True,
            associations=["string"],
            properties=["string"],
            properties_with_history=["string"],
        )
        assert_matches_type(SimplePublicObjectWithAssociations, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.contacts.with_raw_response.read(
            contact_id="contactId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(SimplePublicObjectWithAssociations, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.contacts.with_streaming_response.read(
            contact_id="contactId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(SimplePublicObjectWithAssociations, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.crm.objects.contacts.with_raw_response.read(
                contact_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubSpot) -> None:
        contact = await async_client.crm.objects.contacts.search()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubSpot) -> None:
        contact = await async_client.crm.objects.contacts.search(
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
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.contacts.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(CollectionResponseWithTotalSimplePublicObject, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.contacts.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(CollectionResponseWithTotalSimplePublicObject, contact, path=["response"])

        assert cast(Any, response.is_closed) is True
