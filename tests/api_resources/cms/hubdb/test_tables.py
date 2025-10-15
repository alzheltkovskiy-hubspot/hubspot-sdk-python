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
from hubspot_sdk.types.cms import HubDBTableV3, ImportResult, CollectionResponseWithTotalHubDBTableV3ForwardPaging

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTables:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.create(
            label="label",
            name="name",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.create(
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
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.cms.hubdb.tables.with_raw_response.create(
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.cms.hubdb.tables.with_streaming_response.create(
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.list()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.list(
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
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.cms.hubdb.tables.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.cms.hubdb.tables.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_archive(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.archive(
            "tableIdOrName",
        )
        assert table is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: HubSpot) -> None:
        response = client.cms.hubdb.tables.with_raw_response.archive(
            "tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert table is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: HubSpot) -> None:
        with client.cms.hubdb.tables.with_streaming_response.archive(
            "tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert table is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.tables.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_draft(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_draft_with_all_params(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
            new_label="newLabel",
            new_name="newName",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clone_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.tables.with_raw_response.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clone_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.tables.with_streaming_response.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_clone_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.tables.with_raw_response.clone_draft(
                table_id_or_name="",
                copy_rows=True,
                is_hubspot_defined=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_version(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.delete_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        )
        assert table is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_version(self, client: HubSpot) -> None:
        response = client.cms.hubdb.tables.with_raw_response.delete_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert table is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_version(self, client: HubSpot) -> None:
        with client.cms.hubdb.tables.with_streaming_response.delete_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert table is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_version(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.tables.with_raw_response.delete_version(
                version_id=0,
                table_id_or_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        table = client.cms.hubdb.tables.export(
            table_id_or_name="tableIdOrName",
        )
        assert table.is_closed
        assert table.json() == {"foo": "bar"}
        assert cast(Any, table.is_closed) is True
        assert isinstance(table, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        table = client.cms.hubdb.tables.export(
            table_id_or_name="tableIdOrName",
            format="format",
        )
        assert table.is_closed
        assert table.json() == {"foo": "bar"}
        assert cast(Any, table.is_closed) is True
        assert isinstance(table, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        table = client.cms.hubdb.tables.with_raw_response.export(
            table_id_or_name="tableIdOrName",
        )

        assert table.is_closed is True
        assert table.http_request.headers.get("X-Stainless-Lang") == "python"
        assert table.json() == {"foo": "bar"}
        assert isinstance(table, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.hubdb.tables.with_streaming_response.export(
            table_id_or_name="tableIdOrName",
        ) as table:
            assert not table.is_closed
            assert table.http_request.headers.get("X-Stainless-Lang") == "python"

            assert table.json() == {"foo": "bar"}
            assert cast(Any, table.is_closed) is True
            assert isinstance(table, StreamedBinaryAPIResponse)

        assert cast(Any, table.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_export(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.tables.with_raw_response.export(
                table_id_or_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_draft(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        table = client.cms.hubdb.tables.export_draft(
            table_id_or_name="tableIdOrName",
        )
        assert table.is_closed
        assert table.json() == {"foo": "bar"}
        assert cast(Any, table.is_closed) is True
        assert isinstance(table, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_export_draft_with_all_params(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        table = client.cms.hubdb.tables.export_draft(
            table_id_or_name="tableIdOrName",
            format="format",
        )
        assert table.is_closed
        assert table.json() == {"foo": "bar"}
        assert cast(Any, table.is_closed) is True
        assert isinstance(table, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_export_draft(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        table = client.cms.hubdb.tables.with_raw_response.export_draft(
            table_id_or_name="tableIdOrName",
        )

        assert table.is_closed is True
        assert table.http_request.headers.get("X-Stainless-Lang") == "python"
        assert table.json() == {"foo": "bar"}
        assert isinstance(table, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_export_draft(self, client: HubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.cms.hubdb.tables.with_streaming_response.export_draft(
            table_id_or_name="tableIdOrName",
        ) as table:
            assert not table.is_closed
            assert table.http_request.headers.get("X-Stainless-Lang") == "python"

            assert table.json() == {"foo": "bar"}
            assert cast(Any, table.is_closed) is True
            assert isinstance(table, StreamedBinaryAPIResponse)

        assert cast(Any, table.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_export_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.tables.with_raw_response.export_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.get(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.get(
            table_id_or_name="tableIdOrName",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: HubSpot) -> None:
        response = client.cms.hubdb.tables.with_raw_response.get(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: HubSpot) -> None:
        with client.cms.hubdb.tables.with_streaming_response.get(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.tables.with_raw_response.get(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.get_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_draft_with_all_params(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.get_draft(
            table_id_or_name="tableIdOrName",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.tables.with_raw_response.get_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.tables.with_streaming_response.get_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.tables.with_raw_response.get_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_draft(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.import_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(ImportResult, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_draft_with_all_params(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.import_draft(
            table_id_or_name="tableIdOrName",
            config="config",
            file=b"raw file contents",
        )
        assert_matches_type(ImportResult, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_import_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.tables.with_raw_response.import_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(ImportResult, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_import_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.tables.with_streaming_response.import_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(ImportResult, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_import_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.tables.with_raw_response.import_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_drafts(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.list_drafts()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_drafts_with_all_params(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.list_drafts(
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
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_drafts(self, client: HubSpot) -> None:
        response = client.cms.hubdb.tables.with_raw_response.list_drafts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_drafts(self, client: HubSpot) -> None:
        with client.cms.hubdb.tables.with_streaming_response.list_drafts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish_draft(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.publish_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish_draft_with_all_params(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.publish_draft(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_publish_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.tables.with_raw_response.publish_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_publish_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.tables.with_streaming_response.publish_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_publish_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.tables.with_raw_response.publish_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_draft(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.reset_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reset_draft_with_all_params(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.reset_draft(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reset_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.tables.with_raw_response.reset_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reset_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.tables.with_streaming_response.reset_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reset_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.tables.with_raw_response.reset_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unpublish(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.unpublish(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unpublish_with_all_params(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.unpublish(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unpublish(self, client: HubSpot) -> None:
        response = client.cms.hubdb.tables.with_raw_response.unpublish(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unpublish(self, client: HubSpot) -> None:
        with client.cms.hubdb.tables.with_streaming_response.unpublish(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unpublish(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.tables.with_raw_response.unpublish(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_draft_with_all_params(self, client: HubSpot) -> None:
        table = client.cms.hubdb.tables.update_draft(
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
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_draft(self, client: HubSpot) -> None:
        response = client.cms.hubdb.tables.with_raw_response.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_draft(self, client: HubSpot) -> None:
        with client.cms.hubdb.tables.with_streaming_response.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_draft(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            client.cms.hubdb.tables.with_raw_response.update_draft(
                table_id_or_name="",
                label="label",
                name="name",
            )


class TestAsyncTables:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.create(
            label="label",
            name="name",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.create(
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
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.tables.with_raw_response.create(
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.tables.with_streaming_response.create(
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.list()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.list(
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
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.tables.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.tables.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.archive(
            "tableIdOrName",
        )
        assert table is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.tables.with_raw_response.archive(
            "tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert table is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.tables.with_streaming_response.archive(
            "tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert table is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.tables.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_draft(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
            new_label="newLabel",
            new_name="newName",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clone_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.tables.with_raw_response.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clone_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.tables.with_streaming_response.clone_draft(
            table_id_or_name="tableIdOrName",
            copy_rows=True,
            is_hubspot_defined=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_clone_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.tables.with_raw_response.clone_draft(
                table_id_or_name="",
                copy_rows=True,
                is_hubspot_defined=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_version(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.delete_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        )
        assert table is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_version(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.tables.with_raw_response.delete_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert table is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_version(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.tables.with_streaming_response.delete_version(
            version_id=0,
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert table is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_version(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.tables.with_raw_response.delete_version(
                version_id=0,
                table_id_or_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        table = await async_client.cms.hubdb.tables.export(
            table_id_or_name="tableIdOrName",
        )
        assert table.is_closed
        assert await table.json() == {"foo": "bar"}
        assert cast(Any, table.is_closed) is True
        assert isinstance(table, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_with_all_params(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        table = await async_client.cms.hubdb.tables.export(
            table_id_or_name="tableIdOrName",
            format="format",
        )
        assert table.is_closed
        assert await table.json() == {"foo": "bar"}
        assert cast(Any, table.is_closed) is True
        assert isinstance(table, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        table = await async_client.cms.hubdb.tables.with_raw_response.export(
            table_id_or_name="tableIdOrName",
        )

        assert table.is_closed is True
        assert table.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await table.json() == {"foo": "bar"}
        assert isinstance(table, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.hubdb.tables.with_streaming_response.export(
            table_id_or_name="tableIdOrName",
        ) as table:
            assert not table.is_closed
            assert table.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await table.json() == {"foo": "bar"}
            assert cast(Any, table.is_closed) is True
            assert isinstance(table, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, table.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_export(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.tables.with_raw_response.export(
                table_id_or_name="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_draft(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        table = await async_client.cms.hubdb.tables.export_draft(
            table_id_or_name="tableIdOrName",
        )
        assert table.is_closed
        assert await table.json() == {"foo": "bar"}
        assert cast(Any, table.is_closed) is True
        assert isinstance(table, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_export_draft_with_all_params(
        self, async_client: AsyncHubSpot, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        table = await async_client.cms.hubdb.tables.export_draft(
            table_id_or_name="tableIdOrName",
            format="format",
        )
        assert table.is_closed
        assert await table.json() == {"foo": "bar"}
        assert cast(Any, table.is_closed) is True
        assert isinstance(table, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_export_draft(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        table = await async_client.cms.hubdb.tables.with_raw_response.export_draft(
            table_id_or_name="tableIdOrName",
        )

        assert table.is_closed is True
        assert table.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await table.json() == {"foo": "bar"}
        assert isinstance(table, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_export_draft(self, async_client: AsyncHubSpot, respx_mock: MockRouter) -> None:
        respx_mock.get("/cms/v3/hubdb/tables/tableIdOrName/draft/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.cms.hubdb.tables.with_streaming_response.export_draft(
            table_id_or_name="tableIdOrName",
        ) as table:
            assert not table.is_closed
            assert table.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await table.json() == {"foo": "bar"}
            assert cast(Any, table.is_closed) is True
            assert isinstance(table, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, table.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_export_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.tables.with_raw_response.export_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.get(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.get(
            table_id_or_name="tableIdOrName",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.tables.with_raw_response.get(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.tables.with_streaming_response.get(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.tables.with_raw_response.get(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.get_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.get_draft(
            table_id_or_name="tableIdOrName",
            archived=True,
            include_foreign_ids=True,
            is_get_localized_schema=True,
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.tables.with_raw_response.get_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.tables.with_streaming_response.get_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.tables.with_raw_response.get_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_draft(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.import_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(ImportResult, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.import_draft(
            table_id_or_name="tableIdOrName",
            config="config",
            file=b"raw file contents",
        )
        assert_matches_type(ImportResult, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_import_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.tables.with_raw_response.import_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(ImportResult, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_import_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.tables.with_streaming_response.import_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(ImportResult, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_import_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.tables.with_raw_response.import_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_drafts(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.list_drafts()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_drafts_with_all_params(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.list_drafts(
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
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_drafts(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.tables.with_raw_response.list_drafts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_drafts(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.tables.with_streaming_response.list_drafts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(CollectionResponseWithTotalHubDBTableV3ForwardPaging, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish_draft(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.publish_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.publish_draft(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_publish_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.tables.with_raw_response.publish_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_publish_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.tables.with_streaming_response.publish_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_publish_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.tables.with_raw_response.publish_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_draft(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.reset_draft(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reset_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.reset_draft(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reset_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.tables.with_raw_response.reset_draft(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reset_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.tables.with_streaming_response.reset_draft(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reset_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.tables.with_raw_response.reset_draft(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unpublish(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.unpublish(
            table_id_or_name="tableIdOrName",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unpublish_with_all_params(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.unpublish(
            table_id_or_name="tableIdOrName",
            include_foreign_ids=True,
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unpublish(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.tables.with_raw_response.unpublish(
            table_id_or_name="tableIdOrName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unpublish(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.tables.with_streaming_response.unpublish(
            table_id_or_name="tableIdOrName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unpublish(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.tables.with_raw_response.unpublish(
                table_id_or_name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        )
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_draft_with_all_params(self, async_client: AsyncHubSpot) -> None:
        table = await async_client.cms.hubdb.tables.update_draft(
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
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_draft(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.cms.hubdb.tables.with_raw_response.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        table = await response.parse()
        assert_matches_type(HubDBTableV3, table, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_draft(self, async_client: AsyncHubSpot) -> None:
        async with async_client.cms.hubdb.tables.with_streaming_response.update_draft(
            table_id_or_name="tableIdOrName",
            label="label",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            table = await response.parse()
            assert_matches_type(HubDBTableV3, table, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_draft(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `table_id_or_name` but received ''"):
            await async_client.cms.hubdb.tables.with_raw_response.update_draft(
                table_id_or_name="",
                label="label",
                name="name",
            )
