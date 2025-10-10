# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Mapping, Iterable, cast
from datetime import datetime

import httpx

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
from ....pagination import SyncPage, AsyncPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.cms.hubdb import (
    table_get_params,
    table_list_params,
    table_create_params,
    table_export_params,
    table_get_draft_params,
    table_unpublish_params,
    table_clone_draft_params,
    table_list_drafts_params,
    table_reset_draft_params,
    table_export_draft_params,
    table_import_draft_params,
    table_update_draft_params,
    table_publish_draft_params,
)
from ....types.cms.import_result import ImportResult
from ....types.cms.hub_db_table_v3 import HubDBTableV3
from ....types.cms.column_request_param import ColumnRequestParam
from ....types.cms.collection_response_with_total_hub_db_table_v3_forward_paging import (
    CollectionResponseWithTotalHubDBTableV3ForwardPaging,
)

__all__ = ["TablesResource", "AsyncTablesResource"]


class TablesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return TablesResourceWithStreamingResponse(self)

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
                table_create_params.TableCreateParams,
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
    ) -> SyncPage[HubDBTableV3]:
        """
        Get all published tables

        Args:
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
                    table_list_params.TableListParams,
                ),
            ),
            model=HubDBTableV3,
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
                table_clone_draft_params.TableCloneDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
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
                query=maybe_transform({"format": format}, table_export_params.TableExportParams),
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
                query=maybe_transform({"format": format}, table_export_draft_params.TableExportDraftParams),
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
                    table_get_params.TableGetParams,
                ),
            ),
            cast_to=HubDBTableV3,
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
                    table_get_draft_params.TableGetDraftParams,
                ),
            ),
            cast_to=HubDBTableV3,
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
            body=maybe_transform(body, table_import_draft_params.TableImportDraftParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportResult,
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
                    table_list_drafts_params.TableListDraftsParams,
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
                    {"include_foreign_ids": include_foreign_ids}, table_publish_draft_params.TablePublishDraftParams
                ),
            ),
            cast_to=HubDBTableV3,
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
                    {"include_foreign_ids": include_foreign_ids}, table_reset_draft_params.TableResetDraftParams
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
                    {"include_foreign_ids": include_foreign_ids}, table_unpublish_params.TableUnpublishParams
                ),
            ),
            cast_to=HubDBTableV3,
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
                table_update_draft_params.TableUpdateDraftParams,
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
                    table_update_draft_params.TableUpdateDraftParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )


class AsyncTablesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncTablesResourceWithStreamingResponse(self)

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
                table_create_params.TableCreateParams,
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
    ) -> AsyncPaginator[HubDBTableV3, AsyncPage[HubDBTableV3]]:
        """
        Get all published tables

        Args:
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
                    table_list_params.TableListParams,
                ),
            ),
            model=HubDBTableV3,
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
                table_clone_draft_params.TableCloneDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableV3,
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
                query=await async_maybe_transform({"format": format}, table_export_params.TableExportParams),
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
                query=await async_maybe_transform({"format": format}, table_export_draft_params.TableExportDraftParams),
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
                    table_get_params.TableGetParams,
                ),
            ),
            cast_to=HubDBTableV3,
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
                    table_get_draft_params.TableGetDraftParams,
                ),
            ),
            cast_to=HubDBTableV3,
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
            body=await async_maybe_transform(body, table_import_draft_params.TableImportDraftParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportResult,
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
                    table_list_drafts_params.TableListDraftsParams,
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
                    {"include_foreign_ids": include_foreign_ids}, table_publish_draft_params.TablePublishDraftParams
                ),
            ),
            cast_to=HubDBTableV3,
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
                    {"include_foreign_ids": include_foreign_ids}, table_reset_draft_params.TableResetDraftParams
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
                    {"include_foreign_ids": include_foreign_ids}, table_unpublish_params.TableUnpublishParams
                ),
            ),
            cast_to=HubDBTableV3,
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
                table_update_draft_params.TableUpdateDraftParams,
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
                    table_update_draft_params.TableUpdateDraftParams,
                ),
            ),
            cast_to=HubDBTableV3,
        )


class TablesResourceWithRawResponse:
    def __init__(self, tables: TablesResource) -> None:
        self._tables = tables

        self.create = to_raw_response_wrapper(
            tables.create,
        )
        self.list = to_raw_response_wrapper(
            tables.list,
        )
        self.archive = to_raw_response_wrapper(
            tables.archive,
        )
        self.clone_draft = to_raw_response_wrapper(
            tables.clone_draft,
        )
        self.delete_version = to_raw_response_wrapper(
            tables.delete_version,
        )
        self.export = to_custom_raw_response_wrapper(
            tables.export,
            BinaryAPIResponse,
        )
        self.export_draft = to_custom_raw_response_wrapper(
            tables.export_draft,
            BinaryAPIResponse,
        )
        self.get = to_raw_response_wrapper(
            tables.get,
        )
        self.get_draft = to_raw_response_wrapper(
            tables.get_draft,
        )
        self.import_draft = to_raw_response_wrapper(
            tables.import_draft,
        )
        self.list_drafts = to_raw_response_wrapper(
            tables.list_drafts,
        )
        self.publish_draft = to_raw_response_wrapper(
            tables.publish_draft,
        )
        self.reset_draft = to_raw_response_wrapper(
            tables.reset_draft,
        )
        self.unpublish = to_raw_response_wrapper(
            tables.unpublish,
        )
        self.update_draft = to_raw_response_wrapper(
            tables.update_draft,
        )


