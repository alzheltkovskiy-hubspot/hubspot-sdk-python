# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Mapping, Iterable, cast
from datetime import datetime

import httpx

from .tables import (
    TablesResource,
    AsyncTablesResource,
    TablesResourceWithRawResponse,
    AsyncTablesResourceWithRawResponse,
    TablesResourceWithStreamingResponse,
    AsyncTablesResourceWithStreamingResponse,
)
from ...._types import (
    Body,
    Omit,
    Query,
    Headers,
    NoneType,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .rows.rows import (
    RowsResource,
    AsyncRowsResource,
    RowsResourceWithRawResponse,
    AsyncRowsResourceWithRawResponse,
    RowsResourceWithStreamingResponse,
    AsyncRowsResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ....types.cms import (
    hubdb_create_table_params,
    hubdb_export_table_params,
    hubdb_get_table_row_params,
    hubdb_get_all_tables_params,
    hubdb_get_table_rows_params,
    hubdb_read_table_rows_params,
    hubdb_unpublish_table_params,
    hubdb_create_table_row_params,
    hubdb_clone_draft_table_params,
    hubdb_get_table_details_params,
    hubdb_reset_draft_table_params,
    hubdb_export_draft_table_params,
    hubdb_import_draft_table_params,
    hubdb_update_draft_table_params,
    hubdb_publish_draft_table_params,
    hubdb_get_all_draft_tables_params,
    hubdb_clone_draft_table_row_params,
    hubdb_read_draft_table_rows_params,
    hubdb_clone_draft_table_rows_params,
    hubdb_purge_draft_table_rows_params,
    hubdb_update_draft_table_row_params,
    hubdb_create_draft_table_rows_params,
    hubdb_replace_draft_table_row_params,
    hubdb_update_draft_table_rows_params,
    hubdb_replace_draft_table_rows_params,
    hubdb_get_draft_table_row_by_id_params,
    hubdb_get_draft_table_details_by_id_params,
)
from ...._base_client import make_request_options
from ....types.cms.import_result import ImportResult
from ....types.cms.variant_param import VariantParam
from ....types.cms.hub_db_table_v3 import HubDBTableV3
from ....types.cms.hub_db_table_row_v3 import HubDBTableRowV3
from ....types.cms.column_request_param import ColumnRequestParam
from ....types.cms.hub_db_table_row_v3_request_param import HubDBTableRowV3RequestParam
from ....types.cms.batch_response_hub_db_table_row_v3 import BatchResponseHubDBTableRowV3
from ....types.cms.hub_db_table_row_batch_clone_request_param import HubDBTableRowBatchCloneRequestParam
from ....types.cms.hub_db_table_row_v3_batch_update_request_param import HubDBTableRowV3BatchUpdateRequestParam
from ....types.cms.collection_response_with_total_hub_db_table_v3_forward_paging import (
    CollectionResponseWithTotalHubDBTableV3ForwardPaging,
)
from ....types.cms.unified_collection_response_with_total_base_hub_db_table_row_v3 import (
    UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3,
)

__all__ = ["HubdbResource", "AsyncHubdbResource"]


class HubdbResource(SyncAPIResource):
    @cached_property
    def rows(self) -> RowsResource:
        return RowsResource(self._client)

    @cached_property
    def tables(self) -> TablesResource:
        return TablesResource(self._client)

    @cached_property
    def with_raw_response(self) -> HubdbResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return HubdbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HubdbResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return HubdbResourceWithStreamingResponse(self)

    def archive_table(
        self,
        table_id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cms/v3/hubdb/tables/{table_id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def clone_draft_table(
        self,
        table_id_or_name: str,
        *,
        copy_rows: bool,
        is_hubspot_defined: bool,
        new_label: str | Omit = omit,
        new_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Clone a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/clone",
            body=maybe_transform(
                {
                    "copy_rows": copy_rows,
                    "is_hubspot_defined": is_hubspot_defined,
                    "new_label": new_label,
                    "new_name": new_name,
                },
                hubdb_clone_draft_table_params.HubdbCloneDraftTableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
        )

    def clone_draft_table_row(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Clone a row

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/{row_id}/draft/clone",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"name": name}, hubdb_clone_draft_table_row_params.HubdbCloneDraftTableRowParams),
            ),
            cast_to=HubDBTableRowV3,
        )

    def clone_draft_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowBatchCloneRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Clone rows in batch

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/clone",
            body=maybe_transform(
                {"inputs": inputs}, hubdb_clone_draft_table_rows_params.HubdbCloneDraftTableRowsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def create_draft_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowV3RequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Create rows in batch

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/create",
            body=maybe_transform(
                {"inputs": inputs}, hubdb_create_draft_table_rows_params.HubdbCreateDraftTableRowsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def create_table(
        self,
        *,
        label: str,
        name: str,
        allow_child_tables: bool | Omit = omit,
        allow_public_api_access: bool | Omit = omit,
        columns: Iterable[ColumnRequestParam] | Omit = omit,
        dynamic_meta_tags: Dict[str, int] | Omit = omit,
        enable_child_table_pages: bool | Omit = omit,
        use_for_pages: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Create a new table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/hubdb/tables",
            body=maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "allow_child_tables": allow_child_tables,
                    "allow_public_api_access": allow_public_api_access,
                    "columns": columns,
                    "dynamic_meta_tags": dynamic_meta_tags,
                    "enable_child_table_pages": enable_child_table_pages,
                    "use_for_pages": use_for_pages,
                },
                hubdb_create_table_params.HubdbCreateTableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
        )

    def create_table_row(
        self,
        table_id_or_name: str,
        *,
        values: Dict[str, VariantParam],
        child_table_id: int | Omit = omit,
        display_index: int | Omit = omit,
        name: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Add a new row to a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows",
            body=maybe_transform(
                {
                    "values": values,
                    "child_table_id": child_table_id,
                    "display_index": display_index,
                    "name": name,
                    "path": path,
                },
                hubdb_create_table_row_params.HubdbCreateTableRowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )

    def export_draft_table(
        self,
        table_id_or_name: str,
        *,
        format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Export a draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "application/vnd.ms-excel", **(extra_headers or {})}
        return self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, hubdb_export_draft_table_params.HubdbExportDraftTableParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def export_table(
        self,
        table_id_or_name: str,
        *,
        format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Export a published version of a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "application/vnd.ms-excel", **(extra_headers or {})}
        return self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"format": format}, hubdb_export_table_params.HubdbExportTableParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_all_draft_tables(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        content_type: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalHubDBTableV3ForwardPaging:
        """
        Return all draft tables

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cms/v3/hubdb/tables/draft",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "content_type": content_type,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "is_get_localized_schema": is_get_localized_schema,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    hubdb_get_all_draft_tables_params.HubdbGetAllDraftTablesParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalHubDBTableV3ForwardPaging,
        )

    def get_all_tables(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        content_type: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalHubDBTableV3ForwardPaging:
        """
        Get all published tables

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cms/v3/hubdb/tables",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "content_type": content_type,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "is_get_localized_schema": is_get_localized_schema,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    hubdb_get_all_tables_params.HubdbGetAllTablesParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalHubDBTableV3ForwardPaging,
        )

    def get_draft_table_details_by_id(
        self,
        table_id_or_name: str,
        *,
        archived: bool | Omit = omit,
        include_foreign_ids: bool | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Get details for a draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "include_foreign_ids": include_foreign_ids,
                        "is_get_localized_schema": is_get_localized_schema,
                    },
                    hubdb_get_draft_table_details_by_id_params.HubdbGetDraftTableDetailsByIDParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    def get_draft_table_row_by_id(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Get a row from the draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/{row_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"archived": archived}, hubdb_get_draft_table_row_by_id_params.HubdbGetDraftTableRowByIDParams
                ),
            ),
            cast_to=HubDBTableRowV3,
        )

    def get_table_details(
        self,
        table_id_or_name: str,
        *,
        archived: bool | Omit = omit,
        include_foreign_ids: bool | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Get details of a published table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "include_foreign_ids": include_foreign_ids,
                        "is_get_localized_schema": is_get_localized_schema,
                    },
                    hubdb_get_table_details_params.HubdbGetTableDetailsParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    def get_table_row(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Get a table row

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/{row_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, hubdb_get_table_row_params.HubdbGetTableRowParams),
            ),
            cast_to=HubDBTableRowV3,
        )

    def get_table_rows(
        self,
        table_id_or_name: str,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3:
        """
        Get rows for a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return cast(
            UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3,
            self._get(
                f"/cms/v3/hubdb/tables/{table_id_or_name}/rows",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "after": after,
                            "archived": archived,
                            "limit": limit,
                            "offset": offset,
                            "properties": properties,
                            "sort": sort,
                        },
                        hubdb_get_table_rows_params.HubdbGetTableRowsParams,
                    ),
                ),
                cast_to=cast(
                    Any, UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def import_draft_table(
        self,
        table_id_or_name: str,
        *,
        config: str | Omit = omit,
        file: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportResult:
        """
        Import data into draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        body = deepcopy_minimal(
            {
                "config": config,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/import",
            body=maybe_transform(body, hubdb_import_draft_table_params.HubdbImportDraftTableParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportResult,
        )

    def publish_draft_table(
        self,
        table_id_or_name: str,
        *,
        include_foreign_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Publish a table from draft

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/publish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_foreign_ids": include_foreign_ids},
                    hubdb_publish_draft_table_params.HubdbPublishDraftTableParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    def purge_draft_table_row(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes a row

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/{row_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def purge_draft_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes rows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/purge",
            body=maybe_transform(
                {"inputs": inputs}, hubdb_purge_draft_table_rows_params.HubdbPurgeDraftTableRowsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def read_draft_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Get a set of rows from draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/read",
            body=maybe_transform({"inputs": inputs}, hubdb_read_draft_table_rows_params.HubdbReadDraftTableRowsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def read_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Get a set of rows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/batch/read",
            body=maybe_transform({"inputs": inputs}, hubdb_read_table_rows_params.HubdbReadTableRowsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def remove_table_version(
        self,
        version_id: int,
        *,
        table_id_or_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a table version

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def replace_draft_table_row(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        values: Dict[str, VariantParam],
        child_table_id: int | Omit = omit,
        display_index: int | Omit = omit,
        name: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Replaces an existing row

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return self._put(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/{row_id}/draft",
            body=maybe_transform(
                {
                    "values": values,
                    "child_table_id": child_table_id,
                    "display_index": display_index,
                    "name": name,
                    "path": path,
                },
                hubdb_replace_draft_table_row_params.HubdbReplaceDraftTableRowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )

    def replace_draft_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowV3BatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Replace rows in batch in draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/replace",
            body=maybe_transform(
                {"inputs": inputs}, hubdb_replace_draft_table_rows_params.HubdbReplaceDraftTableRowsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def reset_draft_table(
        self,
        table_id_or_name: str,
        *,
        include_foreign_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Reset a draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/reset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_foreign_ids": include_foreign_ids},
                    hubdb_reset_draft_table_params.HubdbResetDraftTableParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    def unpublish_table(
        self,
        table_id_or_name: str,
        *,
        include_foreign_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Unpublish a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/unpublish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"include_foreign_ids": include_foreign_ids}, hubdb_unpublish_table_params.HubdbUnpublishTableParams
                ),
            ),
            cast_to=HubDBTableV3,
        )

    def update_draft_table(
        self,
        table_id_or_name: str,
        *,
        label: str,
        name: str,
        archived: bool | Omit = omit,
        include_foreign_ids: bool | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        allow_child_tables: bool | Omit = omit,
        allow_public_api_access: bool | Omit = omit,
        columns: Iterable[ColumnRequestParam] | Omit = omit,
        dynamic_meta_tags: Dict[str, int] | Omit = omit,
        enable_child_table_pages: bool | Omit = omit,
        use_for_pages: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Update an existing table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._patch(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft",
            body=maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "allow_child_tables": allow_child_tables,
                    "allow_public_api_access": allow_public_api_access,
                    "columns": columns,
                    "dynamic_meta_tags": dynamic_meta_tags,
                    "enable_child_table_pages": enable_child_table_pages,
                    "use_for_pages": use_for_pages,
                },
                hubdb_update_draft_table_params.HubdbUpdateDraftTableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "include_foreign_ids": include_foreign_ids,
                        "is_get_localized_schema": is_get_localized_schema,
                    },
                    hubdb_update_draft_table_params.HubdbUpdateDraftTableParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    def update_draft_table_row(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        values: Dict[str, VariantParam],
        child_table_id: int | Omit = omit,
        display_index: int | Omit = omit,
        name: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Updates an existing row

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return self._patch(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/{row_id}/draft",
            body=maybe_transform(
                {
                    "values": values,
                    "child_table_id": child_table_id,
                    "display_index": display_index,
                    "name": name,
                    "path": path,
                },
                hubdb_update_draft_table_row_params.HubdbUpdateDraftTableRowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )

    def update_draft_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowV3BatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Update rows in batch in draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/update",
            body=maybe_transform(
                {"inputs": inputs}, hubdb_update_draft_table_rows_params.HubdbUpdateDraftTableRowsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )


class AsyncHubdbResource(AsyncAPIResource):
    @cached_property
    def rows(self) -> AsyncRowsResource:
        return AsyncRowsResource(self._client)

    @cached_property
    def tables(self) -> AsyncTablesResource:
        return AsyncTablesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHubdbResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHubdbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHubdbResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncHubdbResourceWithStreamingResponse(self)

    async def archive_table(
        self,
        table_id_or_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cms/v3/hubdb/tables/{table_id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def clone_draft_table(
        self,
        table_id_or_name: str,
        *,
        copy_rows: bool,
        is_hubspot_defined: bool,
        new_label: str | Omit = omit,
        new_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Clone a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/clone",
            body=await async_maybe_transform(
                {
                    "copy_rows": copy_rows,
                    "is_hubspot_defined": is_hubspot_defined,
                    "new_label": new_label,
                    "new_name": new_name,
                },
                hubdb_clone_draft_table_params.HubdbCloneDraftTableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
        )

    async def clone_draft_table_row(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Clone a row

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/{row_id}/draft/clone",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"name": name}, hubdb_clone_draft_table_row_params.HubdbCloneDraftTableRowParams
                ),
            ),
            cast_to=HubDBTableRowV3,
        )

    async def clone_draft_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowBatchCloneRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Clone rows in batch

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/clone",
            body=await async_maybe_transform(
                {"inputs": inputs}, hubdb_clone_draft_table_rows_params.HubdbCloneDraftTableRowsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def create_draft_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowV3RequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Create rows in batch

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/create",
            body=await async_maybe_transform(
                {"inputs": inputs}, hubdb_create_draft_table_rows_params.HubdbCreateDraftTableRowsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def create_table(
        self,
        *,
        label: str,
        name: str,
        allow_child_tables: bool | Omit = omit,
        allow_public_api_access: bool | Omit = omit,
        columns: Iterable[ColumnRequestParam] | Omit = omit,
        dynamic_meta_tags: Dict[str, int] | Omit = omit,
        enable_child_table_pages: bool | Omit = omit,
        use_for_pages: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Create a new table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/hubdb/tables",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "allow_child_tables": allow_child_tables,
                    "allow_public_api_access": allow_public_api_access,
                    "columns": columns,
                    "dynamic_meta_tags": dynamic_meta_tags,
                    "enable_child_table_pages": enable_child_table_pages,
                    "use_for_pages": use_for_pages,
                },
                hubdb_create_table_params.HubdbCreateTableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
        )

    async def create_table_row(
        self,
        table_id_or_name: str,
        *,
        values: Dict[str, VariantParam],
        child_table_id: int | Omit = omit,
        display_index: int | Omit = omit,
        name: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Add a new row to a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows",
            body=await async_maybe_transform(
                {
                    "values": values,
                    "child_table_id": child_table_id,
                    "display_index": display_index,
                    "name": name,
                    "path": path,
                },
                hubdb_create_table_row_params.HubdbCreateTableRowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )

    async def export_draft_table(
        self,
        table_id_or_name: str,
        *,
        format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Export a draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "application/vnd.ms-excel", **(extra_headers or {})}
        return await self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"format": format}, hubdb_export_draft_table_params.HubdbExportDraftTableParams
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def export_table(
        self,
        table_id_or_name: str,
        *,
        format: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Export a published version of a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "application/vnd.ms-excel", **(extra_headers or {})}
        return await self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/export",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"format": format}, hubdb_export_table_params.HubdbExportTableParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_all_draft_tables(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        content_type: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalHubDBTableV3ForwardPaging:
        """
        Return all draft tables

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cms/v3/hubdb/tables/draft",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "content_type": content_type,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "is_get_localized_schema": is_get_localized_schema,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    hubdb_get_all_draft_tables_params.HubdbGetAllDraftTablesParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalHubDBTableV3ForwardPaging,
        )

    async def get_all_tables(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        content_type: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        limit: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        updated_after: Union[str, datetime] | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalHubDBTableV3ForwardPaging:
        """
        Get all published tables

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cms/v3/hubdb/tables",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "content_type": content_type,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "is_get_localized_schema": is_get_localized_schema,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    hubdb_get_all_tables_params.HubdbGetAllTablesParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalHubDBTableV3ForwardPaging,
        )

    async def get_draft_table_details_by_id(
        self,
        table_id_or_name: str,
        *,
        archived: bool | Omit = omit,
        include_foreign_ids: bool | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Get details for a draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "include_foreign_ids": include_foreign_ids,
                        "is_get_localized_schema": is_get_localized_schema,
                    },
                    hubdb_get_draft_table_details_by_id_params.HubdbGetDraftTableDetailsByIDParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    async def get_draft_table_row_by_id(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Get a row from the draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return await self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/{row_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, hubdb_get_draft_table_row_by_id_params.HubdbGetDraftTableRowByIDParams
                ),
            ),
            cast_to=HubDBTableRowV3,
        )

    async def get_table_details(
        self,
        table_id_or_name: str,
        *,
        archived: bool | Omit = omit,
        include_foreign_ids: bool | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Get details of a published table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "include_foreign_ids": include_foreign_ids,
                        "is_get_localized_schema": is_get_localized_schema,
                    },
                    hubdb_get_table_details_params.HubdbGetTableDetailsParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    async def get_table_row(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Get a table row

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return await self._get(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/{row_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"archived": archived}, hubdb_get_table_row_params.HubdbGetTableRowParams
                ),
            ),
            cast_to=HubDBTableRowV3,
        )

    async def get_table_rows(
        self,
        table_id_or_name: str,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3:
        """
        Get rows for a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return cast(
            UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3,
            await self._get(
                f"/cms/v3/hubdb/tables/{table_id_or_name}/rows",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "after": after,
                            "archived": archived,
                            "limit": limit,
                            "offset": offset,
                            "properties": properties,
                            "sort": sort,
                        },
                        hubdb_get_table_rows_params.HubdbGetTableRowsParams,
                    ),
                ),
                cast_to=cast(
                    Any, UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def import_draft_table(
        self,
        table_id_or_name: str,
        *,
        config: str | Omit = omit,
        file: FileTypes | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportResult:
        """
        Import data into draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        body = deepcopy_minimal(
            {
                "config": config,
                "file": file,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/import",
            body=await async_maybe_transform(body, hubdb_import_draft_table_params.HubdbImportDraftTableParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportResult,
        )

    async def publish_draft_table(
        self,
        table_id_or_name: str,
        *,
        include_foreign_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Publish a table from draft

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/publish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_foreign_ids": include_foreign_ids},
                    hubdb_publish_draft_table_params.HubdbPublishDraftTableParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    async def purge_draft_table_row(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes a row

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/{row_id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def purge_draft_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Permanently deletes rows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/purge",
            body=await async_maybe_transform(
                {"inputs": inputs}, hubdb_purge_draft_table_rows_params.HubdbPurgeDraftTableRowsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def read_draft_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Get a set of rows from draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/read",
            body=await async_maybe_transform(
                {"inputs": inputs}, hubdb_read_draft_table_rows_params.HubdbReadDraftTableRowsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def read_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Get a set of rows

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, hubdb_read_table_rows_params.HubdbReadTableRowsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def remove_table_version(
        self,
        version_id: int,
        *,
        table_id_or_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a table version

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/versions/{version_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def replace_draft_table_row(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        values: Dict[str, VariantParam],
        child_table_id: int | Omit = omit,
        display_index: int | Omit = omit,
        name: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Replaces an existing row

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return await self._put(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/{row_id}/draft",
            body=await async_maybe_transform(
                {
                    "values": values,
                    "child_table_id": child_table_id,
                    "display_index": display_index,
                    "name": name,
                    "path": path,
                },
                hubdb_replace_draft_table_row_params.HubdbReplaceDraftTableRowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )

    async def replace_draft_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowV3BatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Replace rows in batch in draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/replace",
            body=await async_maybe_transform(
                {"inputs": inputs}, hubdb_replace_draft_table_rows_params.HubdbReplaceDraftTableRowsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def reset_draft_table(
        self,
        table_id_or_name: str,
        *,
        include_foreign_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Reset a draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft/reset",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_foreign_ids": include_foreign_ids},
                    hubdb_reset_draft_table_params.HubdbResetDraftTableParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    async def unpublish_table(
        self,
        table_id_or_name: str,
        *,
        include_foreign_ids: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Unpublish a table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/unpublish",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"include_foreign_ids": include_foreign_ids}, hubdb_unpublish_table_params.HubdbUnpublishTableParams
                ),
            ),
            cast_to=HubDBTableV3,
        )

    async def update_draft_table(
        self,
        table_id_or_name: str,
        *,
        label: str,
        name: str,
        archived: bool | Omit = omit,
        include_foreign_ids: bool | Omit = omit,
        is_get_localized_schema: bool | Omit = omit,
        allow_child_tables: bool | Omit = omit,
        allow_public_api_access: bool | Omit = omit,
        columns: Iterable[ColumnRequestParam] | Omit = omit,
        dynamic_meta_tags: Dict[str, int] | Omit = omit,
        enable_child_table_pages: bool | Omit = omit,
        use_for_pages: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableV3:
        """
        Update an existing table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._patch(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/draft",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "allow_child_tables": allow_child_tables,
                    "allow_public_api_access": allow_public_api_access,
                    "columns": columns,
                    "dynamic_meta_tags": dynamic_meta_tags,
                    "enable_child_table_pages": enable_child_table_pages,
                    "use_for_pages": use_for_pages,
                },
                hubdb_update_draft_table_params.HubdbUpdateDraftTableParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "include_foreign_ids": include_foreign_ids,
                        "is_get_localized_schema": is_get_localized_schema,
                    },
                    hubdb_update_draft_table_params.HubdbUpdateDraftTableParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )

    async def update_draft_table_row(
        self,
        row_id: str,
        *,
        table_id_or_name: str,
        values: Dict[str, VariantParam],
        child_table_id: int | Omit = omit,
        display_index: int | Omit = omit,
        name: str | Omit = omit,
        path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HubDBTableRowV3:
        """
        Updates an existing row

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        if not row_id:
            raise ValueError(f"Expected a non-empty value for `row_id` but received {row_id!r}")
        return await self._patch(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/{row_id}/draft",
            body=await async_maybe_transform(
                {
                    "values": values,
                    "child_table_id": child_table_id,
                    "display_index": display_index,
                    "name": name,
                    "path": path,
                },
                hubdb_update_draft_table_row_params.HubdbUpdateDraftTableRowParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )

    async def update_draft_table_rows(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[HubDBTableRowV3BatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseHubDBTableRowV3:
        """
        Update rows in batch in draft table

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/update",
            body=await async_maybe_transform(
                {"inputs": inputs}, hubdb_update_draft_table_rows_params.HubdbUpdateDraftTableRowsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )


class HubdbResourceWithRawResponse:
    def __init__(self, hubdb: HubdbResource) -> None:
        self._hubdb = hubdb

        self.archive_table = to_raw_response_wrapper(
            hubdb.archive_table,
        )
        self.clone_draft_table = to_raw_response_wrapper(
            hubdb.clone_draft_table,
        )
        self.clone_draft_table_row = to_raw_response_wrapper(
            hubdb.clone_draft_table_row,
        )
        self.clone_draft_table_rows = to_raw_response_wrapper(
            hubdb.clone_draft_table_rows,
        )
        self.create_draft_table_rows = to_raw_response_wrapper(
            hubdb.create_draft_table_rows,
        )
        self.create_table = to_raw_response_wrapper(
            hubdb.create_table,
        )
        self.create_table_row = to_raw_response_wrapper(
            hubdb.create_table_row,
        )
        self.export_draft_table = to_custom_raw_response_wrapper(
            hubdb.export_draft_table,
            BinaryAPIResponse,
        )
        self.export_table = to_custom_raw_response_wrapper(
            hubdb.export_table,
            BinaryAPIResponse,
        )
        self.get_all_draft_tables = to_raw_response_wrapper(
            hubdb.get_all_draft_tables,
        )
        self.get_all_tables = to_raw_response_wrapper(
            hubdb.get_all_tables,
        )
        self.get_draft_table_details_by_id = to_raw_response_wrapper(
            hubdb.get_draft_table_details_by_id,
        )
        self.get_draft_table_row_by_id = to_raw_response_wrapper(
            hubdb.get_draft_table_row_by_id,
        )
        self.get_table_details = to_raw_response_wrapper(
            hubdb.get_table_details,
        )
        self.get_table_row = to_raw_response_wrapper(
            hubdb.get_table_row,
        )
        self.get_table_rows = to_raw_response_wrapper(
            hubdb.get_table_rows,
        )
        self.import_draft_table = to_raw_response_wrapper(
            hubdb.import_draft_table,
        )
        self.publish_draft_table = to_raw_response_wrapper(
            hubdb.publish_draft_table,
        )
        self.purge_draft_table_row = to_raw_response_wrapper(
            hubdb.purge_draft_table_row,
        )
        self.purge_draft_table_rows = to_raw_response_wrapper(
            hubdb.purge_draft_table_rows,
        )
        self.read_draft_table_rows = to_raw_response_wrapper(
            hubdb.read_draft_table_rows,
        )
        self.read_table_rows = to_raw_response_wrapper(
            hubdb.read_table_rows,
        )
        self.remove_table_version = to_raw_response_wrapper(
            hubdb.remove_table_version,
        )
        self.replace_draft_table_row = to_raw_response_wrapper(
            hubdb.replace_draft_table_row,
        )
        self.replace_draft_table_rows = to_raw_response_wrapper(
            hubdb.replace_draft_table_rows,
        )
        self.reset_draft_table = to_raw_response_wrapper(
            hubdb.reset_draft_table,
        )
        self.unpublish_table = to_raw_response_wrapper(
            hubdb.unpublish_table,
        )
        self.update_draft_table = to_raw_response_wrapper(
            hubdb.update_draft_table,
        )
        self.update_draft_table_row = to_raw_response_wrapper(
            hubdb.update_draft_table_row,
        )
        self.update_draft_table_rows = to_raw_response_wrapper(
            hubdb.update_draft_table_rows,
        )

    @cached_property
    def rows(self) -> RowsResourceWithRawResponse:
        return RowsResourceWithRawResponse(self._hubdb.rows)

    @cached_property
    def tables(self) -> TablesResourceWithRawResponse:
        return TablesResourceWithRawResponse(self._hubdb.tables)


class AsyncHubdbResourceWithRawResponse:
    def __init__(self, hubdb: AsyncHubdbResource) -> None:
        self._hubdb = hubdb

        self.archive_table = async_to_raw_response_wrapper(
            hubdb.archive_table,
        )
        self.clone_draft_table = async_to_raw_response_wrapper(
            hubdb.clone_draft_table,
        )
        self.clone_draft_table_row = async_to_raw_response_wrapper(
            hubdb.clone_draft_table_row,
        )
        self.clone_draft_table_rows = async_to_raw_response_wrapper(
            hubdb.clone_draft_table_rows,
        )
        self.create_draft_table_rows = async_to_raw_response_wrapper(
            hubdb.create_draft_table_rows,
        )
        self.create_table = async_to_raw_response_wrapper(
            hubdb.create_table,
        )
        self.create_table_row = async_to_raw_response_wrapper(
            hubdb.create_table_row,
        )
        self.export_draft_table = async_to_custom_raw_response_wrapper(
            hubdb.export_draft_table,
            AsyncBinaryAPIResponse,
        )
        self.export_table = async_to_custom_raw_response_wrapper(
            hubdb.export_table,
            AsyncBinaryAPIResponse,
        )
        self.get_all_draft_tables = async_to_raw_response_wrapper(
            hubdb.get_all_draft_tables,
        )
        self.get_all_tables = async_to_raw_response_wrapper(
            hubdb.get_all_tables,
        )
        self.get_draft_table_details_by_id = async_to_raw_response_wrapper(
            hubdb.get_draft_table_details_by_id,
        )
        self.get_draft_table_row_by_id = async_to_raw_response_wrapper(
            hubdb.get_draft_table_row_by_id,
        )
        self.get_table_details = async_to_raw_response_wrapper(
            hubdb.get_table_details,
        )
        self.get_table_row = async_to_raw_response_wrapper(
            hubdb.get_table_row,
        )
        self.get_table_rows = async_to_raw_response_wrapper(
            hubdb.get_table_rows,
        )
        self.import_draft_table = async_to_raw_response_wrapper(
            hubdb.import_draft_table,
        )
        self.publish_draft_table = async_to_raw_response_wrapper(
            hubdb.publish_draft_table,
        )
        self.purge_draft_table_row = async_to_raw_response_wrapper(
            hubdb.purge_draft_table_row,
        )
        self.purge_draft_table_rows = async_to_raw_response_wrapper(
            hubdb.purge_draft_table_rows,
        )
        self.read_draft_table_rows = async_to_raw_response_wrapper(
            hubdb.read_draft_table_rows,
        )
        self.read_table_rows = async_to_raw_response_wrapper(
            hubdb.read_table_rows,
        )
        self.remove_table_version = async_to_raw_response_wrapper(
            hubdb.remove_table_version,
        )
        self.replace_draft_table_row = async_to_raw_response_wrapper(
            hubdb.replace_draft_table_row,
        )
        self.replace_draft_table_rows = async_to_raw_response_wrapper(
            hubdb.replace_draft_table_rows,
        )
        self.reset_draft_table = async_to_raw_response_wrapper(
            hubdb.reset_draft_table,
        )
        self.unpublish_table = async_to_raw_response_wrapper(
            hubdb.unpublish_table,
        )
        self.update_draft_table = async_to_raw_response_wrapper(
            hubdb.update_draft_table,
        )
        self.update_draft_table_row = async_to_raw_response_wrapper(
            hubdb.update_draft_table_row,
        )
        self.update_draft_table_rows = async_to_raw_response_wrapper(
            hubdb.update_draft_table_rows,
        )

    @cached_property
    def rows(self) -> AsyncRowsResourceWithRawResponse:
        return AsyncRowsResourceWithRawResponse(self._hubdb.rows)

    @cached_property
    def tables(self) -> AsyncTablesResourceWithRawResponse:
        return AsyncTablesResourceWithRawResponse(self._hubdb.tables)


class HubdbResourceWithStreamingResponse:
    def __init__(self, hubdb: HubdbResource) -> None:
        self._hubdb = hubdb

        self.archive_table = to_streamed_response_wrapper(
            hubdb.archive_table,
        )
        self.clone_draft_table = to_streamed_response_wrapper(
            hubdb.clone_draft_table,
        )
        self.clone_draft_table_row = to_streamed_response_wrapper(
            hubdb.clone_draft_table_row,
        )
        self.clone_draft_table_rows = to_streamed_response_wrapper(
            hubdb.clone_draft_table_rows,
        )
        self.create_draft_table_rows = to_streamed_response_wrapper(
            hubdb.create_draft_table_rows,
        )
        self.create_table = to_streamed_response_wrapper(
            hubdb.create_table,
        )
        self.create_table_row = to_streamed_response_wrapper(
            hubdb.create_table_row,
        )
        self.export_draft_table = to_custom_streamed_response_wrapper(
            hubdb.export_draft_table,
            StreamedBinaryAPIResponse,
        )
        self.export_table = to_custom_streamed_response_wrapper(
            hubdb.export_table,
            StreamedBinaryAPIResponse,
        )
        self.get_all_draft_tables = to_streamed_response_wrapper(
            hubdb.get_all_draft_tables,
        )
        self.get_all_tables = to_streamed_response_wrapper(
            hubdb.get_all_tables,
        )
        self.get_draft_table_details_by_id = to_streamed_response_wrapper(
            hubdb.get_draft_table_details_by_id,
        )
        self.get_draft_table_row_by_id = to_streamed_response_wrapper(
            hubdb.get_draft_table_row_by_id,
        )
        self.get_table_details = to_streamed_response_wrapper(
            hubdb.get_table_details,
        )
        self.get_table_row = to_streamed_response_wrapper(
            hubdb.get_table_row,
        )
        self.get_table_rows = to_streamed_response_wrapper(
            hubdb.get_table_rows,
        )
        self.import_draft_table = to_streamed_response_wrapper(
            hubdb.import_draft_table,
        )
        self.publish_draft_table = to_streamed_response_wrapper(
            hubdb.publish_draft_table,
        )
        self.purge_draft_table_row = to_streamed_response_wrapper(
            hubdb.purge_draft_table_row,
        )
        self.purge_draft_table_rows = to_streamed_response_wrapper(
            hubdb.purge_draft_table_rows,
        )
        self.read_draft_table_rows = to_streamed_response_wrapper(
            hubdb.read_draft_table_rows,
        )
        self.read_table_rows = to_streamed_response_wrapper(
            hubdb.read_table_rows,
        )
        self.remove_table_version = to_streamed_response_wrapper(
            hubdb.remove_table_version,
        )
        self.replace_draft_table_row = to_streamed_response_wrapper(
            hubdb.replace_draft_table_row,
        )
        self.replace_draft_table_rows = to_streamed_response_wrapper(
            hubdb.replace_draft_table_rows,
        )
        self.reset_draft_table = to_streamed_response_wrapper(
            hubdb.reset_draft_table,
        )
        self.unpublish_table = to_streamed_response_wrapper(
            hubdb.unpublish_table,
        )
        self.update_draft_table = to_streamed_response_wrapper(
            hubdb.update_draft_table,
        )
        self.update_draft_table_row = to_streamed_response_wrapper(
            hubdb.update_draft_table_row,
        )
        self.update_draft_table_rows = to_streamed_response_wrapper(
            hubdb.update_draft_table_rows,
        )

    @cached_property
    def rows(self) -> RowsResourceWithStreamingResponse:
        return RowsResourceWithStreamingResponse(self._hubdb.rows)

    @cached_property
    def tables(self) -> TablesResourceWithStreamingResponse:
        return TablesResourceWithStreamingResponse(self._hubdb.tables)


class AsyncHubdbResourceWithStreamingResponse:
    def __init__(self, hubdb: AsyncHubdbResource) -> None:
        self._hubdb = hubdb

        self.archive_table = async_to_streamed_response_wrapper(
            hubdb.archive_table,
        )
        self.clone_draft_table = async_to_streamed_response_wrapper(
            hubdb.clone_draft_table,
        )
        self.clone_draft_table_row = async_to_streamed_response_wrapper(
            hubdb.clone_draft_table_row,
        )
        self.clone_draft_table_rows = async_to_streamed_response_wrapper(
            hubdb.clone_draft_table_rows,
        )
        self.create_draft_table_rows = async_to_streamed_response_wrapper(
            hubdb.create_draft_table_rows,
        )
        self.create_table = async_to_streamed_response_wrapper(
            hubdb.create_table,
        )
        self.create_table_row = async_to_streamed_response_wrapper(
            hubdb.create_table_row,
        )
        self.export_draft_table = async_to_custom_streamed_response_wrapper(
            hubdb.export_draft_table,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_table = async_to_custom_streamed_response_wrapper(
            hubdb.export_table,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_all_draft_tables = async_to_streamed_response_wrapper(
            hubdb.get_all_draft_tables,
        )
        self.get_all_tables = async_to_streamed_response_wrapper(
            hubdb.get_all_tables,
        )
        self.get_draft_table_details_by_id = async_to_streamed_response_wrapper(
            hubdb.get_draft_table_details_by_id,
        )
        self.get_draft_table_row_by_id = async_to_streamed_response_wrapper(
            hubdb.get_draft_table_row_by_id,
        )
        self.get_table_details = async_to_streamed_response_wrapper(
            hubdb.get_table_details,
        )
        self.get_table_row = async_to_streamed_response_wrapper(
            hubdb.get_table_row,
        )
        self.get_table_rows = async_to_streamed_response_wrapper(
            hubdb.get_table_rows,
        )
        self.import_draft_table = async_to_streamed_response_wrapper(
            hubdb.import_draft_table,
        )
        self.publish_draft_table = async_to_streamed_response_wrapper(
            hubdb.publish_draft_table,
        )
        self.purge_draft_table_row = async_to_streamed_response_wrapper(
            hubdb.purge_draft_table_row,
        )
        self.purge_draft_table_rows = async_to_streamed_response_wrapper(
            hubdb.purge_draft_table_rows,
        )
        self.read_draft_table_rows = async_to_streamed_response_wrapper(
            hubdb.read_draft_table_rows,
        )
        self.read_table_rows = async_to_streamed_response_wrapper(
            hubdb.read_table_rows,
        )
        self.remove_table_version = async_to_streamed_response_wrapper(
            hubdb.remove_table_version,
        )
        self.replace_draft_table_row = async_to_streamed_response_wrapper(
            hubdb.replace_draft_table_row,
        )
        self.replace_draft_table_rows = async_to_streamed_response_wrapper(
            hubdb.replace_draft_table_rows,
        )
        self.reset_draft_table = async_to_streamed_response_wrapper(
            hubdb.reset_draft_table,
        )
        self.unpublish_table = async_to_streamed_response_wrapper(
            hubdb.unpublish_table,
        )
        self.update_draft_table = async_to_streamed_response_wrapper(
            hubdb.update_draft_table,
        )
        self.update_draft_table_row = async_to_streamed_response_wrapper(
            hubdb.update_draft_table_row,
        )
        self.update_draft_table_rows = async_to_streamed_response_wrapper(
            hubdb.update_draft_table_rows,
        )

    @cached_property
    def rows(self) -> AsyncRowsResourceWithStreamingResponse:
        return AsyncRowsResourceWithStreamingResponse(self._hubdb.rows)

    @cached_property
    def tables(self) -> AsyncTablesResourceWithStreamingResponse:
        return AsyncTablesResourceWithStreamingResponse(self._hubdb.tables)
