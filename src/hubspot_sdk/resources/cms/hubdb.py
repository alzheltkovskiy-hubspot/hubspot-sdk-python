# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Mapping, Iterable, cast
from datetime import datetime

import httpx

from ..._types import (
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
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
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
from ...types.cms import (
    hubdb_get_params,
    hubdb_list_params,
    hubdb_create_params,
    hubdb_export_params,
    hubdb_get_draft_params,
    hubdb_unpublish_params,
    hubdb_list_draft_params,
    hubdb_read_batch_params,
    hubdb_clone_batch_params,
    hubdb_clone_draft_params,
    hubdb_list_drafts_params,
    hubdb_purge_batch_params,
    hubdb_reset_draft_params,
    hubdb_create_batch_params,
    hubdb_create_table_params,
    hubdb_export_draft_params,
    hubdb_export_table_params,
    hubdb_import_draft_params,
    hubdb_update_batch_params,
    hubdb_update_draft_params,
    hubdb_get_table_row_params,
    hubdb_publish_draft_params,
    hubdb_replace_batch_params,
    hubdb_replace_draft_params,
    hubdb_get_all_tables_params,
    hubdb_get_table_rows_params,
    hubdb_read_table_rows_params,
    hubdb_unpublish_table_params,
    hubdb_create_table_row_params,
    hubdb_read_draft_batch_params,
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
from ...pagination import SyncPage, AsyncPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cms.import_result import ImportResult
from ...types.cms.variant_param import VariantParam
from ...types.cms.hub_db_table_v3 import HubDBTableV3
from ...types.cms.hub_db_table_row_v3 import HubDBTableRowV3
from ...types.cms.column_request_param import ColumnRequestParam
from ...types.cms.hub_db_table_row_v3_request_param import HubDBTableRowV3RequestParam
from ...types.cms.batch_response_hub_db_table_row_v3 import BatchResponseHubDBTableRowV3
from ...types.cms.hub_db_table_row_batch_clone_request_param import HubDBTableRowBatchCloneRequestParam
from ...types.cms.hub_db_table_row_v3_batch_update_request_param import HubDBTableRowV3BatchUpdateRequestParam
from ...types.cms.collection_response_with_total_hub_db_table_v3_forward_paging import (
    CollectionResponseWithTotalHubDBTableV3ForwardPaging,
)
from ...types.cms.unified_collection_response_with_total_base_hub_db_table_row_v3 import (
    UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3,
)

__all__ = ["HubdbResource", "AsyncHubdbResource"]


class HubdbResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HubdbResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return HubdbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HubdbResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#with_streaming_response
        """
        return HubdbResourceWithStreamingResponse(self)

    def create(
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
        """Creates a new draft HubDB table given a JSON schema.

        The table name and label
        should be unique for each account.

        Args:
          label: Label of the table

          name: Name of the table

          allow_child_tables: Specifies whether child tables can be created

          allow_public_api_access: Specifies whether the table can be read by public without authorization

          columns: List of columns in the table

          dynamic_meta_tags: Specifies the key value pairs of the
              [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
              with the associated column IDs.

          enable_child_table_pages: Specifies creation of multi-level dynamic pages using child tables

          use_for_pages: Specifies whether the table can be used for creation of dynamic pages

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
                hubdb_create_params.HubdbCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
        )

    def list(
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
        Returns the details for the published version of each table defined in an
        account, including column definitions.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived tables. Defaults to `false`.

          created_after: Only return tables created after the specified time.

          created_at: Only return tables created at exactly the specified time.

          created_before: Only return tables created before the specified time.

          limit: The maximum number of results to return. Default is 1000.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return tables last updated after the specified time.

          updated_at: Only return tables last updated at exactly the specified time.

          updated_before: Only return tables last updated before the specified time.

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
                    hubdb_list_params.HubdbListParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalHubDBTableV3ForwardPaging,
        )

    def archive(
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
        """Archive (soft delete) an existing HubDB table.

        This archives both the published
        and draft versions.

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
        """Archive (soft delete) an existing HubDB table.

        This archives both the published
        and draft versions.

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

    def clone_batch(
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
        Clones rows in the draft version of the specified table, given a set of row ids.
        Maximum of 100 row ids per call.

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
            body=maybe_transform({"inputs": inputs}, hubdb_clone_batch_params.HubdbCloneBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def clone_draft(
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
        """Clone an existing HubDB table.

        The `newName` and `newLabel` of the new table can
        be sent as JSON in the request body. This will create the cloned table as a
        draft.

        Args:
          copy_rows: Specifies whether to copy the rows during clone

          new_label: The new label for the cloned table

          new_name: The new name for the cloned table

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
                hubdb_clone_draft_params.HubdbCloneDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
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
        """Clone an existing HubDB table.

        The `newName` and `newLabel` of the new table can
        be sent as JSON in the request body. This will create the cloned table as a
        draft.

        Args:
          copy_rows: Specifies whether to copy the rows during clone

          new_label: The new label for the cloned table

          new_name: The new name for the cloned table

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
        Clones a single row in the draft version of a table.

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
        Clones rows in the draft version of the specified table, given a set of row ids.
        Maximum of 100 row ids per call.

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

    def create_batch(
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
        Creates rows in the draft version of the specified table, given an array of row
        objects. Maximum of 100 row object per call. See the overview section for more
        details with an example.

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
            body=maybe_transform({"inputs": inputs}, hubdb_create_batch_params.HubdbCreateBatchParams),
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
        Creates rows in the draft version of the specified table, given an array of row
        objects. Maximum of 100 row object per call. See the overview section for more
        details with an example.

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
        """Creates a new draft HubDB table given a JSON schema.

        The table name and label
        should be unique for each account.

        Args:
          label: Label of the table

          name: Name of the table

          allow_child_tables: Specifies whether child tables can be created

          allow_public_api_access: Specifies whether the table can be read by public without authorization

          columns: List of columns in the table

          dynamic_meta_tags: Specifies the key value pairs of the
              [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
              with the associated column IDs.

          enable_child_table_pages: Specifies creation of multi-level dynamic pages using child tables

          use_for_pages: Specifies whether the table can be used for creation of dynamic pages

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
        """Add a new row to a HubDB table.

        New rows will be added to the draft version of
        the table. Use the `/publish` endpoint to push these changes to published
        version.

        Args:
          values: List of key value pairs with the column name and column value

          child_table_id: Specifies the value for the column child table id

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

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

    def delete_draft(
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
        Permanently deletes a row from a table's draft version.

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

    def delete_version(
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
        Delete a specific version of a table

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

    def export(
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
        Exports the published version of a table in a specified format.

        Args:
          format: The file format to export. Possible values include `CSV`, `XLSX`, and `XLS`.

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
                query=maybe_transform({"format": format}, hubdb_export_params.HubdbExportParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def export_draft(
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
        Exports the draft version of a table to CSV / EXCEL format.

        Args:
          format: The file format to export. Possible values include `CSV`, `XLSX`, and `XLS`.

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
                query=maybe_transform({"format": format}, hubdb_export_draft_params.HubdbExportDraftParams),
            ),
            cast_to=BinaryAPIResponse,
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
        Exports the draft version of a table to CSV / EXCEL format.

        Args:
          format: The file format to export. Possible values include `CSV`, `XLSX`, and `XLS`.

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
        Exports the published version of a table in a specified format.

        Args:
          format: The file format to export. Possible values include `CSV`, `XLSX`, and `XLS`.

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

    def get(
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
        """Returns the details for the published version of the specified table.

        This will
        include the definitions for the columns in the table and the number of rows in
        the table.

        **Note:** This endpoint can be accessed without any authentication if the table
        is set to be allowed for public access. To do so, you'll need to include the
        HubSpot account ID in a `portalId` query parameter.

        Args:
          archived: Set this to `true` to return details for an archived table. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

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
                    hubdb_get_params.HubdbGetParams,
                ),
            ),
            cast_to=HubDBTableV3,
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
    ) -> SyncPage[HubDBTableV3]:
        """
        Returns the details for each draft table defined in the specified account,
        including column definitions.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived tables. Defaults to `false`.

          created_after: Only return tables created after the specified time.

          created_at: Only return tables created at exactly the specified time.

          created_before: Only return tables created before the specified time.

          limit: The maximum number of results to return. Default is 1000.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return tables last updated after the specified time.

          updated_at: Only return tables last updated at exactly the specified time.

          updated_before: Only return tables last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/hubdb/tables/draft",
            page=SyncPage[HubDBTableV3],
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
            model=HubDBTableV3,
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
    ) -> SyncPage[HubDBTableV3]:
        """
        Returns the details for the published version of each table defined in an
        account, including column definitions.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived tables. Defaults to `false`.

          created_after: Only return tables created after the specified time.

          created_at: Only return tables created at exactly the specified time.

          created_before: Only return tables created before the specified time.

          limit: The maximum number of results to return. Default is 1000.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return tables last updated after the specified time.

          updated_at: Only return tables last updated at exactly the specified time.

          updated_before: Only return tables last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/hubdb/tables",
            page=SyncPage[HubDBTableV3],
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
            model=HubDBTableV3,
        )

    def get_draft(
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
        """Get the details for the draft version of a specific HubDB table.

        This will
        include the definitions for the columns in the table and the number of rows in
        the table.

        Args:
          archived: Set this to `true` to return an archived table. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

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
                    hubdb_get_draft_params.HubdbGetDraftParams,
                ),
            ),
            cast_to=HubDBTableV3,
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
        """Get the details for the draft version of a specific HubDB table.

        This will
        include the definitions for the columns in the table and the number of rows in
        the table.

        Args:
          archived: Set this to `true` to return an archived table. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

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
        Get a single row by ID from a table's draft version.

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
        """Returns the details for the published version of the specified table.

        This will
        include the definitions for the columns in the table and the number of rows in
        the table.

        **Note:** This endpoint can be accessed without any authentication if the table
        is set to be allowed for public access. To do so, you'll need to include the
        HubSpot account ID in a `portalId` query parameter.

        Args:
          archived: Set this to `true` to return details for an archived table. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

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
        """Get a single row by ID from the published version of a table.

        **Note:** This
        endpoint can be accessed without any authentication, if the table is set to be
        allowed for public access.

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
    ) -> SyncPage[object]:
        """Returns a set of rows in the published version of the specified table.

        Row
        results can be filtered and sorted. Filtering and sorting options will be sent
        as query parameters to the API request. For example, by adding the query
        parameters `column1__gt=5&sort=-column1`, API returns the rows with values for
        column `column1` greater than 5 and in the descending order of `column1` values.
        Refer to the
        [overview section](https://developers.hubspot.com/docs/api/cms/hubdb#filtering-and-sorting-table-rows)
        for detailed filtering and sorting options. **Note:** This endpoint can be
        accessed without any authentication, if the table is set to be allowed for
        public access.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          limit: The maximum number of results to return. Default is `1000`.

          properties: Specify the column names to get results containing only the required columns
              instead of all column details.

          sort: Specifies the column names to sort the results by. See the above description for
              more details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._get_api_list(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows",
            page=SyncPage[object],
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
            model=object,
        )

    def import_draft(
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
        """Import the contents of a CSV file into an existing HubDB table.

        The data will
        always be imported into the draft version of the table. Use the `/publish`
        endpoint to push these changes to the published version. This endpoint takes a
        multi-part POST request. The first part will be a set of JSON-formatted options
        for the import and you can specify this with the name as `config`. The second
        part will be the CSV file you want to import and you can specify this with the
        name as `file`. Refer the
        [overview section](https://developers.hubspot.com/docs/api/cms/hubdb#importing-tables)
        to check the details and format of the JSON-formatted options for the import.

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
            body=maybe_transform(body, hubdb_import_draft_params.HubdbImportDraftParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportResult,
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
        """Import the contents of a CSV file into an existing HubDB table.

        The data will
        always be imported into the draft version of the table. Use the `/publish`
        endpoint to push these changes to the published version. This endpoint takes a
        multi-part POST request. The first part will be a set of JSON-formatted options
        for the import and you can specify this with the name as `config`. The second
        part will be the CSV file you want to import and you can specify this with the
        name as `file`. Refer the
        [overview section](https://developers.hubspot.com/docs/api/cms/hubdb#importing-tables)
        to check the details and format of the JSON-formatted options for the import.

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

    def list_draft(
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
        """Returns rows in the draft version of the specified table.

        Row results can be
        filtered and sorted. Filtering and sorting options will be sent as query
        parameters to the API request. For example, by adding the query parameters
        `column1__gt=5&sort=-column1`, API returns the rows with values for column
        `column1` greater than 5 and in the descending order of `column1` values. Refer
        to the
        [overview section](https://developers.hubspot.com/docs/api/cms/hubdb#filtering-and-sorting-table-rows)
        for detailed filtering and sorting options.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          limit: The maximum number of results to return. Default is `1000`.

          properties: Specify the column names to get results containing only the required columns
              instead of all column details. If you want to include multiple columns in the
              result, use this query param as many times.

          sort: Specifies the column names to sort the results by.

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
                f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft",
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
                        hubdb_list_draft_params.HubdbListDraftParams,
                    ),
                ),
                cast_to=cast(
                    Any, UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list_drafts(
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
        Returns the details for each draft table defined in the specified account,
        including column definitions.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived tables. Defaults to `false`.

          created_after: Only return tables created after the specified time.

          created_at: Only return tables created at exactly the specified time.

          created_before: Only return tables created before the specified time.

          limit: The maximum number of results to return. Default is 1000.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return tables last updated after the specified time.

          updated_at: Only return tables last updated at exactly the specified time.

          updated_before: Only return tables last updated before the specified time.

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
                    hubdb_list_drafts_params.HubdbListDraftsParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalHubDBTableV3ForwardPaging,
        )

    def publish_draft(
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
        Publishes the table by copying the data and table schema changes from draft
        version to the published version, meaning any website pages using data from the
        table will be updated.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

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
                    {"include_foreign_ids": include_foreign_ids}, hubdb_publish_draft_params.HubdbPublishDraftParams
                ),
            ),
            cast_to=HubDBTableV3,
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
        Publishes the table by copying the data and table schema changes from draft
        version to the published version, meaning any website pages using data from the
        table will be updated.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

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

    def purge_batch(
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
        Permanently deletes rows from the draft version of the table, given a set of row
        IDs. Maximum of 100 row IDs per call.

        Args:
          inputs: Strings to input.

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
            body=maybe_transform({"inputs": inputs}, hubdb_purge_batch_params.HubdbPurgeBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Permanently deletes a row from a table's draft version.

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
        Permanently deletes rows from the draft version of the table, given a set of row
        IDs. Maximum of 100 row IDs per call.

        Args:
          inputs: Strings to input.

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

    def read_batch(
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
        Returns rows in the published version of the specified table, given a set of row
        IDs. **Note:** This endpoint can be accessed without any authentication if the
        table is set to be allowed for public access.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/batch/read",
            body=maybe_transform({"inputs": inputs}, hubdb_read_batch_params.HubdbReadBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def read_draft_batch(
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
        Returns rows in the draft version of the specified table, given a set of row
        IDs.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft/batch/read",
            body=maybe_transform({"inputs": inputs}, hubdb_read_draft_batch_params.HubdbReadDraftBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
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
        Returns rows in the draft version of the specified table, given a set of row
        IDs.

        Args:
          inputs: Strings to input.

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
        Returns rows in the published version of the specified table, given a set of row
        IDs. **Note:** This endpoint can be accessed without any authentication if the
        table is set to be allowed for public access.

        Args:
          inputs: Strings to input.

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
        Delete a specific version of a table

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

    def replace_batch(
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
        Replaces multiple rows as a batch in the draft version of the table, with a
        maximum of 100 rows per call. See the endpoint
        `PUT /tables/{tableIdOrName}/rows/{rowId}/draft` for details on updating a
        single row.

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
            body=maybe_transform({"inputs": inputs}, hubdb_replace_batch_params.HubdbReplaceBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def replace_draft(
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
        """Replace a single row in the draft version of a table.

        All column values must be
        specified. If a column has a value in the target table and this request doesn't
        define that value, it will be deleted. See the "Create a row" endpoint for
        instructions on how to format the JSON row definitions.

        Args:
          values: List of key value pairs with the column name and column value

          child_table_id: Specifies the value for the column child table id

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

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
                hubdb_replace_draft_params.HubdbReplaceDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
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
        """Replace a single row in the draft version of a table.

        All column values must be
        specified. If a column has a value in the target table and this request doesn't
        define that value, it will be deleted. See the "Create a row" endpoint for
        instructions on how to format the JSON row definitions.

        Args:
          values: List of key value pairs with the column name and column value

          child_table_id: Specifies the value for the column child table id

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

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
        Replaces multiple rows as a batch in the draft version of the table, with a
        maximum of 100 rows per call. See the endpoint
        `PUT /tables/{tableIdOrName}/rows/{rowId}/draft` for details on updating a
        single row.

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

    def reset_draft(
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
        Replaces the data in the draft version of the table with values from the
        published version. Any unpublished changes in the draft will be lost after this
        call is made.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

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
                    {"include_foreign_ids": include_foreign_ids}, hubdb_reset_draft_params.HubdbResetDraftParams
                ),
            ),
            cast_to=HubDBTableV3,
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
        Replaces the data in the draft version of the table with values from the
        published version. Any unpublished changes in the draft will be lost after this
        call is made.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

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

    def unpublish(
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
        Unpublishes the table, meaning any website pages using data from the table will
        not render any data.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

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
                    {"include_foreign_ids": include_foreign_ids}, hubdb_unpublish_params.HubdbUnpublishParams
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
        Unpublishes the table, meaning any website pages using data from the table will
        not render any data.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

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

    def update_batch(
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
        Updates multiple rows as a batch in the draft version of the table, with a
        maximum of 100 rows per call. See the endpoint
        `PATCH /tables/{tableIdOrName}/rows/{rowId}/draft` for details on updating a
        single row.

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
            body=maybe_transform({"inputs": inputs}, hubdb_update_batch_params.HubdbUpdateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    def update_draft(
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
        """Update an existing HubDB table.

        You can use this endpoint to add or remove
        columns to the table as well as restore an archived table. Tables updated using
        the endpoint will only modify the draft verion of the table. Use the `/publish`
        endpoint to push all the changes to the published version. To restore a table,
        include the query parameter `archived=true` and `"archived": false` in the json
        body. **Note:** You need to include all the columns in the input when you are
        adding/removing/updating a column. If you do not include an already existing
        column in the request, it will be deleted.

        Args:
          label: Label of the table

          name: Name of the table

          archived: Specifies whether to return archived tables. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

          allow_child_tables: Specifies whether child tables can be created

          allow_public_api_access: Specifies whether the table can be read by public without authorization

          columns: List of columns in the table

          dynamic_meta_tags: Specifies the key value pairs of the
              [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
              with the associated column IDs.

          enable_child_table_pages: Specifies creation of multi-level dynamic pages using child tables

          use_for_pages: Specifies whether the table can be used for creation of dynamic pages

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
                hubdb_update_draft_params.HubdbUpdateDraftParams,
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
                    hubdb_update_draft_params.HubdbUpdateDraftParams,
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
        """Update an existing HubDB table.

        You can use this endpoint to add or remove
        columns to the table as well as restore an archived table. Tables updated using
        the endpoint will only modify the draft verion of the table. Use the `/publish`
        endpoint to push all the changes to the published version. To restore a table,
        include the query parameter `archived=true` and `"archived": false` in the json
        body. **Note:** You need to include all the columns in the input when you are
        adding/removing/updating a column. If you do not include an already existing
        column in the request, it will be deleted.

        Args:
          label: Label of the table

          name: Name of the table

          archived: Specifies whether to return archived tables. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

          allow_child_tables: Specifies whether child tables can be created

          allow_public_api_access: Specifies whether the table can be read by public without authorization

          columns: List of columns in the table

          dynamic_meta_tags: Specifies the key value pairs of the
              [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
              with the associated column IDs.

          enable_child_table_pages: Specifies creation of multi-level dynamic pages using child tables

          use_for_pages: Specifies whether the table can be used for creation of dynamic pages

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
        """Sparse updates a single row in the table's draft version.

        All the column values
        need not be specified. Only the columns or fields that needs to be modified can
        be specified. See the "Create a row" endpoint for instructions on how to format
        the JSON row definitions.

        Args:
          values: List of key value pairs with the column name and column value

          child_table_id: Specifies the value for the column child table id

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

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
        Updates multiple rows as a batch in the draft version of the table, with a
        maximum of 100 rows per call. See the endpoint
        `PATCH /tables/{tableIdOrName}/rows/{rowId}/draft` for details on updating a
        single row.

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
    def with_raw_response(self) -> AsyncHubdbResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHubdbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHubdbResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncHubdbResourceWithStreamingResponse(self)

    async def create(
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
        """Creates a new draft HubDB table given a JSON schema.

        The table name and label
        should be unique for each account.

        Args:
          label: Label of the table

          name: Name of the table

          allow_child_tables: Specifies whether child tables can be created

          allow_public_api_access: Specifies whether the table can be read by public without authorization

          columns: List of columns in the table

          dynamic_meta_tags: Specifies the key value pairs of the
              [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
              with the associated column IDs.

          enable_child_table_pages: Specifies creation of multi-level dynamic pages using child tables

          use_for_pages: Specifies whether the table can be used for creation of dynamic pages

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
                hubdb_create_params.HubdbCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
        )

    async def list(
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
        Returns the details for the published version of each table defined in an
        account, including column definitions.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived tables. Defaults to `false`.

          created_after: Only return tables created after the specified time.

          created_at: Only return tables created at exactly the specified time.

          created_before: Only return tables created before the specified time.

          limit: The maximum number of results to return. Default is 1000.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return tables last updated after the specified time.

          updated_at: Only return tables last updated at exactly the specified time.

          updated_before: Only return tables last updated before the specified time.

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
                    hubdb_list_params.HubdbListParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalHubDBTableV3ForwardPaging,
        )

    async def archive(
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
        """Archive (soft delete) an existing HubDB table.

        This archives both the published
        and draft versions.

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
        """Archive (soft delete) an existing HubDB table.

        This archives both the published
        and draft versions.

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

    async def clone_batch(
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
        Clones rows in the draft version of the specified table, given a set of row ids.
        Maximum of 100 row ids per call.

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
            body=await async_maybe_transform({"inputs": inputs}, hubdb_clone_batch_params.HubdbCloneBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def clone_draft(
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
        """Clone an existing HubDB table.

        The `newName` and `newLabel` of the new table can
        be sent as JSON in the request body. This will create the cloned table as a
        draft.

        Args:
          copy_rows: Specifies whether to copy the rows during clone

          new_label: The new label for the cloned table

          new_name: The new name for the cloned table

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
                hubdb_clone_draft_params.HubdbCloneDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
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
        """Clone an existing HubDB table.

        The `newName` and `newLabel` of the new table can
        be sent as JSON in the request body. This will create the cloned table as a
        draft.

        Args:
          copy_rows: Specifies whether to copy the rows during clone

          new_label: The new label for the cloned table

          new_name: The new name for the cloned table

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
        Clones a single row in the draft version of a table.

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
        Clones rows in the draft version of the specified table, given a set of row ids.
        Maximum of 100 row ids per call.

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

    async def create_batch(
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
        Creates rows in the draft version of the specified table, given an array of row
        objects. Maximum of 100 row object per call. See the overview section for more
        details with an example.

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
            body=await async_maybe_transform({"inputs": inputs}, hubdb_create_batch_params.HubdbCreateBatchParams),
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
        Creates rows in the draft version of the specified table, given an array of row
        objects. Maximum of 100 row object per call. See the overview section for more
        details with an example.

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
        """Creates a new draft HubDB table given a JSON schema.

        The table name and label
        should be unique for each account.

        Args:
          label: Label of the table

          name: Name of the table

          allow_child_tables: Specifies whether child tables can be created

          allow_public_api_access: Specifies whether the table can be read by public without authorization

          columns: List of columns in the table

          dynamic_meta_tags: Specifies the key value pairs of the
              [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
              with the associated column IDs.

          enable_child_table_pages: Specifies creation of multi-level dynamic pages using child tables

          use_for_pages: Specifies whether the table can be used for creation of dynamic pages

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
        """Add a new row to a HubDB table.

        New rows will be added to the draft version of
        the table. Use the `/publish` endpoint to push these changes to published
        version.

        Args:
          values: List of key value pairs with the column name and column value

          child_table_id: Specifies the value for the column child table id

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

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

    async def delete_draft(
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
        Permanently deletes a row from a table's draft version.

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

    async def delete_version(
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
        Delete a specific version of a table

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

    async def export(
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
        Exports the published version of a table in a specified format.

        Args:
          format: The file format to export. Possible values include `CSV`, `XLSX`, and `XLS`.

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
                query=await async_maybe_transform({"format": format}, hubdb_export_params.HubdbExportParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def export_draft(
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
        Exports the draft version of a table to CSV / EXCEL format.

        Args:
          format: The file format to export. Possible values include `CSV`, `XLSX`, and `XLS`.

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
                query=await async_maybe_transform({"format": format}, hubdb_export_draft_params.HubdbExportDraftParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
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
        Exports the draft version of a table to CSV / EXCEL format.

        Args:
          format: The file format to export. Possible values include `CSV`, `XLSX`, and `XLS`.

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
        Exports the published version of a table in a specified format.

        Args:
          format: The file format to export. Possible values include `CSV`, `XLSX`, and `XLS`.

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

    async def get(
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
        """Returns the details for the published version of the specified table.

        This will
        include the definitions for the columns in the table and the number of rows in
        the table.

        **Note:** This endpoint can be accessed without any authentication if the table
        is set to be allowed for public access. To do so, you'll need to include the
        HubSpot account ID in a `portalId` query parameter.

        Args:
          archived: Set this to `true` to return details for an archived table. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

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
                    hubdb_get_params.HubdbGetParams,
                ),
            ),
            cast_to=HubDBTableV3,
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
    ) -> AsyncPaginator[HubDBTableV3, AsyncPage[HubDBTableV3]]:
        """
        Returns the details for each draft table defined in the specified account,
        including column definitions.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived tables. Defaults to `false`.

          created_after: Only return tables created after the specified time.

          created_at: Only return tables created at exactly the specified time.

          created_before: Only return tables created before the specified time.

          limit: The maximum number of results to return. Default is 1000.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return tables last updated after the specified time.

          updated_at: Only return tables last updated at exactly the specified time.

          updated_before: Only return tables last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/hubdb/tables/draft",
            page=AsyncPage[HubDBTableV3],
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
            model=HubDBTableV3,
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
    ) -> AsyncPaginator[HubDBTableV3, AsyncPage[HubDBTableV3]]:
        """
        Returns the details for the published version of each table defined in an
        account, including column definitions.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived tables. Defaults to `false`.

          created_after: Only return tables created after the specified time.

          created_at: Only return tables created at exactly the specified time.

          created_before: Only return tables created before the specified time.

          limit: The maximum number of results to return. Default is 1000.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return tables last updated after the specified time.

          updated_at: Only return tables last updated at exactly the specified time.

          updated_before: Only return tables last updated before the specified time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cms/v3/hubdb/tables",
            page=AsyncPage[HubDBTableV3],
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
            model=HubDBTableV3,
        )

    async def get_draft(
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
        """Get the details for the draft version of a specific HubDB table.

        This will
        include the definitions for the columns in the table and the number of rows in
        the table.

        Args:
          archived: Set this to `true` to return an archived table. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

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
                    hubdb_get_draft_params.HubdbGetDraftParams,
                ),
            ),
            cast_to=HubDBTableV3,
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
        """Get the details for the draft version of a specific HubDB table.

        This will
        include the definitions for the columns in the table and the number of rows in
        the table.

        Args:
          archived: Set this to `true` to return an archived table. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

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
        Get a single row by ID from a table's draft version.

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
        """Returns the details for the published version of the specified table.

        This will
        include the definitions for the columns in the table and the number of rows in
        the table.

        **Note:** This endpoint can be accessed without any authentication if the table
        is set to be allowed for public access. To do so, you'll need to include the
        HubSpot account ID in a `portalId` query parameter.

        Args:
          archived: Set this to `true` to return details for an archived table. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

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
        """Get a single row by ID from the published version of a table.

        **Note:** This
        endpoint can be accessed without any authentication, if the table is set to be
        allowed for public access.

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
    ) -> AsyncPaginator[object, AsyncPage[object]]:
        """Returns a set of rows in the published version of the specified table.

        Row
        results can be filtered and sorted. Filtering and sorting options will be sent
        as query parameters to the API request. For example, by adding the query
        parameters `column1__gt=5&sort=-column1`, API returns the rows with values for
        column `column1` greater than 5 and in the descending order of `column1` values.
        Refer to the
        [overview section](https://developers.hubspot.com/docs/api/cms/hubdb#filtering-and-sorting-table-rows)
        for detailed filtering and sorting options. **Note:** This endpoint can be
        accessed without any authentication, if the table is set to be allowed for
        public access.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          limit: The maximum number of results to return. Default is `1000`.

          properties: Specify the column names to get results containing only the required columns
              instead of all column details.

          sort: Specifies the column names to sort the results by. See the above description for
              more details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return self._get_api_list(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows",
            page=AsyncPage[object],
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
            model=object,
        )

    async def import_draft(
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
        """Import the contents of a CSV file into an existing HubDB table.

        The data will
        always be imported into the draft version of the table. Use the `/publish`
        endpoint to push these changes to the published version. This endpoint takes a
        multi-part POST request. The first part will be a set of JSON-formatted options
        for the import and you can specify this with the name as `config`. The second
        part will be the CSV file you want to import and you can specify this with the
        name as `file`. Refer the
        [overview section](https://developers.hubspot.com/docs/api/cms/hubdb#importing-tables)
        to check the details and format of the JSON-formatted options for the import.

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
            body=await async_maybe_transform(body, hubdb_import_draft_params.HubdbImportDraftParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportResult,
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
        """Import the contents of a CSV file into an existing HubDB table.

        The data will
        always be imported into the draft version of the table. Use the `/publish`
        endpoint to push these changes to the published version. This endpoint takes a
        multi-part POST request. The first part will be a set of JSON-formatted options
        for the import and you can specify this with the name as `config`. The second
        part will be the CSV file you want to import and you can specify this with the
        name as `file`. Refer the
        [overview section](https://developers.hubspot.com/docs/api/cms/hubdb#importing-tables)
        to check the details and format of the JSON-formatted options for the import.

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

    async def list_draft(
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
        """Returns rows in the draft version of the specified table.

        Row results can be
        filtered and sorted. Filtering and sorting options will be sent as query
        parameters to the API request. For example, by adding the query parameters
        `column1__gt=5&sort=-column1`, API returns the rows with values for column
        `column1` greater than 5 and in the descending order of `column1` values. Refer
        to the
        [overview section](https://developers.hubspot.com/docs/api/cms/hubdb#filtering-and-sorting-table-rows)
        for detailed filtering and sorting options.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          limit: The maximum number of results to return. Default is `1000`.

          properties: Specify the column names to get results containing only the required columns
              instead of all column details. If you want to include multiple columns in the
              result, use this query param as many times.

          sort: Specifies the column names to sort the results by.

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
                f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/draft",
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
                        hubdb_list_draft_params.HubdbListDraftParams,
                    ),
                ),
                cast_to=cast(
                    Any, UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list_drafts(
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
        Returns the details for each draft table defined in the specified account,
        including column definitions.

        Args:
          after: The cursor token value to get the next set of results. You can get this from the
              `paging.next.after` JSON property of a paged response containing more results.

          archived: Specifies whether to return archived tables. Defaults to `false`.

          created_after: Only return tables created after the specified time.

          created_at: Only return tables created at exactly the specified time.

          created_before: Only return tables created before the specified time.

          limit: The maximum number of results to return. Default is 1000.

          sort: Specifies which fields to use for sorting results. Valid fields are `name`,
              `createdAt`, `updatedAt`, `createdBy`, `updatedBy`. `createdAt` will be used by
              default.

          updated_after: Only return tables last updated after the specified time.

          updated_at: Only return tables last updated at exactly the specified time.

          updated_before: Only return tables last updated before the specified time.

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
                    hubdb_list_drafts_params.HubdbListDraftsParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalHubDBTableV3ForwardPaging,
        )

    async def publish_draft(
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
        Publishes the table by copying the data and table schema changes from draft
        version to the published version, meaning any website pages using data from the
        table will be updated.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

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
                    {"include_foreign_ids": include_foreign_ids}, hubdb_publish_draft_params.HubdbPublishDraftParams
                ),
            ),
            cast_to=HubDBTableV3,
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
        Publishes the table by copying the data and table schema changes from draft
        version to the published version, meaning any website pages using data from the
        table will be updated.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

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

    async def purge_batch(
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
        Permanently deletes rows from the draft version of the table, given a set of row
        IDs. Maximum of 100 row IDs per call.

        Args:
          inputs: Strings to input.

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
            body=await async_maybe_transform({"inputs": inputs}, hubdb_purge_batch_params.HubdbPurgeBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        Permanently deletes a row from a table's draft version.

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
        Permanently deletes rows from the draft version of the table, given a set of row
        IDs. Maximum of 100 row IDs per call.

        Args:
          inputs: Strings to input.

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

    async def read_batch(
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
        Returns rows in the published version of the specified table, given a set of row
        IDs. **Note:** This endpoint can be accessed without any authentication if the
        table is set to be allowed for public access.

        Args:
          inputs: Strings to input.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id_or_name:
            raise ValueError(f"Expected a non-empty value for `table_id_or_name` but received {table_id_or_name!r}")
        return await self._post(
            f"/cms/v3/hubdb/tables/{table_id_or_name}/rows/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, hubdb_read_batch_params.HubdbReadBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def read_draft_batch(
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
        Returns rows in the draft version of the specified table, given a set of row
        IDs.

        Args:
          inputs: Strings to input.

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
                {"inputs": inputs}, hubdb_read_draft_batch_params.HubdbReadDraftBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
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
        Returns rows in the draft version of the specified table, given a set of row
        IDs.

        Args:
          inputs: Strings to input.

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
        Returns rows in the published version of the specified table, given a set of row
        IDs. **Note:** This endpoint can be accessed without any authentication if the
        table is set to be allowed for public access.

        Args:
          inputs: Strings to input.

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
        Delete a specific version of a table

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

    async def replace_batch(
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
        Replaces multiple rows as a batch in the draft version of the table, with a
        maximum of 100 rows per call. See the endpoint
        `PUT /tables/{tableIdOrName}/rows/{rowId}/draft` for details on updating a
        single row.

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
            body=await async_maybe_transform({"inputs": inputs}, hubdb_replace_batch_params.HubdbReplaceBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def replace_draft(
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
        """Replace a single row in the draft version of a table.

        All column values must be
        specified. If a column has a value in the target table and this request doesn't
        define that value, it will be deleted. See the "Create a row" endpoint for
        instructions on how to format the JSON row definitions.

        Args:
          values: List of key value pairs with the column name and column value

          child_table_id: Specifies the value for the column child table id

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

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
                hubdb_replace_draft_params.HubdbReplaceDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
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
        """Replace a single row in the draft version of a table.

        All column values must be
        specified. If a column has a value in the target table and this request doesn't
        define that value, it will be deleted. See the "Create a row" endpoint for
        instructions on how to format the JSON row definitions.

        Args:
          values: List of key value pairs with the column name and column value

          child_table_id: Specifies the value for the column child table id

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

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
        Replaces multiple rows as a batch in the draft version of the table, with a
        maximum of 100 rows per call. See the endpoint
        `PUT /tables/{tableIdOrName}/rows/{rowId}/draft` for details on updating a
        single row.

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

    async def reset_draft(
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
        Replaces the data in the draft version of the table with values from the
        published version. Any unpublished changes in the draft will be lost after this
        call is made.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

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
                    {"include_foreign_ids": include_foreign_ids}, hubdb_reset_draft_params.HubdbResetDraftParams
                ),
            ),
            cast_to=HubDBTableV3,
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
        Replaces the data in the draft version of the table with values from the
        published version. Any unpublished changes in the draft will be lost after this
        call is made.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

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

    async def unpublish(
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
        Unpublishes the table, meaning any website pages using data from the table will
        not render any data.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

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
                    {"include_foreign_ids": include_foreign_ids}, hubdb_unpublish_params.HubdbUnpublishParams
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
        Unpublishes the table, meaning any website pages using data from the table will
        not render any data.

        Args:
          include_foreign_ids: Set this to `true` to populate foreign ID values in the response.

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

    async def update_batch(
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
        Updates multiple rows as a batch in the draft version of the table, with a
        maximum of 100 rows per call. See the endpoint
        `PATCH /tables/{tableIdOrName}/rows/{rowId}/draft` for details on updating a
        single row.

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
            body=await async_maybe_transform({"inputs": inputs}, hubdb_update_batch_params.HubdbUpdateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseHubDBTableRowV3,
        )

    async def update_draft(
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
        """Update an existing HubDB table.

        You can use this endpoint to add or remove
        columns to the table as well as restore an archived table. Tables updated using
        the endpoint will only modify the draft verion of the table. Use the `/publish`
        endpoint to push all the changes to the published version. To restore a table,
        include the query parameter `archived=true` and `"archived": false` in the json
        body. **Note:** You need to include all the columns in the input when you are
        adding/removing/updating a column. If you do not include an already existing
        column in the request, it will be deleted.

        Args:
          label: Label of the table

          name: Name of the table

          archived: Specifies whether to return archived tables. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

          allow_child_tables: Specifies whether child tables can be created

          allow_public_api_access: Specifies whether the table can be read by public without authorization

          columns: List of columns in the table

          dynamic_meta_tags: Specifies the key value pairs of the
              [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
              with the associated column IDs.

          enable_child_table_pages: Specifies creation of multi-level dynamic pages using child tables

          use_for_pages: Specifies whether the table can be used for creation of dynamic pages

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
                hubdb_update_draft_params.HubdbUpdateDraftParams,
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
                    hubdb_update_draft_params.HubdbUpdateDraftParams,
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
        """Update an existing HubDB table.

        You can use this endpoint to add or remove
        columns to the table as well as restore an archived table. Tables updated using
        the endpoint will only modify the draft verion of the table. Use the `/publish`
        endpoint to push all the changes to the published version. To restore a table,
        include the query parameter `archived=true` and `"archived": false` in the json
        body. **Note:** You need to include all the columns in the input when you are
        adding/removing/updating a column. If you do not include an already existing
        column in the request, it will be deleted.

        Args:
          label: Label of the table

          name: Name of the table

          archived: Specifies whether to return archived tables. Defaults to `false`.

          include_foreign_ids: Set this to `true` to populate foreign ID values in the result.

          allow_child_tables: Specifies whether child tables can be created

          allow_public_api_access: Specifies whether the table can be read by public without authorization

          columns: List of columns in the table

          dynamic_meta_tags: Specifies the key value pairs of the
              [metadata fields](https://developers.hubspot.com/docs/cms/guides/dynamic-pages/hubdb#dynamic-pages)
              with the associated column IDs.

          enable_child_table_pages: Specifies creation of multi-level dynamic pages using child tables

          use_for_pages: Specifies whether the table can be used for creation of dynamic pages

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
        """Sparse updates a single row in the table's draft version.

        All the column values
        need not be specified. Only the columns or fields that needs to be modified can
        be specified. See the "Create a row" endpoint for instructions on how to format
        the JSON row definitions.

        Args:
          values: List of key value pairs with the column name and column value

          child_table_id: Specifies the value for the column child table id

          name: Specifies the value for `hs_name` column, which will be used as title in the
              dynamic pages

          path: Specifies the value for `hs_path` column, which will be used as slug in the
              dynamic pages

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
        Updates multiple rows as a batch in the draft version of the table, with a
        maximum of 100 rows per call. See the endpoint
        `PATCH /tables/{tableIdOrName}/rows/{rowId}/draft` for details on updating a
        single row.

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

        self.create = to_raw_response_wrapper(
            hubdb.create,
        )
        self.list = to_raw_response_wrapper(
            hubdb.list,
        )
        self.archive = to_raw_response_wrapper(
            hubdb.archive,
        )
        self.archive_table = to_raw_response_wrapper(
            hubdb.archive_table,
        )
        self.clone_batch = to_raw_response_wrapper(
            hubdb.clone_batch,
        )
        self.clone_draft = to_raw_response_wrapper(
            hubdb.clone_draft,
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
        self.create_batch = to_raw_response_wrapper(
            hubdb.create_batch,
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
        self.delete_draft = to_raw_response_wrapper(
            hubdb.delete_draft,
        )
        self.delete_version = to_raw_response_wrapper(
            hubdb.delete_version,
        )
        self.export = to_custom_raw_response_wrapper(
            hubdb.export,
            BinaryAPIResponse,
        )
        self.export_draft = to_custom_raw_response_wrapper(
            hubdb.export_draft,
            BinaryAPIResponse,
        )
        self.export_draft_table = to_custom_raw_response_wrapper(
            hubdb.export_draft_table,
            BinaryAPIResponse,
        )
        self.export_table = to_custom_raw_response_wrapper(
            hubdb.export_table,
            BinaryAPIResponse,
        )
        self.get = to_raw_response_wrapper(
            hubdb.get,
        )
        self.get_all_draft_tables = to_raw_response_wrapper(
            hubdb.get_all_draft_tables,
        )
        self.get_all_tables = to_raw_response_wrapper(
            hubdb.get_all_tables,
        )
        self.get_draft = to_raw_response_wrapper(
            hubdb.get_draft,
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
        self.import_draft = to_raw_response_wrapper(
            hubdb.import_draft,
        )
        self.import_draft_table = to_raw_response_wrapper(
            hubdb.import_draft_table,
        )
        self.list_draft = to_raw_response_wrapper(
            hubdb.list_draft,
        )
        self.list_drafts = to_raw_response_wrapper(
            hubdb.list_drafts,
        )
        self.publish_draft = to_raw_response_wrapper(
            hubdb.publish_draft,
        )
        self.publish_draft_table = to_raw_response_wrapper(
            hubdb.publish_draft_table,
        )
        self.purge_batch = to_raw_response_wrapper(
            hubdb.purge_batch,
        )
        self.purge_draft_table_row = to_raw_response_wrapper(
            hubdb.purge_draft_table_row,
        )
        self.purge_draft_table_rows = to_raw_response_wrapper(
            hubdb.purge_draft_table_rows,
        )
        self.read_batch = to_raw_response_wrapper(
            hubdb.read_batch,
        )
        self.read_draft_batch = to_raw_response_wrapper(
            hubdb.read_draft_batch,
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
        self.replace_batch = to_raw_response_wrapper(
            hubdb.replace_batch,
        )
        self.replace_draft = to_raw_response_wrapper(
            hubdb.replace_draft,
        )
        self.replace_draft_table_row = to_raw_response_wrapper(
            hubdb.replace_draft_table_row,
        )
        self.replace_draft_table_rows = to_raw_response_wrapper(
            hubdb.replace_draft_table_rows,
        )
        self.reset_draft = to_raw_response_wrapper(
            hubdb.reset_draft,
        )
        self.reset_draft_table = to_raw_response_wrapper(
            hubdb.reset_draft_table,
        )
        self.unpublish = to_raw_response_wrapper(
            hubdb.unpublish,
        )
        self.unpublish_table = to_raw_response_wrapper(
            hubdb.unpublish_table,
        )
        self.update_batch = to_raw_response_wrapper(
            hubdb.update_batch,
        )
        self.update_draft = to_raw_response_wrapper(
            hubdb.update_draft,
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


class AsyncHubdbResourceWithRawResponse:
    def __init__(self, hubdb: AsyncHubdbResource) -> None:
        self._hubdb = hubdb

        self.create = async_to_raw_response_wrapper(
            hubdb.create,
        )
        self.list = async_to_raw_response_wrapper(
            hubdb.list,
        )
        self.archive = async_to_raw_response_wrapper(
            hubdb.archive,
        )
        self.archive_table = async_to_raw_response_wrapper(
            hubdb.archive_table,
        )
        self.clone_batch = async_to_raw_response_wrapper(
            hubdb.clone_batch,
        )
        self.clone_draft = async_to_raw_response_wrapper(
            hubdb.clone_draft,
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
        self.create_batch = async_to_raw_response_wrapper(
            hubdb.create_batch,
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
        self.delete_draft = async_to_raw_response_wrapper(
            hubdb.delete_draft,
        )
        self.delete_version = async_to_raw_response_wrapper(
            hubdb.delete_version,
        )
        self.export = async_to_custom_raw_response_wrapper(
            hubdb.export,
            AsyncBinaryAPIResponse,
        )
        self.export_draft = async_to_custom_raw_response_wrapper(
            hubdb.export_draft,
            AsyncBinaryAPIResponse,
        )
        self.export_draft_table = async_to_custom_raw_response_wrapper(
            hubdb.export_draft_table,
            AsyncBinaryAPIResponse,
        )
        self.export_table = async_to_custom_raw_response_wrapper(
            hubdb.export_table,
            AsyncBinaryAPIResponse,
        )
        self.get = async_to_raw_response_wrapper(
            hubdb.get,
        )
        self.get_all_draft_tables = async_to_raw_response_wrapper(
            hubdb.get_all_draft_tables,
        )
        self.get_all_tables = async_to_raw_response_wrapper(
            hubdb.get_all_tables,
        )
        self.get_draft = async_to_raw_response_wrapper(
            hubdb.get_draft,
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
        self.import_draft = async_to_raw_response_wrapper(
            hubdb.import_draft,
        )
        self.import_draft_table = async_to_raw_response_wrapper(
            hubdb.import_draft_table,
        )
        self.list_draft = async_to_raw_response_wrapper(
            hubdb.list_draft,
        )
        self.list_drafts = async_to_raw_response_wrapper(
            hubdb.list_drafts,
        )
        self.publish_draft = async_to_raw_response_wrapper(
            hubdb.publish_draft,
        )
        self.publish_draft_table = async_to_raw_response_wrapper(
            hubdb.publish_draft_table,
        )
        self.purge_batch = async_to_raw_response_wrapper(
            hubdb.purge_batch,
        )
        self.purge_draft_table_row = async_to_raw_response_wrapper(
            hubdb.purge_draft_table_row,
        )
        self.purge_draft_table_rows = async_to_raw_response_wrapper(
            hubdb.purge_draft_table_rows,
        )
        self.read_batch = async_to_raw_response_wrapper(
            hubdb.read_batch,
        )
        self.read_draft_batch = async_to_raw_response_wrapper(
            hubdb.read_draft_batch,
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
        self.replace_batch = async_to_raw_response_wrapper(
            hubdb.replace_batch,
        )
        self.replace_draft = async_to_raw_response_wrapper(
            hubdb.replace_draft,
        )
        self.replace_draft_table_row = async_to_raw_response_wrapper(
            hubdb.replace_draft_table_row,
        )
        self.replace_draft_table_rows = async_to_raw_response_wrapper(
            hubdb.replace_draft_table_rows,
        )
        self.reset_draft = async_to_raw_response_wrapper(
            hubdb.reset_draft,
        )
        self.reset_draft_table = async_to_raw_response_wrapper(
            hubdb.reset_draft_table,
        )
        self.unpublish = async_to_raw_response_wrapper(
            hubdb.unpublish,
        )
        self.unpublish_table = async_to_raw_response_wrapper(
            hubdb.unpublish_table,
        )
        self.update_batch = async_to_raw_response_wrapper(
            hubdb.update_batch,
        )
        self.update_draft = async_to_raw_response_wrapper(
            hubdb.update_draft,
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


class HubdbResourceWithStreamingResponse:
    def __init__(self, hubdb: HubdbResource) -> None:
        self._hubdb = hubdb

        self.create = to_streamed_response_wrapper(
            hubdb.create,
        )
        self.list = to_streamed_response_wrapper(
            hubdb.list,
        )
        self.archive = to_streamed_response_wrapper(
            hubdb.archive,
        )
        self.archive_table = to_streamed_response_wrapper(
            hubdb.archive_table,
        )
        self.clone_batch = to_streamed_response_wrapper(
            hubdb.clone_batch,
        )
        self.clone_draft = to_streamed_response_wrapper(
            hubdb.clone_draft,
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
        self.create_batch = to_streamed_response_wrapper(
            hubdb.create_batch,
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
        self.delete_draft = to_streamed_response_wrapper(
            hubdb.delete_draft,
        )
        self.delete_version = to_streamed_response_wrapper(
            hubdb.delete_version,
        )
        self.export = to_custom_streamed_response_wrapper(
            hubdb.export,
            StreamedBinaryAPIResponse,
        )
        self.export_draft = to_custom_streamed_response_wrapper(
            hubdb.export_draft,
            StreamedBinaryAPIResponse,
        )
        self.export_draft_table = to_custom_streamed_response_wrapper(
            hubdb.export_draft_table,
            StreamedBinaryAPIResponse,
        )
        self.export_table = to_custom_streamed_response_wrapper(
            hubdb.export_table,
            StreamedBinaryAPIResponse,
        )
        self.get = to_streamed_response_wrapper(
            hubdb.get,
        )
        self.get_all_draft_tables = to_streamed_response_wrapper(
            hubdb.get_all_draft_tables,
        )
        self.get_all_tables = to_streamed_response_wrapper(
            hubdb.get_all_tables,
        )
        self.get_draft = to_streamed_response_wrapper(
            hubdb.get_draft,
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
        self.import_draft = to_streamed_response_wrapper(
            hubdb.import_draft,
        )
        self.import_draft_table = to_streamed_response_wrapper(
            hubdb.import_draft_table,
        )
        self.list_draft = to_streamed_response_wrapper(
            hubdb.list_draft,
        )
        self.list_drafts = to_streamed_response_wrapper(
            hubdb.list_drafts,
        )
        self.publish_draft = to_streamed_response_wrapper(
            hubdb.publish_draft,
        )
        self.publish_draft_table = to_streamed_response_wrapper(
            hubdb.publish_draft_table,
        )
        self.purge_batch = to_streamed_response_wrapper(
            hubdb.purge_batch,
        )
        self.purge_draft_table_row = to_streamed_response_wrapper(
            hubdb.purge_draft_table_row,
        )
        self.purge_draft_table_rows = to_streamed_response_wrapper(
            hubdb.purge_draft_table_rows,
        )
        self.read_batch = to_streamed_response_wrapper(
            hubdb.read_batch,
        )
        self.read_draft_batch = to_streamed_response_wrapper(
            hubdb.read_draft_batch,
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
        self.replace_batch = to_streamed_response_wrapper(
            hubdb.replace_batch,
        )
        self.replace_draft = to_streamed_response_wrapper(
            hubdb.replace_draft,
        )
        self.replace_draft_table_row = to_streamed_response_wrapper(
            hubdb.replace_draft_table_row,
        )
        self.replace_draft_table_rows = to_streamed_response_wrapper(
            hubdb.replace_draft_table_rows,
        )
        self.reset_draft = to_streamed_response_wrapper(
            hubdb.reset_draft,
        )
        self.reset_draft_table = to_streamed_response_wrapper(
            hubdb.reset_draft_table,
        )
        self.unpublish = to_streamed_response_wrapper(
            hubdb.unpublish,
        )
        self.unpublish_table = to_streamed_response_wrapper(
            hubdb.unpublish_table,
        )
        self.update_batch = to_streamed_response_wrapper(
            hubdb.update_batch,
        )
        self.update_draft = to_streamed_response_wrapper(
            hubdb.update_draft,
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


class AsyncHubdbResourceWithStreamingResponse:
    def __init__(self, hubdb: AsyncHubdbResource) -> None:
        self._hubdb = hubdb

        self.create = async_to_streamed_response_wrapper(
            hubdb.create,
        )
        self.list = async_to_streamed_response_wrapper(
            hubdb.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            hubdb.archive,
        )
        self.archive_table = async_to_streamed_response_wrapper(
            hubdb.archive_table,
        )
        self.clone_batch = async_to_streamed_response_wrapper(
            hubdb.clone_batch,
        )
        self.clone_draft = async_to_streamed_response_wrapper(
            hubdb.clone_draft,
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
        self.create_batch = async_to_streamed_response_wrapper(
            hubdb.create_batch,
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
        self.delete_draft = async_to_streamed_response_wrapper(
            hubdb.delete_draft,
        )
        self.delete_version = async_to_streamed_response_wrapper(
            hubdb.delete_version,
        )
        self.export = async_to_custom_streamed_response_wrapper(
            hubdb.export,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_draft = async_to_custom_streamed_response_wrapper(
            hubdb.export_draft,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_draft_table = async_to_custom_streamed_response_wrapper(
            hubdb.export_draft_table,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_table = async_to_custom_streamed_response_wrapper(
            hubdb.export_table,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get = async_to_streamed_response_wrapper(
            hubdb.get,
        )
        self.get_all_draft_tables = async_to_streamed_response_wrapper(
            hubdb.get_all_draft_tables,
        )
        self.get_all_tables = async_to_streamed_response_wrapper(
            hubdb.get_all_tables,
        )
        self.get_draft = async_to_streamed_response_wrapper(
            hubdb.get_draft,
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
        self.import_draft = async_to_streamed_response_wrapper(
            hubdb.import_draft,
        )
        self.import_draft_table = async_to_streamed_response_wrapper(
            hubdb.import_draft_table,
        )
        self.list_draft = async_to_streamed_response_wrapper(
            hubdb.list_draft,
        )
        self.list_drafts = async_to_streamed_response_wrapper(
            hubdb.list_drafts,
        )
        self.publish_draft = async_to_streamed_response_wrapper(
            hubdb.publish_draft,
        )
        self.publish_draft_table = async_to_streamed_response_wrapper(
            hubdb.publish_draft_table,
        )
        self.purge_batch = async_to_streamed_response_wrapper(
            hubdb.purge_batch,
        )
        self.purge_draft_table_row = async_to_streamed_response_wrapper(
            hubdb.purge_draft_table_row,
        )
        self.purge_draft_table_rows = async_to_streamed_response_wrapper(
            hubdb.purge_draft_table_rows,
        )
        self.read_batch = async_to_streamed_response_wrapper(
            hubdb.read_batch,
        )
        self.read_draft_batch = async_to_streamed_response_wrapper(
            hubdb.read_draft_batch,
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
        self.replace_batch = async_to_streamed_response_wrapper(
            hubdb.replace_batch,
        )
        self.replace_draft = async_to_streamed_response_wrapper(
            hubdb.replace_draft,
        )
        self.replace_draft_table_row = async_to_streamed_response_wrapper(
            hubdb.replace_draft_table_row,
        )
        self.replace_draft_table_rows = async_to_streamed_response_wrapper(
            hubdb.replace_draft_table_rows,
        )
        self.reset_draft = async_to_streamed_response_wrapper(
            hubdb.reset_draft,
        )
        self.reset_draft_table = async_to_streamed_response_wrapper(
            hubdb.reset_draft_table,
        )
        self.unpublish = async_to_streamed_response_wrapper(
            hubdb.unpublish,
        )
        self.unpublish_table = async_to_streamed_response_wrapper(
            hubdb.unpublish_table,
        )
        self.update_batch = async_to_streamed_response_wrapper(
            hubdb.update_batch,
        )
        self.update_draft = async_to_streamed_response_wrapper(
            hubdb.update_draft,
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