class AsyncTablesResourceWithRawResponse:
    def __init__(self, tables: AsyncTablesResource) -> None:
        self._tables = tables

        self.create = async_to_raw_response_wrapper(
            tables.create,
        )
        self.list = async_to_raw_response_wrapper(
            tables.list,
        )
        self.archive = async_to_raw_response_wrapper(
            tables.archive,
        )
        self.clone_draft = async_to_raw_response_wrapper(
            tables.clone_draft,
        )
        self.delete_version = async_to_raw_response_wrapper(
            tables.delete_version,
        )
        self.export = async_to_custom_raw_response_wrapper(
            tables.export,
            AsyncBinaryAPIResponse,
        )
        self.export_draft = async_to_custom_raw_response_wrapper(
            tables.export_draft,
            AsyncBinaryAPIResponse,
        )
        self.get = async_to_raw_response_wrapper(
            tables.get,
        )
        self.get_draft = async_to_raw_response_wrapper(
            tables.get_draft,
        )
        self.import_draft = async_to_raw_response_wrapper(
            tables.import_draft,
        )
        self.list_drafts = async_to_raw_response_wrapper(
            tables.list_drafts,
        )
        self.publish_draft = async_to_raw_response_wrapper(
            tables.publish_draft,
        )
        self.reset_draft = async_to_raw_response_wrapper(
            tables.reset_draft,
        )
        self.unpublish = async_to_raw_response_wrapper(
            tables.unpublish,
        )
        self.update_draft = async_to_raw_response_wrapper(
            tables.update_draft,
        )


class TablesResourceWithStreamingResponse:
    def __init__(self, tables: TablesResource) -> None:
        self._tables = tables

        self.create = to_streamed_response_wrapper(
            tables.create,
        )
        self.list = to_streamed_response_wrapper(
            tables.list,
        )
        self.archive = to_streamed_response_wrapper(
            tables.archive,
        )
        self.clone_draft = to_streamed_response_wrapper(
            tables.clone_draft,
        )
        self.delete_version = to_streamed_response_wrapper(
            tables.delete_version,
        )
        self.export = to_custom_streamed_response_wrapper(
            tables.export,
            StreamedBinaryAPIResponse,
        )
        self.export_draft = to_custom_streamed_response_wrapper(
            tables.export_draft,
            StreamedBinaryAPIResponse,
        )
        self.get = to_streamed_response_wrapper(
            tables.get,
        )
        self.get_draft = to_streamed_response_wrapper(
            tables.get_draft,
        )
        self.import_draft = to_streamed_response_wrapper(
            tables.import_draft,
        )
        self.list_drafts = to_streamed_response_wrapper(
            tables.list_drafts,
        )
        self.publish_draft = to_streamed_response_wrapper(
            tables.publish_draft,
        )
        self.reset_draft = to_streamed_response_wrapper(
            tables.reset_draft,
        )
        self.unpublish = to_streamed_response_wrapper(
            tables.unpublish,
        )
        self.update_draft = to_streamed_response_wrapper(
            tables.update_draft,
        )


class AsyncTablesResourceWithStreamingResponse:
    def __init__(self, tables: AsyncTablesResource) -> None:
        self._tables = tables

        self.create = async_to_streamed_response_wrapper(
            tables.create,
        )
        self.list = async_to_streamed_response_wrapper(
            tables.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            tables.archive,
        )
        self.clone_draft = async_to_streamed_response_wrapper(
            tables.clone_draft,
        )
        self.delete_version = async_to_streamed_response_wrapper(
            tables.delete_version,
        )
        self.export = async_to_custom_streamed_response_wrapper(
            tables.export,
            AsyncStreamedBinaryAPIResponse,
        )
        self.export_draft = async_to_custom_streamed_response_wrapper(
            tables.export_draft,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get = async_to_streamed_response_wrapper(
            tables.get,
        )
        self.get_draft = async_to_streamed_response_wrapper(
            tables.get_draft,
        )
        self.import_draft = async_to_streamed_response_wrapper(
            tables.import_draft,
        )
        self.list_drafts = async_to_streamed_response_wrapper(
            tables.list_drafts,
        )
        self.publish_draft = async_to_streamed_response_wrapper(
            tables.publish_draft,
        )
        self.reset_draft = async_to_streamed_response_wrapper(
            tables.reset_draft,
        )
        self.unpublish = async_to_streamed_response_wrapper(
            tables.unpublish,
        )
        self.update_draft = async_to_streamed_response_wrapper(
            tables.update_draft,
        )
