# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from .....types.crm.objects import (
    deal_get_by_object_type_id_params,
    deal_list_by_object_type_id_params,
    deal_merge_by_object_type_id_params,
    deal_create_by_object_type_id_params,
    deal_search_by_object_type_id_params,
    deal_update_by_object_type_id_params,
)
from .....types.crm.filter_group_param import FilterGroupParam
from .....types.crm.simple_public_object import SimplePublicObject
from .....types.crm.public_associations_for_object_param import PublicAssociationsForObjectParam
from .....types.crm.created_response_simple_public_object import CreatedResponseSimplePublicObject
from .....types.crm.simple_public_object_with_associations import SimplePublicObjectWithAssociations
from .....types.crm.collection_response_with_total_simple_public_object import (
    CollectionResponseWithTotalSimplePublicObject,
)
from .....types.crm.collection_response_simple_public_object_with_associations import (
    CollectionResponseSimplePublicObjectWithAssociations,
)

__all__ = ["DealsResource", "AsyncDealsResource"]


class DealsResource(SyncAPIResource):
    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> DealsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DealsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DealsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return DealsResourceWithStreamingResponse(self)

    def create_by_object_type_id(
        self,
        *,
        properties: Dict[str, str],
        associations: Iterable[PublicAssociationsForObjectParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedResponseSimplePublicObject:
        """
        Create

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/objects/0-3",
            body=maybe_transform(
                {
                    "properties": properties,
                    "associations": associations,
                },
                deal_create_by_object_type_id_params.DealCreateByObjectTypeIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedResponseSimplePublicObject,
        )

    def delete_by_object_type_id(
        self,
        deal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/crm/v3/objects/0-3/{deal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_by_object_type_id(
        self,
        deal_id: str,
        *,
        archived: bool | Omit = omit,
        associations: SequenceNotStr[str] | Omit = omit,
        id_property: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        properties_with_history: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObjectWithAssociations:
        """
        Read

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return self._get(
            f"/crm/v3/objects/0-3/{deal_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "associations": associations,
                        "id_property": id_property,
                        "properties": properties,
                        "properties_with_history": properties_with_history,
                    },
                    deal_get_by_object_type_id_params.DealGetByObjectTypeIDParams,
                ),
            ),
            cast_to=SimplePublicObjectWithAssociations,
        )

    def list_by_object_type_id(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        associations: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        properties_with_history: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseSimplePublicObjectWithAssociations:
        """
        List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/crm/v3/objects/0-3",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "associations": associations,
                        "limit": limit,
                        "properties": properties,
                        "properties_with_history": properties_with_history,
                    },
                    deal_list_by_object_type_id_params.DealListByObjectTypeIDParams,
                ),
            ),
            cast_to=CollectionResponseSimplePublicObjectWithAssociations,
        )

    def merge_by_object_type_id(
        self,
        *,
        object_id_to_merge: str,
        primary_object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObject:
        """
        Merge two deals with same type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/objects/0-3/merge",
            body=maybe_transform(
                {
                    "object_id_to_merge": object_id_to_merge,
                    "primary_object_id": primary_object_id,
                },
                deal_merge_by_object_type_id_params.DealMergeByObjectTypeIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimplePublicObject,
        )

    def search_by_object_type_id(
        self,
        *,
        after: str | Omit = omit,
        filter_groups: Iterable[FilterGroupParam] | Omit = omit,
        limit: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        query: str | Omit = omit,
        sorts: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalSimplePublicObject:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/objects/0-3/search",
            body=maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "query": query,
                    "sorts": sorts,
                },
                deal_search_by_object_type_id_params.DealSearchByObjectTypeIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalSimplePublicObject,
        )

    def update_by_object_type_id(
        self,
        deal_id: str,
        *,
        properties: Dict[str, str],
        id_property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObject:
        """
        Update

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return self._patch(
            f"/crm/v3/objects/0-3/{deal_id}",
            body=maybe_transform(
                {"properties": properties}, deal_update_by_object_type_id_params.DealUpdateByObjectTypeIDParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"id_property": id_property}, deal_update_by_object_type_id_params.DealUpdateByObjectTypeIDParams
                ),
            ),
            cast_to=SimplePublicObject,
        )


class AsyncDealsResource(AsyncAPIResource):
    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDealsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDealsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDealsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncDealsResourceWithStreamingResponse(self)

    async def create_by_object_type_id(
        self,
        *,
        properties: Dict[str, str],
        associations: Iterable[PublicAssociationsForObjectParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedResponseSimplePublicObject:
        """
        Create

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/objects/0-3",
            body=await async_maybe_transform(
                {
                    "properties": properties,
                    "associations": associations,
                },
                deal_create_by_object_type_id_params.DealCreateByObjectTypeIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedResponseSimplePublicObject,
        )

    async def delete_by_object_type_id(
        self,
        deal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/crm/v3/objects/0-3/{deal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_by_object_type_id(
        self,
        deal_id: str,
        *,
        archived: bool | Omit = omit,
        associations: SequenceNotStr[str] | Omit = omit,
        id_property: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        properties_with_history: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObjectWithAssociations:
        """
        Read

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return await self._get(
            f"/crm/v3/objects/0-3/{deal_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "associations": associations,
                        "id_property": id_property,
                        "properties": properties,
                        "properties_with_history": properties_with_history,
                    },
                    deal_get_by_object_type_id_params.DealGetByObjectTypeIDParams,
                ),
            ),
            cast_to=SimplePublicObjectWithAssociations,
        )

    async def list_by_object_type_id(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        associations: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        properties_with_history: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseSimplePublicObjectWithAssociations:
        """
        List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/crm/v3/objects/0-3",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "associations": associations,
                        "limit": limit,
                        "properties": properties,
                        "properties_with_history": properties_with_history,
                    },
                    deal_list_by_object_type_id_params.DealListByObjectTypeIDParams,
                ),
            ),
            cast_to=CollectionResponseSimplePublicObjectWithAssociations,
        )

    async def merge_by_object_type_id(
        self,
        *,
        object_id_to_merge: str,
        primary_object_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObject:
        """
        Merge two deals with same type

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/objects/0-3/merge",
            body=await async_maybe_transform(
                {
                    "object_id_to_merge": object_id_to_merge,
                    "primary_object_id": primary_object_id,
                },
                deal_merge_by_object_type_id_params.DealMergeByObjectTypeIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimplePublicObject,
        )

    async def search_by_object_type_id(
        self,
        *,
        after: str | Omit = omit,
        filter_groups: Iterable[FilterGroupParam] | Omit = omit,
        limit: int | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        query: str | Omit = omit,
        sorts: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseWithTotalSimplePublicObject:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/objects/0-3/search",
            body=await async_maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "query": query,
                    "sorts": sorts,
                },
                deal_search_by_object_type_id_params.DealSearchByObjectTypeIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponseWithTotalSimplePublicObject,
        )

    async def update_by_object_type_id(
        self,
        deal_id: str,
        *,
        properties: Dict[str, str],
        id_property: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimplePublicObject:
        """
        Update

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not deal_id:
            raise ValueError(f"Expected a non-empty value for `deal_id` but received {deal_id!r}")
        return await self._patch(
            f"/crm/v3/objects/0-3/{deal_id}",
            body=await async_maybe_transform(
                {"properties": properties}, deal_update_by_object_type_id_params.DealUpdateByObjectTypeIDParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"id_property": id_property}, deal_update_by_object_type_id_params.DealUpdateByObjectTypeIDParams
                ),
            ),
            cast_to=SimplePublicObject,
        )


