# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cms import url_redirect_list_params, url_redirect_create_params, url_redirect_update_params
from ..._base_client import make_request_options
from ...types.url_mapping import URLMapping
from ...types.collection_response_with_total_url_mapping_forward_paging import (
    CollectionResponseWithTotalURLMappingForwardPaging,
)

__all__ = ["URLRedirectsResource", "AsyncURLRedirectsResource"]


class URLRedirectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLRedirectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return URLRedirectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLRedirectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return URLRedirectsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        destination: str,
        redirect_style: int,
        route_prefix: str,
        is_match_full_url: bool | Omit = omit,
        is_match_query_string: bool | Omit = omit,
        is_only_after_not_found: bool | Omit = omit,
        is_pattern: bool | Omit = omit,
        is_protocol_agnostic: bool | Omit = omit,
        is_trailing_slash_optional: bool | Omit = omit,
        precedence: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLMapping:
        """
        Create a redirect

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/cms/v3/url-redirects/",
            body=maybe_transform(
                {
                    "destination": destination,
                    "redirect_style": redirect_style,
                    "route_prefix": route_prefix,
                    "is_match_full_url": is_match_full_url,
                    "is_match_query_string": is_match_query_string,
                    "is_only_after_not_found": is_only_after_not_found,
                    "is_pattern": is_pattern,
                    "is_protocol_agnostic": is_protocol_agnostic,
                    "is_trailing_slash_optional": is_trailing_slash_optional,
                    "precedence": precedence,
                },
                url_redirect_create_params.URLRedirectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLMapping,
        )

    def update(
        self,
        url_redirect_id: str,
        *,
        id: str,
        destination: str,
        is_match_full_url: bool,
        is_match_query_string: bool,
        is_only_after_not_found: bool,
        is_pattern: bool,
        is_protocol_agnostic: bool,
        is_trailing_slash_optional: bool,
        precedence: int,
        redirect_style: int,
        route_prefix: str,
        created: Union[str, datetime] | Omit = omit,
        updated: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLMapping:
        """
        Update a redirect

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_redirect_id:
            raise ValueError(f"Expected a non-empty value for `url_redirect_id` but received {url_redirect_id!r}")
        return self._patch(
            f"/cms/v3/url-redirects/{url_redirect_id}",
            body=maybe_transform(
                {
                    "id": id,
                    "destination": destination,
                    "is_match_full_url": is_match_full_url,
                    "is_match_query_string": is_match_query_string,
                    "is_only_after_not_found": is_only_after_not_found,
                    "is_pattern": is_pattern,
                    "is_protocol_agnostic": is_protocol_agnostic,
                    "is_trailing_slash_optional": is_trailing_slash_optional,
                    "precedence": precedence,
                    "redirect_style": redirect_style,
                    "route_prefix": route_prefix,
                    "created": created,
                    "updated": updated,
                },
                url_redirect_update_params.URLRedirectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLMapping,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
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
    ) -> CollectionResponseWithTotalURLMappingForwardPaging:
        """
        Get current redirects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/cms/v3/url-redirects/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    url_redirect_list_params.URLRedirectListParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalURLMappingForwardPaging,
        )

    def delete(
        self,
        url_redirect_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a redirect

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_redirect_id:
            raise ValueError(f"Expected a non-empty value for `url_redirect_id` but received {url_redirect_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/cms/v3/url-redirects/{url_redirect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def read(
        self,
        url_redirect_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLMapping:
        """
        Get details for a redirect

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_redirect_id:
            raise ValueError(f"Expected a non-empty value for `url_redirect_id` but received {url_redirect_id!r}")
        return self._get(
            f"/cms/v3/url-redirects/{url_redirect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLMapping,
        )


class AsyncURLRedirectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLRedirectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncURLRedirectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLRedirectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncURLRedirectsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        destination: str,
        redirect_style: int,
        route_prefix: str,
        is_match_full_url: bool | Omit = omit,
        is_match_query_string: bool | Omit = omit,
        is_only_after_not_found: bool | Omit = omit,
        is_pattern: bool | Omit = omit,
        is_protocol_agnostic: bool | Omit = omit,
        is_trailing_slash_optional: bool | Omit = omit,
        precedence: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLMapping:
        """
        Create a redirect

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/cms/v3/url-redirects/",
            body=await async_maybe_transform(
                {
                    "destination": destination,
                    "redirect_style": redirect_style,
                    "route_prefix": route_prefix,
                    "is_match_full_url": is_match_full_url,
                    "is_match_query_string": is_match_query_string,
                    "is_only_after_not_found": is_only_after_not_found,
                    "is_pattern": is_pattern,
                    "is_protocol_agnostic": is_protocol_agnostic,
                    "is_trailing_slash_optional": is_trailing_slash_optional,
                    "precedence": precedence,
                },
                url_redirect_create_params.URLRedirectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLMapping,
        )

    async def update(
        self,
        url_redirect_id: str,
        *,
        id: str,
        destination: str,
        is_match_full_url: bool,
        is_match_query_string: bool,
        is_only_after_not_found: bool,
        is_pattern: bool,
        is_protocol_agnostic: bool,
        is_trailing_slash_optional: bool,
        precedence: int,
        redirect_style: int,
        route_prefix: str,
        created: Union[str, datetime] | Omit = omit,
        updated: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLMapping:
        """
        Update a redirect

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_redirect_id:
            raise ValueError(f"Expected a non-empty value for `url_redirect_id` but received {url_redirect_id!r}")
        return await self._patch(
            f"/cms/v3/url-redirects/{url_redirect_id}",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "destination": destination,
                    "is_match_full_url": is_match_full_url,
                    "is_match_query_string": is_match_query_string,
                    "is_only_after_not_found": is_only_after_not_found,
                    "is_pattern": is_pattern,
                    "is_protocol_agnostic": is_protocol_agnostic,
                    "is_trailing_slash_optional": is_trailing_slash_optional,
                    "precedence": precedence,
                    "redirect_style": redirect_style,
                    "route_prefix": route_prefix,
                    "created": created,
                    "updated": updated,
                },
                url_redirect_update_params.URLRedirectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLMapping,
        )

    async def list(
        self,
        *,
        after: str | Omit = omit,
        archived: bool | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_before: Union[str, datetime] | Omit = omit,
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
    ) -> CollectionResponseWithTotalURLMappingForwardPaging:
        """
        Get current redirects

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/cms/v3/url-redirects/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "archived": archived,
                        "created_after": created_after,
                        "created_at": created_at,
                        "created_before": created_before,
                        "limit": limit,
                        "sort": sort,
                        "updated_after": updated_after,
                        "updated_at": updated_at,
                        "updated_before": updated_before,
                    },
                    url_redirect_list_params.URLRedirectListParams,
                ),
            ),
            cast_to=CollectionResponseWithTotalURLMappingForwardPaging,
        )

    async def delete(
        self,
        url_redirect_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a redirect

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_redirect_id:
            raise ValueError(f"Expected a non-empty value for `url_redirect_id` but received {url_redirect_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/cms/v3/url-redirects/{url_redirect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def read(
        self,
        url_redirect_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLMapping:
        """
        Get details for a redirect

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not url_redirect_id:
            raise ValueError(f"Expected a non-empty value for `url_redirect_id` but received {url_redirect_id!r}")
        return await self._get(
            f"/cms/v3/url-redirects/{url_redirect_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLMapping,
        )


