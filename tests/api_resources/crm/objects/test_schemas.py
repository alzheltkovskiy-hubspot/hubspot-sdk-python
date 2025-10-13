# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types.crm.objects import (
    ObjectSchema,
    ObjectTypeDefinition,
    AssociationDefinition,
    CollectionResponseObjectSchemaNoPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchemas:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        schema = client.crm.objects.schemas.create(
            associated_objects=["CONTACT"],
            labels={},
            name="my_object",
            properties=[
                {
                    "field_type": "select",
                    "label": "My object property",
                    "name": "my_object_property",
                    "type": "enumeration",
                }
            ],
            required_properties=["my_object_property"],
        )
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        schema = client.crm.objects.schemas.create(
            associated_objects=["CONTACT"],
            labels={
                "plural": "My objects",
                "singular": "My object",
            },
            name="my_object",
            properties=[
                {
                    "field_type": "select",
                    "label": "My object property",
                    "name": "my_object_property",
                    "type": "enumeration",
                    "description": "description",
                    "display_order": 2,
                    "form_field": True,
                    "group_name": "my_object_information",
                    "has_unique_value": False,
                    "hidden": True,
                    "number_display_hint": "unformatted",
                    "options": [
                        {
                            "hidden": False,
                            "label": "Option A",
                            "value": "A",
                            "description": "Choice number one",
                            "display_order": 1,
                        },
                        {
                            "hidden": False,
                            "label": "Option B",
                            "value": "B",
                            "description": "Choice number two",
                            "display_order": 2,
                        },
                    ],
                    "option_sort_strategy": "DISPLAY_ORDER",
                    "referenced_object_type": "referencedObjectType",
                    "searchable_in_global_search": True,
                    "show_currency_symbol": True,
                    "text_display_hint": "unformatted_single_line",
                }
            ],
            required_properties=["my_object_property"],
            description="description",
            primary_display_property="my_object_property",
            searchable_properties=["string"],
            secondary_display_properties=["string"],
        )
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.objects.schemas.with_raw_response.create(
            associated_objects=["CONTACT"],
            labels={},
            name="my_object",
            properties=[
                {
                    "field_type": "select",
                    "label": "My object property",
                    "name": "my_object_property",
                    "type": "enumeration",
                }
            ],
            required_properties=["my_object_property"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.objects.schemas.with_streaming_response.create(
            associated_objects=["CONTACT"],
            labels={},
            name="my_object",
            properties=[
                {
                    "field_type": "select",
                    "label": "My object property",
                    "name": "my_object_property",
                    "type": "enumeration",
                }
            ],
            required_properties=["my_object_property"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(ObjectSchema, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        schema = client.crm.objects.schemas.update(
            object_type="objectType",
        )
        assert_matches_type(ObjectTypeDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        schema = client.crm.objects.schemas.update(
            object_type="objectType",
            clear_description=True,
            description="description",
            labels={
                "plural": "My objects",
                "singular": "My object",
            },
            primary_display_property="my_object_property",
            required_properties=["my_object_property"],
            restorable=True,
            searchable_properties=["my_object_property"],
            secondary_display_properties=["string"],
        )
        assert_matches_type(ObjectTypeDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.crm.objects.schemas.with_raw_response.update(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(ObjectTypeDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.crm.objects.schemas.with_streaming_response.update(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(ObjectTypeDefinition, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.schemas.with_raw_response.update(
                object_type="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        schema = client.crm.objects.schemas.list()
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        schema = client.crm.objects.schemas.list(
            archived=True,
        )
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.objects.schemas.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.crm.objects.schemas.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(CollectionResponseObjectSchemaNoPaging, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        schema = client.crm.objects.schemas.delete(
            object_type="objectType",
        )
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: HubSpot) -> None:
        schema = client.crm.objects.schemas.delete(
            object_type="objectType",
            archived=True,
        )
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.objects.schemas.with_raw_response.delete(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.objects.schemas.with_streaming_response.delete(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert schema is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.schemas.with_raw_response.delete(
                object_type="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_archive_association(self, client: HubSpot) -> None:
        schema = client.crm.objects.schemas.archive_association(
            association_identifier="associationIdentifier",
            object_type="objectType",
        )
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_archive_association(self, client: HubSpot) -> None:
        response = client.crm.objects.schemas.with_raw_response.archive_association(
            association_identifier="associationIdentifier",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_archive_association(self, client: HubSpot) -> None:
        with client.crm.objects.schemas.with_streaming_response.archive_association(
            association_identifier="associationIdentifier",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert schema is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_archive_association(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.schemas.with_raw_response.archive_association(
                association_identifier="associationIdentifier",
                object_type="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `association_identifier` but received ''"
        ):
            client.crm.objects.schemas.with_raw_response.archive_association(
                association_identifier="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_association(self, client: HubSpot) -> None:
        schema = client.crm.objects.schemas.create_association(
            object_type="objectType",
            from_object_type_id="2-123456",
            to_object_type_id="contact",
        )
        assert_matches_type(AssociationDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_association_with_all_params(self, client: HubSpot) -> None:
        schema = client.crm.objects.schemas.create_association(
            object_type="objectType",
            from_object_type_id="2-123456",
            to_object_type_id="contact",
            name="my_object_to_contact",
        )
        assert_matches_type(AssociationDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_association(self, client: HubSpot) -> None:
        response = client.crm.objects.schemas.with_raw_response.create_association(
            object_type="objectType",
            from_object_type_id="2-123456",
            to_object_type_id="contact",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(AssociationDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_association(self, client: HubSpot) -> None:
        with client.crm.objects.schemas.with_streaming_response.create_association(
            object_type="objectType",
            from_object_type_id="2-123456",
            to_object_type_id="contact",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(AssociationDefinition, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_association(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.schemas.with_raw_response.create_association(
                object_type="",
                from_object_type_id="2-123456",
                to_object_type_id="contact",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read(self, client: HubSpot) -> None:
        schema = client.crm.objects.schemas.read(
            "objectType",
        )
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: HubSpot) -> None:
        response = client.crm.objects.schemas.with_raw_response.read(
            "objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = response.parse()
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: HubSpot) -> None:
        with client.crm.objects.schemas.with_streaming_response.read(
            "objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = response.parse()
            assert_matches_type(ObjectSchema, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.objects.schemas.with_raw_response.read(
                "",
            )


class TestAsyncSchemas:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        schema = await async_client.crm.objects.schemas.create(
            associated_objects=["CONTACT"],
            labels={},
            name="my_object",
            properties=[
                {
                    "field_type": "select",
                    "label": "My object property",
                    "name": "my_object_property",
                    "type": "enumeration",
                }
            ],
            required_properties=["my_object_property"],
        )
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        schema = await async_client.crm.objects.schemas.create(
            associated_objects=["CONTACT"],
            labels={
                "plural": "My objects",
                "singular": "My object",
            },
            name="my_object",
            properties=[
                {
                    "field_type": "select",
                    "label": "My object property",
                    "name": "my_object_property",
                    "type": "enumeration",
                    "description": "description",
                    "display_order": 2,
                    "form_field": True,
                    "group_name": "my_object_information",
                    "has_unique_value": False,
                    "hidden": True,
                    "number_display_hint": "unformatted",
                    "options": [
                        {
                            "hidden": False,
                            "label": "Option A",
                            "value": "A",
                            "description": "Choice number one",
                            "display_order": 1,
                        },
                        {
                            "hidden": False,
                            "label": "Option B",
                            "value": "B",
                            "description": "Choice number two",
                            "display_order": 2,
                        },
                    ],
                    "option_sort_strategy": "DISPLAY_ORDER",
                    "referenced_object_type": "referencedObjectType",
                    "searchable_in_global_search": True,
                    "show_currency_symbol": True,
                    "text_display_hint": "unformatted_single_line",
                }
            ],
            required_properties=["my_object_property"],
            description="description",
            primary_display_property="my_object_property",
            searchable_properties=["string"],
            secondary_display_properties=["string"],
        )
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.schemas.with_raw_response.create(
            associated_objects=["CONTACT"],
            labels={},
            name="my_object",
            properties=[
                {
                    "field_type": "select",
                    "label": "My object property",
                    "name": "my_object_property",
                    "type": "enumeration",
                }
            ],
            required_properties=["my_object_property"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.schemas.with_streaming_response.create(
            associated_objects=["CONTACT"],
            labels={},
            name="my_object",
            properties=[
                {
                    "field_type": "select",
                    "label": "My object property",
                    "name": "my_object_property",
                    "type": "enumeration",
                }
            ],
            required_properties=["my_object_property"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(ObjectSchema, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        schema = await async_client.crm.objects.schemas.update(
            object_type="objectType",
        )
        assert_matches_type(ObjectTypeDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        schema = await async_client.crm.objects.schemas.update(
            object_type="objectType",
            clear_description=True,
            description="description",
            labels={
                "plural": "My objects",
                "singular": "My object",
            },
            primary_display_property="my_object_property",
            required_properties=["my_object_property"],
            restorable=True,
            searchable_properties=["my_object_property"],
            secondary_display_properties=["string"],
        )
        assert_matches_type(ObjectTypeDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.schemas.with_raw_response.update(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(ObjectTypeDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.schemas.with_streaming_response.update(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(ObjectTypeDefinition, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.schemas.with_raw_response.update(
                object_type="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        schema = await async_client.crm.objects.schemas.list()
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        schema = await async_client.crm.objects.schemas.list(
            archived=True,
        )
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.schemas.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(CollectionResponseObjectSchemaNoPaging, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.schemas.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(CollectionResponseObjectSchemaNoPaging, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        schema = await async_client.crm.objects.schemas.delete(
            object_type="objectType",
        )
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncHubSpot) -> None:
        schema = await async_client.crm.objects.schemas.delete(
            object_type="objectType",
            archived=True,
        )
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.schemas.with_raw_response.delete(
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.schemas.with_streaming_response.delete(
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert schema is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.schemas.with_raw_response.delete(
                object_type="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_archive_association(self, async_client: AsyncHubSpot) -> None:
        schema = await async_client.crm.objects.schemas.archive_association(
            association_identifier="associationIdentifier",
            object_type="objectType",
        )
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_archive_association(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.schemas.with_raw_response.archive_association(
            association_identifier="associationIdentifier",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert schema is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_archive_association(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.schemas.with_streaming_response.archive_association(
            association_identifier="associationIdentifier",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert schema is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_archive_association(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.schemas.with_raw_response.archive_association(
                association_identifier="associationIdentifier",
                object_type="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `association_identifier` but received ''"
        ):
            await async_client.crm.objects.schemas.with_raw_response.archive_association(
                association_identifier="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_association(self, async_client: AsyncHubSpot) -> None:
        schema = await async_client.crm.objects.schemas.create_association(
            object_type="objectType",
            from_object_type_id="2-123456",
            to_object_type_id="contact",
        )
        assert_matches_type(AssociationDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_association_with_all_params(self, async_client: AsyncHubSpot) -> None:
        schema = await async_client.crm.objects.schemas.create_association(
            object_type="objectType",
            from_object_type_id="2-123456",
            to_object_type_id="contact",
            name="my_object_to_contact",
        )
        assert_matches_type(AssociationDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_association(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.schemas.with_raw_response.create_association(
            object_type="objectType",
            from_object_type_id="2-123456",
            to_object_type_id="contact",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(AssociationDefinition, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_association(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.schemas.with_streaming_response.create_association(
            object_type="objectType",
            from_object_type_id="2-123456",
            to_object_type_id="contact",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(AssociationDefinition, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_association(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.schemas.with_raw_response.create_association(
                object_type="",
                from_object_type_id="2-123456",
                to_object_type_id="contact",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncHubSpot) -> None:
        schema = await async_client.crm.objects.schemas.read(
            "objectType",
        )
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.objects.schemas.with_raw_response.read(
            "objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schema = await response.parse()
        assert_matches_type(ObjectSchema, schema, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.objects.schemas.with_streaming_response.read(
            "objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schema = await response.parse()
            assert_matches_type(ObjectSchema, schema, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.objects.schemas.with_raw_response.read(
                "",
            )