class DealsResourceWithRawResponse:
    def __init__(self, deals: DealsResource) -> None:
        self._deals = deals

        self.create_by_object_type_id = to_raw_response_wrapper(
            deals.create_by_object_type_id,
        )
        self.delete_by_object_type_id = to_raw_response_wrapper(
            deals.delete_by_object_type_id,
        )
        self.get_by_object_type_id = to_raw_response_wrapper(
            deals.get_by_object_type_id,
        )
        self.list_by_object_type_id = to_raw_response_wrapper(
            deals.list_by_object_type_id,
        )
        self.merge_by_object_type_id = to_raw_response_wrapper(
            deals.merge_by_object_type_id,
        )
        self.search_by_object_type_id = to_raw_response_wrapper(
            deals.search_by_object_type_id,
        )
        self.update_by_object_type_id = to_raw_response_wrapper(
            deals.update_by_object_type_id,
        )

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._deals.batch)


class AsyncDealsResourceWithRawResponse:
    def __init__(self, deals: AsyncDealsResource) -> None:
        self._deals = deals

        self.create_by_object_type_id = async_to_raw_response_wrapper(
            deals.create_by_object_type_id,
        )
        self.delete_by_object_type_id = async_to_raw_response_wrapper(
            deals.delete_by_object_type_id,
        )
        self.get_by_object_type_id = async_to_raw_response_wrapper(
            deals.get_by_object_type_id,
        )
        self.list_by_object_type_id = async_to_raw_response_wrapper(
            deals.list_by_object_type_id,
        )
        self.merge_by_object_type_id = async_to_raw_response_wrapper(
            deals.merge_by_object_type_id,
        )
        self.search_by_object_type_id = async_to_raw_response_wrapper(
            deals.search_by_object_type_id,
        )
        self.update_by_object_type_id = async_to_raw_response_wrapper(
            deals.update_by_object_type_id,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._deals.batch)


class DealsResourceWithStreamingResponse:
    def __init__(self, deals: DealsResource) -> None:
        self._deals = deals

        self.create_by_object_type_id = to_streamed_response_wrapper(
            deals.create_by_object_type_id,
        )
        self.delete_by_object_type_id = to_streamed_response_wrapper(
            deals.delete_by_object_type_id,
        )
        self.get_by_object_type_id = to_streamed_response_wrapper(
            deals.get_by_object_type_id,
        )
        self.list_by_object_type_id = to_streamed_response_wrapper(
            deals.list_by_object_type_id,
        )
        self.merge_by_object_type_id = to_streamed_response_wrapper(
            deals.merge_by_object_type_id,
        )
        self.search_by_object_type_id = to_streamed_response_wrapper(
            deals.search_by_object_type_id,
        )
        self.update_by_object_type_id = to_streamed_response_wrapper(
            deals.update_by_object_type_id,
        )

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._deals.batch)


class AsyncDealsResourceWithStreamingResponse:
    def __init__(self, deals: AsyncDealsResource) -> None:
        self._deals = deals

        self.create_by_object_type_id = async_to_streamed_response_wrapper(
            deals.create_by_object_type_id,
        )
        self.delete_by_object_type_id = async_to_streamed_response_wrapper(
            deals.delete_by_object_type_id,
        )
        self.get_by_object_type_id = async_to_streamed_response_wrapper(
            deals.get_by_object_type_id,
        )
        self.list_by_object_type_id = async_to_streamed_response_wrapper(
            deals.list_by_object_type_id,
        )
        self.merge_by_object_type_id = async_to_streamed_response_wrapper(
            deals.merge_by_object_type_id,
        )
        self.search_by_object_type_id = async_to_streamed_response_wrapper(
            deals.search_by_object_type_id,
        )
        self.update_by_object_type_id = async_to_streamed_response_wrapper(
            deals.update_by_object_type_id,
        )

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._deals.batch)