class URLRedirectsResourceWithRawResponse:
    def __init__(self, url_redirects: URLRedirectsResource) -> None:
        self._url_redirects = url_redirects

        self.create = to_raw_response_wrapper(
            url_redirects.create,
        )
        self.update = to_raw_response_wrapper(
            url_redirects.update,
        )
        self.list = to_raw_response_wrapper(
            url_redirects.list,
        )
        self.delete = to_raw_response_wrapper(
            url_redirects.delete,
        )
        self.read = to_raw_response_wrapper(
            url_redirects.read,
        )


class AsyncURLRedirectsResourceWithRawResponse:
    def __init__(self, url_redirects: AsyncURLRedirectsResource) -> None:
        self._url_redirects = url_redirects

        self.create = async_to_raw_response_wrapper(
            url_redirects.create,
        )
        self.update = async_to_raw_response_wrapper(
            url_redirects.update,
        )
        self.list = async_to_raw_response_wrapper(
            url_redirects.list,
        )
        self.delete = async_to_raw_response_wrapper(
            url_redirects.delete,
        )
        self.read = async_to_raw_response_wrapper(
            url_redirects.read,
        )


class URLRedirectsResourceWithStreamingResponse:
    def __init__(self, url_redirects: URLRedirectsResource) -> None:
        self._url_redirects = url_redirects

        self.create = to_streamed_response_wrapper(
            url_redirects.create,
        )
        self.update = to_streamed_response_wrapper(
            url_redirects.update,
        )
        self.list = to_streamed_response_wrapper(
            url_redirects.list,
        )
        self.delete = to_streamed_response_wrapper(
            url_redirects.delete,
        )
        self.read = to_streamed_response_wrapper(
            url_redirects.read,
        )


class AsyncURLRedirectsResourceWithStreamingResponse:
    def __init__(self, url_redirects: AsyncURLRedirectsResource) -> None:
        self._url_redirects = url_redirects

        self.create = async_to_streamed_response_wrapper(
            url_redirects.create,
        )
        self.update = async_to_streamed_response_wrapper(
            url_redirects.update,
        )
        self.list = async_to_streamed_response_wrapper(
            url_redirects.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            url_redirects.delete,
        )
        self.read = async_to_streamed_response_wrapper(
            url_redirects.read,
        )
