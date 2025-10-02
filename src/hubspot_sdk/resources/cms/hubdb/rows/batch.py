# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.cms.hubdb.rows import batch_replace_params
from .....types.cms.cms_hubdb_batch_response_hub_db_table_row_v3 import CmsHubdbBatchResponseHubDBTableRowV3
from .....types.cms.cms_hubdb_hub_db_table_row_v3_batch_update_request_param import (
    CmsHubdbHubDBTableRowV3BatchUpdateRequestParam,
)

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def replace(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[CmsHubdbHubDBTableRowV3BatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CmsHubdbBatchResponseHubDBTableRowV3:
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
            body=maybe_transform({"inputs": inputs}, batch_replace_params.BatchReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CmsHubdbBatchResponseHubDBTableRowV3,
        )


class AsyncBatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def replace(
        self,
        table_id_or_name: str,
        *,
        inputs: Iterable[CmsHubdbHubDBTableRowV3BatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CmsHubdbBatchResponseHubDBTableRowV3:
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
            body=await async_maybe_transform({"inputs": inputs}, batch_replace_params.BatchReplaceParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CmsHubdbBatchResponseHubDBTableRowV3,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.replace = to_raw_response_wrapper(
            batch.replace,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.replace = async_to_raw_response_wrapper(
            batch.replace,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.replace = to_streamed_response_wrapper(
            batch.replace,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.replace = async_to_streamed_response_wrapper(
            batch.replace,
        )
