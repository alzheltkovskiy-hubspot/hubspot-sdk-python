# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types import Property
from hubspot_sdk.types.crm import (
    BatchResponseProperty,
    CreatedResponsePropertyGroup,
    CollectionResponsePropertyGroup,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProperties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        property = client.crm.properties.create(
            object_type="objectType",
            label="My Property Group",
            name="mypropertygroup",
        )
        assert_matches_type(CreatedResponsePropertyGroup, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        property = client.crm.properties.create(
            object_type="objectType",
            label="My Property Group",
            name="mypropertygroup",
            display_order=-1,
        )
        assert_matches_type(CreatedResponsePropertyGroup, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.crm.properties.with_raw_response.create(
            object_type="objectType",
            label="My Property Group",
            name="mypropertygroup",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(CreatedResponsePropertyGroup, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.crm.properties.with_streaming_response.create(
            object_type="objectType",
            label="My Property Group",
            name="mypropertygroup",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(CreatedResponsePropertyGroup, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.with_raw_response.create(
                object_type="",
                label="My Property Group",
                name="mypropertygroup",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        property = client.crm.properties.update(
            property_name="propertyName",
            object_type="objectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        property = client.crm.properties.update(
            property_name="propertyName",
            object_type="objectType",
            calculation_formula="calculationFormula",
            description="description",
            display_order=2,
            field_type="select",
            form_field=True,
            group_name="contactinformation",
            hidden=False,
            label="My Contact Property",
            options=[
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
            type="enumeration",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.crm.properties.with_raw_response.update(
            property_name="propertyName",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.crm.properties.with_streaming_response.update(
            property_name="propertyName",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.with_raw_response.update(
                property_name="propertyName",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.crm.properties.with_raw_response.update(
                property_name="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        property = client.crm.properties.list(
            "objectType",
        )
        assert_matches_type(CollectionResponsePropertyGroup, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.crm.properties.with_raw_response.list(
            "objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(CollectionResponsePropertyGroup, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.crm.properties.with_streaming_response.list(
            "objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(CollectionResponsePropertyGroup, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        property = client.crm.properties.delete(
            property_name="propertyName",
            object_type="objectType",
        )
        assert property is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.crm.properties.with_raw_response.delete(
            property_name="propertyName",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert property is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.crm.properties.with_streaming_response.delete(
            property_name="propertyName",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert property is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.with_raw_response.delete(
                property_name="propertyName",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.crm.properties.with_raw_response.delete(
                property_name="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_name(self, client: HubSpot) -> None:
        property = client.crm.properties.get_by_name(
            property_name="propertyName",
            object_type="objectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_name_with_all_params(self, client: HubSpot) -> None:
        property = client.crm.properties.get_by_name(
            property_name="propertyName",
            object_type="objectType",
            archived=True,
            properties="properties",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_name(self, client: HubSpot) -> None:
        response = client.crm.properties.with_raw_response.get_by_name(
            property_name="propertyName",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_name(self, client: HubSpot) -> None:
        with client.crm.properties.with_streaming_response.get_by_name(
            property_name="propertyName",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_by_name(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.with_raw_response.get_by_name(
                property_name="propertyName",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            client.crm.properties.with_raw_response.get_by_name(
                property_name="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read(self, client: HubSpot) -> None:
        property = client.crm.properties.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
        )
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_with_all_params(self, client: HubSpot) -> None:
        property = client.crm.properties.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
            data_sensitivity="non_sensitive",
        )
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: HubSpot) -> None:
        response = client.crm.properties.with_raw_response.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = response.parse()
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: HubSpot) -> None:
        with client.crm.properties.with_streaming_response.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = response.parse()
            assert_matches_type(BatchResponseProperty, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            client.crm.properties.with_raw_response.read(
                object_type="",
                archived=True,
                inputs=[{"name": "my_custom_property"}],
            )


class TestAsyncProperties:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        property = await async_client.crm.properties.create(
            object_type="objectType",
            label="My Property Group",
            name="mypropertygroup",
        )
        assert_matches_type(CreatedResponsePropertyGroup, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        property = await async_client.crm.properties.create(
            object_type="objectType",
            label="My Property Group",
            name="mypropertygroup",
            display_order=-1,
        )
        assert_matches_type(CreatedResponsePropertyGroup, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.properties.with_raw_response.create(
            object_type="objectType",
            label="My Property Group",
            name="mypropertygroup",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(CreatedResponsePropertyGroup, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.properties.with_streaming_response.create(
            object_type="objectType",
            label="My Property Group",
            name="mypropertygroup",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(CreatedResponsePropertyGroup, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.with_raw_response.create(
                object_type="",
                label="My Property Group",
                name="mypropertygroup",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        property = await async_client.crm.properties.update(
            property_name="propertyName",
            object_type="objectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        property = await async_client.crm.properties.update(
            property_name="propertyName",
            object_type="objectType",
            calculation_formula="calculationFormula",
            description="description",
            display_order=2,
            field_type="select",
            form_field=True,
            group_name="contactinformation",
            hidden=False,
            label="My Contact Property",
            options=[
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
            type="enumeration",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.properties.with_raw_response.update(
            property_name="propertyName",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.properties.with_streaming_response.update(
            property_name="propertyName",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.with_raw_response.update(
                property_name="propertyName",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.crm.properties.with_raw_response.update(
                property_name="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        property = await async_client.crm.properties.list(
            "objectType",
        )
        assert_matches_type(CollectionResponsePropertyGroup, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.properties.with_raw_response.list(
            "objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(CollectionResponsePropertyGroup, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.properties.with_streaming_response.list(
            "objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(CollectionResponsePropertyGroup, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        property = await async_client.crm.properties.delete(
            property_name="propertyName",
            object_type="objectType",
        )
        assert property is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.properties.with_raw_response.delete(
            property_name="propertyName",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert property is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.properties.with_streaming_response.delete(
            property_name="propertyName",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert property is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.with_raw_response.delete(
                property_name="propertyName",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.crm.properties.with_raw_response.delete(
                property_name="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_name(self, async_client: AsyncHubSpot) -> None:
        property = await async_client.crm.properties.get_by_name(
            property_name="propertyName",
            object_type="objectType",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_name_with_all_params(self, async_client: AsyncHubSpot) -> None:
        property = await async_client.crm.properties.get_by_name(
            property_name="propertyName",
            object_type="objectType",
            archived=True,
            properties="properties",
        )
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_name(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.properties.with_raw_response.get_by_name(
            property_name="propertyName",
            object_type="objectType",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(Property, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_name(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.properties.with_streaming_response.get_by_name(
            property_name="propertyName",
            object_type="objectType",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(Property, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_by_name(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.with_raw_response.get_by_name(
                property_name="propertyName",
                object_type="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `property_name` but received ''"):
            await async_client.crm.properties.with_raw_response.get_by_name(
                property_name="",
                object_type="objectType",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncHubSpot) -> None:
        property = await async_client.crm.properties.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
        )
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncHubSpot) -> None:
        property = await async_client.crm.properties.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
            data_sensitivity="non_sensitive",
        )
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.crm.properties.with_raw_response.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        property = await response.parse()
        assert_matches_type(BatchResponseProperty, property, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncHubSpot) -> None:
        async with async_client.crm.properties.with_streaming_response.read(
            object_type="objectType",
            archived=True,
            inputs=[{"name": "my_custom_property"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            property = await response.parse()
            assert_matches_type(BatchResponseProperty, property, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `object_type` but received ''"):
            await async_client.crm.properties.with_raw_response.read(
                object_type="",
                archived=True,
                inputs=[{"name": "my_custom_property"}],
            )
