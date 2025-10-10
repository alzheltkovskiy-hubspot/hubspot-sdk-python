# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from .draft.draft import (
    DraftResource,
    AsyncDraftResource,
    DraftResourceWithRawResponse,
    AsyncDraftResourceWithRawResponse,
    DraftResourceWithStreamingResponse,
    AsyncDraftResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncPage, AsyncPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.cms.hubdb import (
    row_get_params,
    row_list_params,
    row_create_params,
    row_get_draft_params,
    row_list_draft_params,
    row_clone_draft_params,
    row_update_draft_params,
    row_replace_draft_params,
)
from .....types.cms.variant_param import VariantParam
from .....types.cms.hub_db_table_row_v3 import HubDBTableRowV3
from .....types.cms.unified_collection_response_with_total_base_hub_db_table_row_v3 import (
    UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3,
)

__all__ = ["RowsResource", "AsyncRowsResource"]


class RowsResource(SyncAPIResource):
    @cached_property
    def draft(self) -> DraftResource:
        return DraftResource(self._client)

    @cached_property
    def with_raw_response(self) -> RowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return RowsResourceWithStreamingResponse(self)

    def create(
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
                row_create_params.RowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )

    def list(
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
                    row_list_params.RowListParams,
                ),
            ),
            model=object,
        )

    def clone_draft(
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
                query=maybe_transform({"name": name}, row_clone_draft_params.RowCloneDraftParams),
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

    def get(
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
                query=maybe_transform({"archived": archived}, row_get_params.RowGetParams),
            ),
            cast_to=HubDBTableRowV3,
        )

    def get_draft(
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
                query=maybe_transform({"archived": archived}, row_get_draft_params.RowGetDraftParams),
            ),
            cast_to=HubDBTableRowV3,
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
        """
        Get rows from draft table

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
                        row_list_draft_params.RowListDraftParams,
                    ),
                ),
                cast_to=cast(
                    Any, UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
                row_replace_draft_params.RowReplaceDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )

    def update_draft(
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
                row_update_draft_params.RowUpdateDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )


class AsyncRowsResource(AsyncAPIResource):
    @cached_property
    def draft(self) -> AsyncDraftResource:
        return AsyncDraftResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncRowsResourceWithStreamingResponse(self)

    async def create(
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
                row_create_params.RowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )

    def list(
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
                    row_list_params.RowListParams,
                ),
            ),
            model=object,
        )

    async def clone_draft(
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
                query=await async_maybe_transform({"name": name}, row_clone_draft_params.RowCloneDraftParams),
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

    async def get(
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
                query=await async_maybe_transform({"archived": archived}, row_get_params.RowGetParams),
            ),
            cast_to=HubDBTableRowV3,
        )

    async def get_draft(
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
                query=await async_maybe_transform({"archived": archived}, row_get_draft_params.RowGetDraftParams),
            ),
            cast_to=HubDBTableRowV3,
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
        """
        Get rows from draft table

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
                        row_list_draft_params.RowListDraftParams,
                    ),
                ),
                cast_to=cast(
                    Any, UnifiedCollectionResponseWithTotalBaseHubDBTableRowV3
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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
                row_replace_draft_params.RowReplaceDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )

    async def update_draft(
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
                row_update_draft_params.RowUpdateDraftParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HubDBTableRowV3,
        )


class RowsResourceWithRawResponse:
    def __init__(self, rows: RowsResource) -> None:
        self._rows = rows

        self.create = to_raw_response_wrapper(
            rows.create,
        )
        self.list = to_raw_response_wrapper(
            rows.list,
        )
        self.clone_draft = to_raw_response_wrapper(
            rows.clone_draft,
        )
        self.delete_draft = to_raw_response_wrapper(
            rows.delete_draft,
        )
        self.get = to_raw_response_wrapper(
            rows.get,
        )
        self.get_draft = to_raw_response_wrapper(
            rows.get_draft,
        )
        self.list_draft = to_raw_response_wrapper(
            rows.list_draft,
        )
        self.replace_draft = to_raw_response_wrapper(
            rows.replace_draft,
        )
        self.update_draft = to_raw_response_wrapper(
            rows.update_draft,
        )

    @cached_property
    def draft(self) -> DraftResourceWithRawResponse:
        return DraftResourceWithRawResponse(self._rows.draft)


class AsyncRowsResourceWithRawResponse:
    def __init__(self, rows: AsyncRowsResource) -> None:
        self._rows = rows

        self.create = async_to_raw_response_wrapper(
            rows.create,
        )
        self.list = async_to_raw_response_wrapper(
            rows.list,
        )
        self.clone_draft = async_to_raw_response_wrapper(
            rows.clone_draft,
        )
        self.delete_draft = async_to_raw_response_wrapper(
            rows.delete_draft,
        )
        self.get = async_to_raw_response_wrapper(
            rows.get,
        )
        self.get_draft = async_to_raw_response_wrapper(
            rows.get_draft,
        )
        self.list_draft = async_to_raw_response_wrapper(
            rows.list_draft,
        )
        self.replace_draft = async_to_raw_response_wrapper(
            rows.replace_draft,
        )
        self.update_draft = async_to_raw_response_wrapper(
            rows.update_draft,
        )

    @cached_property
    def draft(self) -> AsyncDraftResourceWithRawResponse:
        return AsyncDraftResourceWithRawResponse(self._rows.draft)


class RowsResourceWithStreamingResponse:
    def __init__(self, rows: RowsResource) -> None:
        self._rows = rows

        self.create = to_streamed_response_wrapper(
            rows.create,
        )
        self.list = to_streamed_response_wrapper(
            rows.list,
        )
        self.clone_draft = to_streamed_response_wrapper(
            rows.clone_draft,
        )
        self.delete_draft = to_streamed_response_wrapper(
            rows.delete_draft,
        )
        self.get = to_streamed_response_wrapper(
            rows.get,
        )
        self.get_draft = to_streamed_response_wrapper(
            rows.get_draft,
        )
        self.list_draft = to_streamed_response_wrapper(
            rows.list_draft,
        )
        self.replace_draft = to_streamed_response_wrapper(
            rows.replace_draft,
        )
        self.update_draft = to_streamed_response_wrapper(
            rows.update_draft,
        )

    @cached_property
    def draft(self) -> DraftResourceWithStreamingResponse:
        return DraftResourceWithStreamingResponse(self._rows.draft)


class AsyncRowsResourceWithStreamingResponse:
    def __init__(self, rows: AsyncRowsResource) -> None:
        self._rows = rows

        self.create = async_to_streamed_response_wrapper(
            rows.create,
        )
        self.list = async_to_streamed_response_wrapper(
            rows.list,
        )
        self.clone_draft = async_to_streamed_response_wrapper(
            rows.clone_draft,
        )
        self.delete_draft = async_to_streamed_response_wrapper(
            rows.delete_draft,
        )
        self.get = async_to_streamed_response_wrapper(
            rows.get,
        )
        self.get_draft = async_to_streamed_response_wrapper(
            rows.get_draft,
        )
        self.list_draft = async_to_streamed_response_wrapper(
            rows.list_draft,
        )
        self.replace_draft = async_to_streamed_response_wrapper(
            rows.replace_draft,
        )
        self.update_draft = async_to_streamed_response_wrapper(
            rows.update_draft,
        )

    @cached_property
    def draft(self) -> AsyncDraftResourceWithStreamingResponse:
        return AsyncDraftResourceWithStreamingResponse(self._rows.draft)
