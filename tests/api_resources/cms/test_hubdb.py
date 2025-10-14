# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from hubspot_sdk.types.cms import (
    HubDBTableV3,
    ImportResult,
    HubDBTableRowV3,
    BatchResponseHubDBTableRowV3,
    CollectionResponseWithTotalHubDBTableV3ForwardPaging,
    UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHubdb:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.create(
            label="label",
            name="name",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.create(
            label="label",
            name="name",
            allow_child_tables=True,
            allow_public_api_access=True,
            columns=[
                {
                    "id": 0,
                    "label": "label",
                    "name": "name",
                    "options": [
                        {
                            "hidden": False,
                            "label": "Option A",
                            "value": "A",
                            "description": "Choice number one",
                            "display_order": 1,
                        }
                    ],
                    "type": "NULL",
                    "foreign_column_id": 0,
                    "foreign_table_id": 0,
                    "max_number_of_characters": 0,
                    "max_number_of_options": 0,
                }
            ],
            dynamic_meta_tags={"foo": 0},
            enable_child_table_pages=True,
            use_for_pages=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.create(
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.create(
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.list()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.list(
            after="after",
            archived=True,
            content_type="contentType",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_get_localized_schema=True,
            limit=0,
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_archive(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.archive(
            "tableIdOrName",
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.archive(
            "tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.archive(
            "tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_archive_table(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.archive_table(
            "tableIdOrName",
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_archive_table(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.archive_table(
            "tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_archive_table(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.archive_table(
            "tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_archive_table(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.archive_table(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_batch(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.clone_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clone_batch(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.clone_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clone_batch(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.clone_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_clone_batch(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.clone_batch(
                table_id_or_name="",
                inputs=[{"id": "id"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_draft(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_draft_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
            new_label="newLabel",
            new_name="newName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clone_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clone_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_clone_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.clone_draft(
                table_id_or_name="",
                copy_rows=True,
                is_hubspot_defined=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_draft_table(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.clone_draft_table(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_draft_table_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.clone_draft_table(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
            new_label="newLabel",
            new_name="newName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clone_draft_table(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.clone_draft_table(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clone_draft_table(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.clone_draft_table(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_clone_draft_table(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.clone_draft_table(
                table_id_or_name="",
                copy_rows=True,
                is_hubspot_defined=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_draft_table_row(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.clone_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_draft_table_row_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.clone_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            name="name",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clone_draft_table_row(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.clone_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clone_draft_table_row(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.clone_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_clone_draft_table_row(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.clone_draft_table_row(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.with_raw_response.clone_draft_table_row(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_draft_table_rows(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.clone_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clone_draft_table_rows(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.clone_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clone_draft_table_rows(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.clone_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_clone_draft_table_rows(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.clone_draft_table_rows(
                table_id_or_name="",
                inputs=[{"id": "id"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_batch(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.create_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"values": {"foo": {}}}],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_batch(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.create_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"values": {"foo": {}}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_batch(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.create_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"values": {"foo": {}}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_batch(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.create_batch(
                table_id_or_name="",
                inputs=[{"values": {"foo": {}}}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_draft_table_rows(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.create_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[{"values": {"foo": {}}}],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_draft_table_rows(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.create_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[{"values": {"foo": {}}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_draft_table_rows(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.create_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[{"values": {"foo": {}}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_draft_table_rows(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.create_draft_table_rows(
                table_id_or_name="",
                inputs=[{"values": {"foo": {}}}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_table(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.create_table(
            label="label",
            name="name",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_table_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.create_table(
            label="label",
            name="name",
            allow_child_tables=True,
            allow_public_api_access=True,
            columns=[
                {
                    "id": 0,
                    "label": "label",
                    "name": "name",
                    "options": [
                        {
                            "hidden": False,
                            "label": "Option A",
                            "value": "A",
                            "description": "Choice number one",
                            "display_order": 1,
                        }
                    ],
                    "type": "NULL",
                    "foreign_column_id": 0,
                    "foreign_table_id": 0,
                    "max_number_of_characters": 0,
                    "max_number_of_options": 0,
                }
            ],
            dynamic_meta_tags={"foo": 0},
            enable_child_table_pages=True,
            use_for_pages=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_table(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.create_table(
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_table(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.create_table(
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_table_row(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.create_table_row(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_table_row_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.create_table_row(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_table_row(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.create_table_row(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_table_row(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.create_table_row(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_table_row(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.create_table_row(
                table_id_or_name="",
                values={"foo": {}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_draft(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.delete_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.delete_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.delete_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.delete_draft(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.with_raw_response.delete_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_version(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.delete_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_version(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.delete_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_version(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.delete_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_version(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.delete_version(
                version_id=0,
                table_id_or_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = client.cms.hubdb.export(
            table_id_or_name="tableIdOrName",
        )
        assert hubdb.is_closed
        assert hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = client.cms.hubdb.export(
            table_id_or_name="tableIdOrName",
            format="format",
        )
        assert hubdb.is_closed
        assert hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        hubdb = client.cms.hubdb.with_raw_response.export(
            table_id_or_name="tableIdOrName",
        )

        assert hubdb.is_closed is True
        assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"
        assert hubdb.json() == {"foo": "bar"}
        assert isinstance(hubdb, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.hubdb.with_streaming_response.export(
            table_id_or_name="tableIdOrName",
        ) as hubdb:
            assert not hubdb.is_closed
            assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"

            assert hubdb.json() == {"foo": "bar"}
            assert cast(Any, hubdb.is_closed) is True
            assert isinstance(hubdb, StreamedBinaryAPIResponse)

        assert cast(Any, hubdb.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_export(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.export(
                table_id_or_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_draft(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = client.cms.hubdb.export_draft(
            table_id_or_name="tableIdOrName",
        )
        assert hubdb.is_closed
        assert hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_draft_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = client.cms.hubdb.export_draft(
            table_id_or_name="tableIdOrName",
            format="format",
        )
        assert hubdb.is_closed
        assert hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_draft(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        hubdb = client.cms.hubdb.with_raw_response.export_draft(
            table_id_or_name="tableIdOrName",
        )

        assert hubdb.is_closed is True
        assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"
        assert hubdb.json() == {"foo": "bar"}
        assert isinstance(hubdb, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_draft(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.hubdb.with_streaming_response.export_draft(
            table_id_or_name="tableIdOrName",
        ) as hubdb:
            assert not hubdb.is_closed
            assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"

            assert hubdb.json() == {"foo": "bar"}
            assert cast(Any, hubdb.is_closed) is True
            assert isinstance(hubdb, StreamedBinaryAPIResponse)

        assert cast(Any, hubdb.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_export_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.export_draft(
                table_id_or_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_draft_table(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = client.cms.hubdb.export_draft_table(
            table_id_or_name="tableIdOrName",
        )
        assert hubdb.is_closed
        assert hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_draft_table_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = client.cms.hubdb.export_draft_table(
            table_id_or_name="tableIdOrName",
            format="format",
        )
        assert hubdb.is_closed
        assert hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_draft_table(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        hubdb = client.cms.hubdb.with_raw_response.export_draft_table(
            table_id_or_name="tableIdOrName",
        )

        assert hubdb.is_closed is True
        assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"
        assert hubdb.json() == {"foo": "bar"}
        assert isinstance(hubdb, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_draft_table(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.hubdb.with_streaming_response.export_draft_table(
            table_id_or_name="tableIdOrName",
        ) as hubdb:
            assert not hubdb.is_closed
            assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"

            assert hubdb.json() == {"foo": "bar"}
            assert cast(Any, hubdb.is_closed) is True
            assert isinstance(hubdb, StreamedBinaryAPIResponse)

        assert cast(Any, hubdb.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_export_draft_table(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.export_draft_table(
                table_id_or_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_table(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = client.cms.hubdb.export_table(
            table_id_or_name="tableIdOrName",
        )
        assert hubdb.is_closed
        assert hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_table_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = client.cms.hubdb.export_table(
            table_id_or_name="tableIdOrName",
            format="format",
        )
        assert hubdb.is_closed
        assert hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_table(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        hubdb = client.cms.hubdb.with_raw_response.export_table(
            table_id_or_name="tableIdOrName",
        )

        assert hubdb.is_closed is True
        assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"
        assert hubdb.json() == {"foo": "bar"}
        assert isinstance(hubdb, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_table(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.hubdb.with_streaming_response.export_table(
            table_id_or_name="tableIdOrName",
        ) as hubdb:
            assert not hubdb.is_closed
            assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"

            assert hubdb.json() == {"foo": "bar"}
            assert cast(Any, hubdb.is_closed) is True
            assert isinstance(hubdb, StreamedBinaryAPIResponse)

        assert cast(Any, hubdb.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_export_table(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.export_table(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get(
            table_id_or_name="tableIdOrName",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.get(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.get(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.get(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_all_draft_tables(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_all_draft_tables()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_all_draft_tables_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_all_draft_tables(
            after="after",
            archived=True,
            content_type="contentType",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_get_localized_schema=True,
            limit=0,
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_all_draft_tables(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.get_all_draft_tables()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_all_draft_tables(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.get_all_draft_tables() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_all_tables(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_all_tables()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_all_tables_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_all_tables(
            after="after",
            archived=True,
            content_type="contentType",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_get_localized_schema=True,
            limit=0,
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_all_tables(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.get_all_tables()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_all_tables(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.get_all_tables() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_draft(
            table_id_or_name="tableIdOrName",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.get_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.get_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.get_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft_table_details_by_id(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_draft_table_details_by_id(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft_table_details_by_id_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_draft_table_details_by_id(
            table_id_or_name="tableIdOrName",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_draft_table_details_by_id(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.get_draft_table_details_by_id(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_draft_table_details_by_id(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.get_draft_table_details_by_id(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_draft_table_details_by_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.get_draft_table_details_by_id(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft_table_row_by_id(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_draft_table_row_by_id(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft_table_row_by_id_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_draft_table_row_by_id(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            archived=True,
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_draft_table_row_by_id(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.get_draft_table_row_by_id(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_draft_table_row_by_id(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.get_draft_table_row_by_id(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_draft_table_row_by_id(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.get_draft_table_row_by_id(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.with_raw_response.get_draft_table_row_by_id(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_table_details(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_table_details(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_table_details_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_table_details(
            table_id_or_name="tableIdOrName",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_table_details(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.get_table_details(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_table_details(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.get_table_details(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_table_details(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.get_table_details(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_table_row(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_table_row_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            archived=True,
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_table_row(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.get_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_table_row(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.get_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_table_row(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.get_table_row(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.with_raw_response.get_table_row(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_table_rows(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_table_rows(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_table_rows_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.get_table_rows(
            table_id_or_name="tableIdOrName",
            after="after",
            archived=True,
            limit=0,
            offset=0,
            properties=["string"],
            sort=["string"],
        )
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_table_rows(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.get_table_rows(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_table_rows(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.get_table_rows(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_table_rows(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.get_table_rows(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_draft(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.import_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(ImportResult, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_draft_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.import_draft(
            table_id_or_name="tableIdOrName",
            config="config",
            file=b"raw file contents",
        )
        assert_matches_type(ImportResult, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_import_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.import_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(ImportResult, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_import_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.import_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(ImportResult, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_import_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.import_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_draft_table(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.import_draft_table(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(ImportResult, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_draft_table_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.import_draft_table(
            table_id_or_name="tableIdOrName",
            config="config",
            file=b"raw file contents",
        )
        assert_matches_type(ImportResult, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_import_draft_table(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.import_draft_table(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(ImportResult, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_import_draft_table(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.import_draft_table(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(ImportResult, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_import_draft_table(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.import_draft_table(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_draft(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.list_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_draft_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.list_draft(
            table_id_or_name="tableIdOrName",
            after="after",
            archived=True,
            limit=0,
            offset=0,
            properties=["string"],
            sort=["string"],
        )
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.list_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.list_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.list_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_drafts(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.list_drafts()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_drafts_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.list_drafts(
            after="after",
            archived=True,
            content_type="contentType",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_get_localized_schema=True,
            limit=0,
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_drafts(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.list_drafts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_drafts(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.list_drafts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish_draft(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.publish_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish_draft_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.publish_draft(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_publish_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.publish_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_publish_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.publish_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_publish_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.publish_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish_draft_table(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.publish_draft_table(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish_draft_table_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.publish_draft_table(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_publish_draft_table(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.publish_draft_table(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_publish_draft_table(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.publish_draft_table(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_publish_draft_table(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.publish_draft_table(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_purge_batch(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.purge_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_purge_batch(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.purge_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_purge_batch(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.purge_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_purge_batch(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.purge_batch(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_purge_draft_table_row(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.purge_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_purge_draft_table_row(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.purge_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_purge_draft_table_row(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.purge_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_purge_draft_table_row(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.purge_draft_table_row(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.with_raw_response.purge_draft_table_row(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_purge_draft_table_rows(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.purge_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_purge_draft_table_rows(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.purge_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_purge_draft_table_rows(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.purge_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_purge_draft_table_rows(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.purge_draft_table_rows(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_batch(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.read_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read_batch(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.read_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read_batch(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.read_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read_batch(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.read_batch(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_draft_batch(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.read_draft_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read_draft_batch(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.read_draft_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read_draft_batch(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.read_draft_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read_draft_batch(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.read_draft_batch(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_draft_table_rows(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.read_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read_draft_table_rows(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.read_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read_draft_table_rows(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.read_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read_draft_table_rows(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.read_draft_table_rows(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_table_rows(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.read_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read_table_rows(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.read_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read_table_rows(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.read_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read_table_rows(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.read_table_rows(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove_table_version(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.remove_table_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove_table_version(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.remove_table_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove_table_version(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.remove_table_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove_table_version(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.remove_table_version(
                version_id=0,
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace_batch(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.replace_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replace_batch(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.replace_batch(
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
        hubdb = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replace_batch(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.replace_batch(
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

            hubdb = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replace_batch(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.replace_batch(
                table_id_or_name="",
                inputs=[
                    {
                        "id": "id",
                        "values": {"foo": {}},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace_draft(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace_draft_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replace_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replace_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replace_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.replace_draft(
                row_id="321669910225",
                table_id_or_name="",
                values={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.with_raw_response.replace_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
                values={"foo": {}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace_draft_table_row(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.replace_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace_draft_table_row_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.replace_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replace_draft_table_row(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.replace_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replace_draft_table_row(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.replace_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replace_draft_table_row(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.replace_draft_table_row(
                row_id="321669910225",
                table_id_or_name="",
                values={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.with_raw_response.replace_draft_table_row(
                row_id="",
                table_id_or_name="tableIdOrName",
                values={"foo": {}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace_draft_table_rows(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.replace_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replace_draft_table_rows(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.replace_draft_table_rows(
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
        hubdb = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replace_draft_table_rows(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.replace_draft_table_rows(
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

            hubdb = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replace_draft_table_rows(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.replace_draft_table_rows(
                table_id_or_name="",
                inputs=[
                    {
                        "id": "id",
                        "values": {"foo": {}},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_draft(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.reset_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_draft_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.reset_draft(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reset_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.reset_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reset_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.reset_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reset_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.reset_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_draft_table(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.reset_draft_table(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_draft_table_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.reset_draft_table(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reset_draft_table(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.reset_draft_table(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reset_draft_table(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.reset_draft_table(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reset_draft_table(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.reset_draft_table(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unpublish(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.unpublish(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unpublish_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.unpublish(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unpublish(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.unpublish(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unpublish(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.unpublish(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unpublish(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.unpublish(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unpublish_table(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.unpublish_table(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unpublish_table_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.unpublish_table(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unpublish_table(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.unpublish_table(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unpublish_table(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.unpublish_table(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unpublish_table(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.unpublish_table(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_batch(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.update_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_batch(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.update_batch(
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
        hubdb = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_batch(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.update_batch(
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

            hubdb = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_batch(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.update_batch(
                table_id_or_name="",
                inputs=[
                    {
                        "id": "id",
                        "values": {"foo": {}},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
            allow_child_tables=True,
            allow_public_api_access=True,
            columns=[
                {
                    "id": 0,
                    "label": "label",
                    "name": "name",
                    "options": [
                        {
                            "hidden": False,
                            "label": "Option A",
                            "value": "A",
                            "description": "Choice number one",
                            "display_order": 1,
                        }
                    ],
                    "type": "NULL",
                    "foreign_column_id": 0,
                    "foreign_table_id": 0,
                    "max_number_of_characters": 0,
                    "max_number_of_options": 0,
                }
            ],
            dynamic_meta_tags={"foo": 0},
            enable_child_table_pages=True,
            use_for_pages=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.update_draft(
                table_id_or_name="",
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft_table(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.update_draft_table(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft_table_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.update_draft_table(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
            allow_child_tables=True,
            allow_public_api_access=True,
            columns=[
                {
                    "id": 0,
                    "label": "label",
                    "name": "name",
                    "options": [
                        {
                            "hidden": False,
                            "label": "Option A",
                            "value": "A",
                            "description": "Choice number one",
                            "display_order": 1,
                        }
                    ],
                    "type": "NULL",
                    "foreign_column_id": 0,
                    "foreign_table_id": 0,
                    "max_number_of_characters": 0,
                    "max_number_of_options": 0,
                }
            ],
            dynamic_meta_tags={"foo": 0},
            enable_child_table_pages=True,
            use_for_pages=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_draft_table(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.update_draft_table(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_draft_table(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.update_draft_table(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_draft_table(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.update_draft_table(
                table_id_or_name="",
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft_table_row(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.update_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft_table_row_with_all_params(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.update_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_draft_table_row(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.update_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_draft_table_row(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.update_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_draft_table_row(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.update_draft_table_row(
                row_id="321669910225",
                table_id_or_name="",
                values={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            client.cms.hubdb.with_raw_response.update_draft_table_row(
                row_id="",
                table_id_or_name="tableIdOrName",
                values={"foo": {}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft_table_rows(self, client: HubSpot) -> None:
        hubdb = client.cms.hubdb.update_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_draft_table_rows(self, client: HubSpot) -> None:
        response = client.cms.hubdb.with_raw_response.update_draft_table_rows(
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
        hubdb = response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_draft_table_rows(self, client: HubSpot) -> None:
        with client.cms.hubdb.with_streaming_response.update_draft_table_rows(
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

            hubdb = response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_draft_table_rows(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.with_raw_response.update_draft_table_rows(
                table_id_or_name="",
                inputs=[
                    {
                        "id": "id",
                        "values": {"foo": {}},
                    }
                ],
            )


class TestAsyncHubdb:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.create(
            label="label",
            name="name",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.create(
            label="label",
            name="name",
            allow_child_tables=True,
            allow_public_api_access=True,
            columns=[
                {
                    "id": 0,
                    "label": "label",
                    "name": "name",
                    "options": [
                        {
                            "hidden": False,
                            "label": "Option A",
                            "value": "A",
                            "description": "Choice number one",
                            "display_order": 1,
                        }
                    ],
                    "type": "NULL",
                    "foreign_column_id": 0,
                    "foreign_table_id": 0,
                    "max_number_of_characters": 0,
                    "max_number_of_options": 0,
                }
            ],
            dynamic_meta_tags={"foo": 0},
            enable_child_table_pages=True,
            use_for_pages=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.create(
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.create(
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.list()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.list(
            after="after",
            archived=True,
            content_type="contentType",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_get_localized_schema=True,
            limit=0,
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.archive(
            "tableIdOrName",
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.archive(
            "tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.archive(
            "tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_archive_table(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.archive_table(
            "tableIdOrName",
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_archive_table(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.archive_table(
            "tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_archive_table(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.archive_table(
            "tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_archive_table(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.archive_table(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_batch(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.clone_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clone_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.clone_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clone_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.clone_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_clone_batch(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.clone_batch(
                table_id_or_name="",
                inputs=[{"id": "id"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_draft(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
            new_label="newLabel",
            new_name="newName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clone_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clone_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_clone_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.clone_draft(
                table_id_or_name="",
                copy_rows=True,
                is_hubspot_defined=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_draft_table(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.clone_draft_table(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_draft_table_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.clone_draft_table(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
            new_label="newLabel",
            new_name="newName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clone_draft_table(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.clone_draft_table(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clone_draft_table(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.clone_draft_table(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_clone_draft_table(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.clone_draft_table(
                table_id_or_name="",
                copy_rows=True,
                is_hubspot_defined=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.clone_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_draft_table_row_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.clone_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            name="name",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clone_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.clone_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clone_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.clone_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_clone_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.clone_draft_table_row(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.with_raw_response.clone_draft_table_row(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.clone_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clone_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.clone_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clone_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.clone_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[{"id": "id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_clone_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.clone_draft_table_rows(
                table_id_or_name="",
                inputs=[{"id": "id"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_batch(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.create_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"values": {"foo": {}}}],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.create_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"values": {"foo": {}}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.create_batch(
            table_id_or_name="tableIdOrName",
            inputs=[{"values": {"foo": {}}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_batch(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.create_batch(
                table_id_or_name="",
                inputs=[{"values": {"foo": {}}}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.create_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[{"values": {"foo": {}}}],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.create_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[{"values": {"foo": {}}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.create_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[{"values": {"foo": {}}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.create_draft_table_rows(
                table_id_or_name="",
                inputs=[{"values": {"foo": {}}}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_table(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.create_table(
            label="label",
            name="name",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_table_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.create_table(
            label="label",
            name="name",
            allow_child_tables=True,
            allow_public_api_access=True,
            columns=[
                {
                    "id": 0,
                    "label": "label",
                    "name": "name",
                    "options": [
                        {
                            "hidden": False,
                            "label": "Option A",
                            "value": "A",
                            "description": "Choice number one",
                            "display_order": 1,
                        }
                    ],
                    "type": "NULL",
                    "foreign_column_id": 0,
                    "foreign_table_id": 0,
                    "max_number_of_characters": 0,
                    "max_number_of_options": 0,
                }
            ],
            dynamic_meta_tags={"foo": 0},
            enable_child_table_pages=True,
            use_for_pages=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_table(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.create_table(
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_table(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.create_table(
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_table_row(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.create_table_row(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_table_row_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.create_table_row(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_table_row(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.create_table_row(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_table_row(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.create_table_row(
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_table_row(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.create_table_row(
                table_id_or_name="",
                values={"foo": {}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_draft(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.delete_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.delete_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.delete_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.delete_draft(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.with_raw_response.delete_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_version(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.delete_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_version(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.delete_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_version(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.delete_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_version(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.delete_version(
                version_id=0,
                table_id_or_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = await async_client.cms.hubdb.export(
            table_id_or_name="tableIdOrName",
        )
        assert hubdb.is_closed
        assert await hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_with_all_params(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = await async_client.cms.hubdb.export(
            table_id_or_name="tableIdOrName",
            format="format",
        )
        assert hubdb.is_closed
        assert await hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        hubdb = await async_client.cms.hubdb.with_raw_response.export(
            table_id_or_name="tableIdOrName",
        )

        assert hubdb.is_closed is True
        assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await hubdb.json() == {"foo": "bar"}
        assert isinstance(hubdb, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.hubdb.with_streaming_response.export(
            table_id_or_name="tableIdOrName",
        ) as hubdb:
            assert not hubdb.is_closed
            assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await hubdb.json() == {"foo": "bar"}
            assert cast(Any, hubdb.is_closed) is True
            assert isinstance(hubdb, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, hubdb.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_export(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.export(
                table_id_or_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_draft(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = await async_client.cms.hubdb.export_draft(
            table_id_or_name="tableIdOrName",
        )
        assert hubdb.is_closed
        assert await hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_draft_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = await async_client.cms.hubdb.export_draft(
            table_id_or_name="tableIdOrName",
            format="format",
        )
        assert hubdb.is_closed
        assert await hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_draft(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        hubdb = await async_client.cms.hubdb.with_raw_response.export_draft(
            table_id_or_name="tableIdOrName",
        )

        assert hubdb.is_closed is True
        assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await hubdb.json() == {"foo": "bar"}
        assert isinstance(hubdb, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_draft(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.hubdb.with_streaming_response.export_draft(
            table_id_or_name="tableIdOrName",
        ) as hubdb:
            assert not hubdb.is_closed
            assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await hubdb.json() == {"foo": "bar"}
            assert cast(Any, hubdb.is_closed) is True
            assert isinstance(hubdb, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, hubdb.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_export_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.export_draft(
                table_id_or_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_draft_table(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = await async_client.cms.hubdb.export_draft_table(
            table_id_or_name="tableIdOrName",
        )
        assert hubdb.is_closed
        assert await hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_draft_table_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = await async_client.cms.hubdb.export_draft_table(
            table_id_or_name="tableIdOrName",
            format="format",
        )
        assert hubdb.is_closed
        assert await hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_draft_table(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        hubdb = await async_client.cms.hubdb.with_raw_response.export_draft_table(
            table_id_or_name="tableIdOrName",
        )

        assert hubdb.is_closed is True
        assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await hubdb.json() == {"foo": "bar"}
        assert isinstance(hubdb, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_draft_table(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.hubdb.with_streaming_response.export_draft_table(
            table_id_or_name="tableIdOrName",
        ) as hubdb:
            assert not hubdb.is_closed
            assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await hubdb.json() == {"foo": "bar"}
            assert cast(Any, hubdb.is_closed) is True
            assert isinstance(hubdb, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, hubdb.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_export_draft_table(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.export_draft_table(
                table_id_or_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_table(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = await async_client.cms.hubdb.export_table(
            table_id_or_name="tableIdOrName",
        )
        assert hubdb.is_closed
        assert await hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_table_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        hubdb = await async_client.cms.hubdb.export_table(
            table_id_or_name="tableIdOrName",
            format="format",
        )
        assert hubdb.is_closed
        assert await hubdb.json() == {"foo": "bar"}
        assert cast(Any, hubdb.is_closed) is True
        assert isinstance(hubdb, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_table(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        hubdb = await async_client.cms.hubdb.with_raw_response.export_table(
            table_id_or_name="tableIdOrName",
        )

        assert hubdb.is_closed is True
        assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await hubdb.json() == {"foo": "bar"}
        assert isinstance(hubdb, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_table(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.hubdb.with_streaming_response.export_table(
            table_id_or_name="tableIdOrName",
        ) as hubdb:
            assert not hubdb.is_closed
            assert hubdb.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await hubdb.json() == {"foo": "bar"}
            assert cast(Any, hubdb.is_closed) is True
            assert isinstance(hubdb, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, hubdb.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_export_table(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.export_table(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get(
            table_id_or_name="tableIdOrName",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.get(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.get(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.get(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_all_draft_tables(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_all_draft_tables()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_all_draft_tables_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_all_draft_tables(
            after="after",
            archived=True,
            content_type="contentType",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_get_localized_schema=True,
            limit=0,
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_all_draft_tables(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.get_all_draft_tables()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_all_draft_tables(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.get_all_draft_tables() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_all_tables(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_all_tables()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_all_tables_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_all_tables(
            after="after",
            archived=True,
            content_type="contentType",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_get_localized_schema=True,
            limit=0,
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_all_tables(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.get_all_tables()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_all_tables(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.get_all_tables() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_draft(
            table_id_or_name="tableIdOrName",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.get_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.get_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.get_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft_table_details_by_id(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_draft_table_details_by_id(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft_table_details_by_id_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_draft_table_details_by_id(
            table_id_or_name="tableIdOrName",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_draft_table_details_by_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.get_draft_table_details_by_id(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_draft_table_details_by_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.get_draft_table_details_by_id(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_draft_table_details_by_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.get_draft_table_details_by_id(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft_table_row_by_id(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_draft_table_row_by_id(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft_table_row_by_id_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_draft_table_row_by_id(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            archived=True,
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_draft_table_row_by_id(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.get_draft_table_row_by_id(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_draft_table_row_by_id(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.get_draft_table_row_by_id(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_draft_table_row_by_id(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.get_draft_table_row_by_id(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.with_raw_response.get_draft_table_row_by_id(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_table_details(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_table_details(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_table_details_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_table_details(
            table_id_or_name="tableIdOrName",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_table_details(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.get_table_details(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_table_details(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.get_table_details(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_table_details(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.get_table_details(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_table_row(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_table_row_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            archived=True,
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_table_row(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.get_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_table_row(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.get_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_table_row(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.get_table_row(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.with_raw_response.get_table_row(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_table_rows(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_table_rows(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_table_rows_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.get_table_rows(
            table_id_or_name="tableIdOrName",
            after="after",
            archived=True,
            limit=0,
            offset=0,
            properties=["string"],
            sort=["string"],
        )
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_table_rows(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.get_table_rows(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_table_rows(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.get_table_rows(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_table_rows(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.get_table_rows(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_draft(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.import_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(ImportResult, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.import_draft(
            table_id_or_name="tableIdOrName",
            config="config",
            file=b"raw file contents",
        )
        assert_matches_type(ImportResult, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_import_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.import_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(ImportResult, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_import_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.import_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(ImportResult, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_import_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.import_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_draft_table(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.import_draft_table(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(ImportResult, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_draft_table_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.import_draft_table(
            table_id_or_name="tableIdOrName",
            config="config",
            file=b"raw file contents",
        )
        assert_matches_type(ImportResult, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_import_draft_table(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.import_draft_table(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(ImportResult, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_import_draft_table(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.import_draft_table(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(ImportResult, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_import_draft_table(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.import_draft_table(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_draft(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.list_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.list_draft(
            table_id_or_name="tableIdOrName",
            after="after",
            archived=True,
            limit=0,
            offset=0,
            properties=["string"],
            sort=["string"],
        )
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.list_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.list_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.list_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_drafts(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.list_drafts()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_drafts_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.list_drafts(
            after="after",
            archived=True,
            content_type="contentType",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            is_get_localized_schema=True,
            limit=0,
            sort=["string"],
            updated_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_before=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_drafts(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.list_drafts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_drafts(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.list_drafts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish_draft(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.publish_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.publish_draft(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_publish_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.publish_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_publish_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.publish_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_publish_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.publish_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish_draft_table(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.publish_draft_table(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish_draft_table_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.publish_draft_table(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_publish_draft_table(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.publish_draft_table(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_publish_draft_table(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.publish_draft_table(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_publish_draft_table(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.publish_draft_table(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_purge_batch(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.purge_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_purge_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.purge_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_purge_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.purge_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_purge_batch(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.purge_batch(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_purge_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.purge_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_purge_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.purge_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_purge_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.purge_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_purge_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.purge_draft_table_row(
                row_id="321669910225",
                table_id_or_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.with_raw_response.purge_draft_table_row(
                row_id="",
                table_id_or_name="tableIdOrName",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_purge_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.purge_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_purge_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.purge_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_purge_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.purge_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_purge_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.purge_draft_table_rows(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_batch(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.read_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.read_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.read_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read_batch(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.read_batch(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_draft_batch(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.read_draft_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read_draft_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.read_draft_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read_draft_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.read_draft_batch(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read_draft_batch(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.read_draft_batch(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.read_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.read_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.read_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.read_draft_table_rows(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_table_rows(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.read_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read_table_rows(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.read_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read_table_rows(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.read_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read_table_rows(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.read_table_rows(
                table_id_or_name="",
                inputs=["string"],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove_table_version(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.remove_table_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        )
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove_table_version(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.remove_table_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert hubdb is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove_table_version(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.remove_table_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert hubdb is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove_table_version(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.remove_table_version(
                version_id=0,
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace_batch(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.replace_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replace_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.replace_batch(
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
        hubdb = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replace_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.replace_batch(
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

            hubdb = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replace_batch(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.replace_batch(
                table_id_or_name="",
                inputs=[
                    {
                        "id": "id",
                        "values": {"foo": {}},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace_draft(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replace_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replace_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.replace_draft(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replace_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.replace_draft(
                row_id="321669910225",
                table_id_or_name="",
                values={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.with_raw_response.replace_draft(
                row_id="",
                table_id_or_name="tableIdOrName",
                values={"foo": {}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.replace_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace_draft_table_row_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.replace_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replace_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.replace_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replace_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.replace_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replace_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.replace_draft_table_row(
                row_id="321669910225",
                table_id_or_name="",
                values={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.with_raw_response.replace_draft_table_row(
                row_id="",
                table_id_or_name="tableIdOrName",
                values={"foo": {}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.replace_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replace_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.replace_draft_table_rows(
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
        hubdb = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replace_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.replace_draft_table_rows(
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

            hubdb = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replace_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.replace_draft_table_rows(
                table_id_or_name="",
                inputs=[
                    {
                        "id": "id",
                        "values": {"foo": {}},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_draft(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.reset_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.reset_draft(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reset_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.reset_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reset_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.reset_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reset_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.reset_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_draft_table(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.reset_draft_table(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_draft_table_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.reset_draft_table(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reset_draft_table(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.reset_draft_table(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reset_draft_table(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.reset_draft_table(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reset_draft_table(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.reset_draft_table(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unpublish(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.unpublish(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unpublish_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.unpublish(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unpublish(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.unpublish(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unpublish(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.unpublish(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unpublish(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.unpublish(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unpublish_table(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.unpublish_table(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unpublish_table_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.unpublish_table(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unpublish_table(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.unpublish_table(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unpublish_table(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.unpublish_table(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unpublish_table(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.unpublish_table(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_batch(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.update_batch(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_batch(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.update_batch(
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
        hubdb = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_batch(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.update_batch(
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

            hubdb = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_batch(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.update_batch(
                table_id_or_name="",
                inputs=[
                    {
                        "id": "id",
                        "values": {"foo": {}},
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
            allow_child_tables=True,
            allow_public_api_access=True,
            columns=[
                {
                    "id": 0,
                    "label": "label",
                    "name": "name",
                    "options": [
                        {
                            "hidden": False,
                            "label": "Option A",
                            "value": "A",
                            "description": "Choice number one",
                            "display_order": 1,
                        }
                    ],
                    "type": "NULL",
                    "foreign_column_id": 0,
                    "foreign_table_id": 0,
                    "max_number_of_characters": 0,
                    "max_number_of_options": 0,
                }
            ],
            dynamic_meta_tags={"foo": 0},
            enable_child_table_pages=True,
            use_for_pages=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.update_draft(
                table_id_or_name="",
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft_table(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.update_draft_table(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft_table_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.update_draft_table(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
            allow_child_tables=True,
            allow_public_api_access=True,
            columns=[
                {
                    "id": 0,
                    "label": "label",
                    "name": "name",
                    "options": [
                        {
                            "hidden": False,
                            "label": "Option A",
                            "value": "A",
                            "description": "Choice number one",
                            "display_order": 1,
                        }
                    ],
                    "type": "NULL",
                    "foreign_column_id": 0,
                    "foreign_table_id": 0,
                    "max_number_of_characters": 0,
                    "max_number_of_options": 0,
                }
            ],
            dynamic_meta_tags={"foo": 0},
            enable_child_table_pages=True,
            use_for_pages=True,
        )
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_draft_table(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.update_draft_table(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_draft_table(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.update_draft_table(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_draft_table(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.update_draft_table(
                table_id_or_name="",
                label="label",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.update_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft_table_row_with_all_params(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.update_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
            child_table_id=0,
            display_index=0,
            name="name",
            path="path",
        )
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.update_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hubdb = await response.parse()
        assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.update_draft_table_row(
            row_id="321669910225",
            table_id_or_name="tableIdOrName",
            values={"foo": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hubdb = await response.parse()
            assert_matches_type(HubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_draft_table_row(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.update_draft_table_row(
                row_id="321669910225",
                table_id_or_name="",
                values={"foo": {}},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `row_id` but received ''"):
            await async_client.cms.hubdb.with_raw_response.update_draft_table_row(
                row_id="",
                table_id_or_name="tableIdOrName",
                values={"foo": {}},
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        hubdb = await async_client.cms.hubdb.update_draft_table_rows(
            table_id_or_name="tableIdOrName",
            inputs=[
                {
                    "id": "id",
                    "values": {"foo": {}},
                }
            ],
        )
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.with_raw_response.update_draft_table_rows(
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
        hubdb = await response.parse()
        assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.with_streaming_response.update_draft_table_rows(
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

            hubdb = await response.parse()
            assert_matches_type(BatchResponseHubDBTableRowV3, hubdb, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_draft_table_rows(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.with_raw_response.update_draft_table_rows(
                table_id_or_name="",
                inputs=[
                    {
                        "id": "id",
                        "values": {"foo": {}},
                    }
                ],
            )
