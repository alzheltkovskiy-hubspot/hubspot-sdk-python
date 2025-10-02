# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.crm.associations import v4_list_params, v4_archive_labels_params
from ....types.crm_batch_response_public_default_association import CRMBatchResponsePublicDefaultAssociation
from ....types.crm_created_response_labels_between_object_pair import CRMCreatedResponseLabelsBetweenObjectPair
from ....types.crm.associations.crm_associations_v4_batch_response_void import CRMAssociationsV4BatchResponseVoid
from ....types.crm_collection_response_multi_associated_object_with_label import (
    CRMCollectionResponseMultiAssociatedObjectWithLabel,
)
from ....types.crm.associations.crm_associations_v4_association_spec_1_param import (
    CRMAssociationsV4AssociationSpec1Param,
)
from ....types.crm.associations.crm_associations_v4_report_creation_response import (
    CRMAssociationsV4ReportCreationResponse,
)
from ....types.crm.associations.crm_associations_v4_public_association_multi_post_param import (
    CRMAssociationsV4PublicAssociationMultiPostParam,
)

__all__ = ["V4Resource", "AsyncV4Resource"]


class V4Resource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V4ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V4ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V4ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return V4ResourceWithStreamingResponse(self)

    def create(
        self,
        to_object_id: str,
        *,
        object_type: str,
        object_id: str,
        to_object_type: str,
        body: Iterable[CRMAssociationsV4AssociationSpec1Param],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMCreatedResponseLabelsBetweenObjectPair:
        """
        Create

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        return self._put(
            f"/crm/v4/objects/{object_type}/{object_id}/associations/{to_object_type}/{to_object_id}",
            body=maybe_transform(body, Iterable[CRMAssociationsV4AssociationSpec1Param]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMCreatedResponseLabelsBetweenObjectPair,
        )

    def list(
        self,
        to_object_type: str,
        *,
        object_type: str,
        object_id: str,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMCollectionResponseMultiAssociatedObjectWithLabel:
        """
        List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return self._get(
            f"/crm/v4/objects/{object_type}/{object_id}/associations/{to_object_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    v4_list_params.V4ListParams,
                ),
            ),
            cast_to=CRMCollectionResponseMultiAssociatedObjectWithLabel,
        )

    def delete(
        self,
        to_object_id: str,
        *,
        object_type: str,
        object_id: str,
        to_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/crm/v4/objects/{object_type}/{object_id}/associations/{to_object_type}/{to_object_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def archive_labels(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[CRMAssociationsV4PublicAssociationMultiPostParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMAssociationsV4BatchResponseVoid:
        """
        Delete Specific Labels

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return self._post(
            f"/crm/v4/associations/{from_object_type}/{to_object_type}/batch/labels/archive",
            body=maybe_transform({"inputs": inputs}, v4_archive_labels_params.V4ArchiveLabelsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMAssociationsV4BatchResponseVoid,
        )

    def create_default(
        self,
        to_object_id: str,
        *,
        from_object_type: str,
        from_object_id: str,
        to_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMBatchResponsePublicDefaultAssociation:
        """
        Create Default

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not from_object_id:
            raise ValueError(f"Expected a non-empty value for `from_object_id` but received {from_object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        return self._put(
            f"/crm/v4/objects/{from_object_type}/{from_object_id}/associations/default/{to_object_type}/{to_object_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMBatchResponsePublicDefaultAssociation,
        )

    def request(
        self,
        user_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMAssociationsV4ReportCreationResponse:
        """
        Report

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/crm/v4/associations/usage/high-usage-report/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMAssociationsV4ReportCreationResponse,
        )


class AsyncV4Resource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV4ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV4ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV4ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncV4ResourceWithStreamingResponse(self)

    async def create(
        self,
        to_object_id: str,
        *,
        object_type: str,
        object_id: str,
        to_object_type: str,
        body: Iterable[CRMAssociationsV4AssociationSpec1Param],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMCreatedResponseLabelsBetweenObjectPair:
        """
        Create

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        return await self._put(
            f"/crm/v4/objects/{object_type}/{object_id}/associations/{to_object_type}/{to_object_id}",
            body=await async_maybe_transform(body, Iterable[CRMAssociationsV4AssociationSpec1Param]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMCreatedResponseLabelsBetweenObjectPair,
        )

    async def list(
        self,
        to_object_type: str,
        *,
        object_type: str,
        object_id: str,
        after: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMCollectionResponseMultiAssociatedObjectWithLabel:
        """
        List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return await self._get(
            f"/crm/v4/objects/{object_type}/{object_id}/associations/{to_object_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "limit": limit,
                    },
                    v4_list_params.V4ListParams,
                ),
            ),
            cast_to=CRMCollectionResponseMultiAssociatedObjectWithLabel,
        )

    async def delete(
        self,
        to_object_id: str,
        *,
        object_type: str,
        object_id: str,
        to_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not object_id:
            raise ValueError(f"Expected a non-empty value for `object_id` but received {object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/crm/v4/objects/{object_type}/{object_id}/associations/{to_object_type}/{to_object_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def archive_labels(
        self,
        to_object_type: str,
        *,
        from_object_type: str,
        inputs: Iterable[CRMAssociationsV4PublicAssociationMultiPostParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMAssociationsV4BatchResponseVoid:
        """
        Delete Specific Labels

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        return await self._post(
            f"/crm/v4/associations/{from_object_type}/{to_object_type}/batch/labels/archive",
            body=await async_maybe_transform({"inputs": inputs}, v4_archive_labels_params.V4ArchiveLabelsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMAssociationsV4BatchResponseVoid,
        )

    async def create_default(
        self,
        to_object_id: str,
        *,
        from_object_type: str,
        from_object_id: str,
        to_object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMBatchResponsePublicDefaultAssociation:
        """
        Create Default

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not from_object_type:
            raise ValueError(f"Expected a non-empty value for `from_object_type` but received {from_object_type!r}")
        if not from_object_id:
            raise ValueError(f"Expected a non-empty value for `from_object_id` but received {from_object_id!r}")
        if not to_object_type:
            raise ValueError(f"Expected a non-empty value for `to_object_type` but received {to_object_type!r}")
        if not to_object_id:
            raise ValueError(f"Expected a non-empty value for `to_object_id` but received {to_object_id!r}")
        return await self._put(
            f"/crm/v4/objects/{from_object_type}/{from_object_id}/associations/default/{to_object_type}/{to_object_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMBatchResponsePublicDefaultAssociation,
        )

    async def request(
        self,
        user_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMAssociationsV4ReportCreationResponse:
        """
        Report

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/crm/v4/associations/usage/high-usage-report/{user_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMAssociationsV4ReportCreationResponse,
        )


class V4ResourceWithRawResponse:
    def __init__(self, v4: V4Resource) -> None:
        self._v4 = v4

        self.create = to_raw_response_wrapper(
            v4.create,
        )
        self.list = to_raw_response_wrapper(
            v4.list,
        )
        self.delete = to_raw_response_wrapper(
            v4.delete,
        )
        self.archive_labels = to_raw_response_wrapper(
            v4.archive_labels,
        )
        self.create_default = to_raw_response_wrapper(
            v4.create_default,
        )
        self.request = to_raw_response_wrapper(
            v4.request,
        )


class AsyncV4ResourceWithRawResponse:
    def __init__(self, v4: AsyncV4Resource) -> None:
        self._v4 = v4

        self.create = async_to_raw_response_wrapper(
            v4.create,
        )
        self.list = async_to_raw_response_wrapper(
            v4.list,
        )
        self.delete = async_to_raw_response_wrapper(
            v4.delete,
        )
        self.archive_labels = async_to_raw_response_wrapper(
            v4.archive_labels,
        )
        self.create_default = async_to_raw_response_wrapper(
            v4.create_default,
        )
        self.request = async_to_raw_response_wrapper(
            v4.request,
        )


class V4ResourceWithStreamingResponse:
    def __init__(self, v4: V4Resource) -> None:
        self._v4 = v4

        self.create = to_streamed_response_wrapper(
            v4.create,
        )
        self.list = to_streamed_response_wrapper(
            v4.list,
        )
        self.delete = to_streamed_response_wrapper(
            v4.delete,
        )
        self.archive_labels = to_streamed_response_wrapper(
            v4.archive_labels,
        )
        self.create_default = to_streamed_response_wrapper(
            v4.create_default,
        )
        self.request = to_streamed_response_wrapper(
            v4.request,
        )


class AsyncV4ResourceWithStreamingResponse:
    def __init__(self, v4: AsyncV4Resource) -> None:
        self._v4 = v4

        self.create = async_to_streamed_response_wrapper(
            v4.create,
        )
        self.list = async_to_streamed_response_wrapper(
            v4.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            v4.delete,
        )
        self.archive_labels = async_to_streamed_response_wrapper(
            v4.archive_labels,
        )
        self.create_default = async_to_streamed_response_wrapper(
            v4.create_default,
        )
        self.request = async_to_streamed_response_wrapper(
            v4.request,
        )
