# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.crm.objects import (
    company_list_params,
    company_read_params,
    company_merge_params,
    company_create_params,
    company_delete_params,
    company_search_params,
    company_update_params,
    company_upsert_params,
)
from ....types.crm.crm_objects_filter_group_param import CRMObjectsFilterGroupParam
from ....types.crm.crm_objects_simple_public_object import CRMObjectsSimplePublicObject
from ....types.crm.crm_objects_simple_public_object_id_param import CRMObjectsSimplePublicObjectIDParam
from ....types.crm.crm_objects_batch_response_simple_public_object import CRMObjectsBatchResponseSimplePublicObject
from ....types.crm.crm_objects_public_associations_for_object_param import CRMObjectsPublicAssociationsForObjectParam
from ....types.crm.crm_objects_created_response_simple_public_object import CRMObjectsCreatedResponseSimplePublicObject
from ....types.crm.crm_objects_simple_public_object_batch_input_param import CRMObjectsSimplePublicObjectBatchInputParam
from ....types.crm.crm_objects_simple_public_object_with_associations import (
    CRMObjectsSimplePublicObjectWithAssociations,
)
from ....types.crm.crm_objects_batch_response_simple_public_upsert_object import (
    CRMObjectsBatchResponseSimplePublicUpsertObject,
)
from ....types.crm.crm_objects_simple_public_object_batch_input_upsert_param import (
    CRMObjectsSimplePublicObjectBatchInputUpsertParam,
)
from ....types.crm.crm_objects_collection_response_with_total_simple_public_object import (
    CRMObjectsCollectionResponseWithTotalSimplePublicObject,
)
from ....types.crm.crm_objects_collection_response_simple_public_object_with_associations import (
    CRMObjectsCollectionResponseSimplePublicObjectWithAssociations,
)

__all__ = ["CompaniesResource", "AsyncCompaniesResource"]


class CompaniesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CompaniesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        properties: Dict[str, str],
        associations: Iterable[CRMObjectsPublicAssociationsForObjectParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMObjectsCreatedResponseSimplePublicObject:
        """
        Create a company

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/objects/companies",
            body=maybe_transform(
                {
                    "properties": properties,
                    "associations": associations,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectsCreatedResponseSimplePublicObject,
        )

    def update(
        self,
        *,
        inputs: Iterable[CRMObjectsSimplePublicObjectBatchInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMObjectsBatchResponseSimplePublicObject:
        """
        Update a batch of companies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/objects/companies/batch/update",
            body=maybe_transform({"inputs": inputs}, company_update_params.CompanyUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectsBatchResponseSimplePublicObject,
        )

    def list(
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
    ) -> CRMObjectsCollectionResponseSimplePublicObjectWithAssociations:
        """
        Retrieve companies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/crm/v3/objects/companies",
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
                    company_list_params.CompanyListParams,
                ),
            ),
            cast_to=CRMObjectsCollectionResponseSimplePublicObjectWithAssociations,
        )

    def delete(
        self,
        *,
        inputs: Iterable[CRMObjectsSimplePublicObjectIDParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive a batch of companies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/crm/v3/objects/companies/batch/archive",
            body=maybe_transform({"inputs": inputs}, company_delete_params.CompanyDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def merge(
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
    ) -> CRMObjectsSimplePublicObject:
        """
        Merge two companies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/objects/companies/merge",
            body=maybe_transform(
                {
                    "object_id_to_merge": object_id_to_merge,
                    "primary_object_id": primary_object_id,
                },
                company_merge_params.CompanyMergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectsSimplePublicObject,
        )

    def read(
        self,
        company_id: str,
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
    ) -> CRMObjectsSimplePublicObjectWithAssociations:
        """
        Retrieve a company

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return self._get(
            f"/crm/v3/objects/companies/{company_id}",
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
                    company_read_params.CompanyReadParams,
                ),
            ),
            cast_to=CRMObjectsSimplePublicObjectWithAssociations,
        )

    def search(
        self,
        *,
        after: str | Omit = omit,
        filter_groups: Iterable[CRMObjectsFilterGroupParam] | Omit = omit,
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
    ) -> CRMObjectsCollectionResponseWithTotalSimplePublicObject:
        """
        Search for companies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/objects/companies/search",
            body=maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "query": query,
                    "sorts": sorts,
                },
                company_search_params.CompanySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectsCollectionResponseWithTotalSimplePublicObject,
        )

    def upsert(
        self,
        *,
        inputs: Iterable[CRMObjectsSimplePublicObjectBatchInputUpsertParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMObjectsBatchResponseSimplePublicUpsertObject:
        """
        Create or update a batch of companies by unique property values

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm/v3/objects/companies/batch/upsert",
            body=maybe_transform({"inputs": inputs}, company_upsert_params.CompanyUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectsBatchResponseSimplePublicUpsertObject,
        )


class AsyncCompaniesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompaniesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompaniesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompaniesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCompaniesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        properties: Dict[str, str],
        associations: Iterable[CRMObjectsPublicAssociationsForObjectParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMObjectsCreatedResponseSimplePublicObject:
        """
        Create a company

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/objects/companies",
            body=await async_maybe_transform(
                {
                    "properties": properties,
                    "associations": associations,
                },
                company_create_params.CompanyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectsCreatedResponseSimplePublicObject,
        )

    async def update(
        self,
        *,
        inputs: Iterable[CRMObjectsSimplePublicObjectBatchInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMObjectsBatchResponseSimplePublicObject:
        """
        Update a batch of companies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/objects/companies/batch/update",
            body=await async_maybe_transform({"inputs": inputs}, company_update_params.CompanyUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectsBatchResponseSimplePublicObject,
        )

    async def list(
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
    ) -> CRMObjectsCollectionResponseSimplePublicObjectWithAssociations:
        """
        Retrieve companies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/crm/v3/objects/companies",
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
                    company_list_params.CompanyListParams,
                ),
            ),
            cast_to=CRMObjectsCollectionResponseSimplePublicObjectWithAssociations,
        )

    async def delete(
        self,
        *,
        inputs: Iterable[CRMObjectsSimplePublicObjectIDParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Archive a batch of companies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/crm/v3/objects/companies/batch/archive",
            body=await async_maybe_transform({"inputs": inputs}, company_delete_params.CompanyDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def merge(
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
    ) -> CRMObjectsSimplePublicObject:
        """
        Merge two companies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/objects/companies/merge",
            body=await async_maybe_transform(
                {
                    "object_id_to_merge": object_id_to_merge,
                    "primary_object_id": primary_object_id,
                },
                company_merge_params.CompanyMergeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectsSimplePublicObject,
        )

    async def read(
        self,
        company_id: str,
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
    ) -> CRMObjectsSimplePublicObjectWithAssociations:
        """
        Retrieve a company

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not company_id:
            raise ValueError(f"Expected a non-empty value for `company_id` but received {company_id!r}")
        return await self._get(
            f"/crm/v3/objects/companies/{company_id}",
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
                    company_read_params.CompanyReadParams,
                ),
            ),
            cast_to=CRMObjectsSimplePublicObjectWithAssociations,
        )

    async def search(
        self,
        *,
        after: str | Omit = omit,
        filter_groups: Iterable[CRMObjectsFilterGroupParam] | Omit = omit,
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
    ) -> CRMObjectsCollectionResponseWithTotalSimplePublicObject:
        """
        Search for companies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/objects/companies/search",
            body=await async_maybe_transform(
                {
                    "after": after,
                    "filter_groups": filter_groups,
                    "limit": limit,
                    "properties": properties,
                    "query": query,
                    "sorts": sorts,
                },
                company_search_params.CompanySearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectsCollectionResponseWithTotalSimplePublicObject,
        )

    async def upsert(
        self,
        *,
        inputs: Iterable[CRMObjectsSimplePublicObjectBatchInputUpsertParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMObjectsBatchResponseSimplePublicUpsertObject:
        """
        Create or update a batch of companies by unique property values

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm/v3/objects/companies/batch/upsert",
            body=await async_maybe_transform({"inputs": inputs}, company_upsert_params.CompanyUpsertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectsBatchResponseSimplePublicUpsertObject,
        )


class CompaniesResourceWithRawResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_raw_response_wrapper(
            companies.create,
        )
        self.update = to_raw_response_wrapper(
            companies.update,
        )
        self.list = to_raw_response_wrapper(
            companies.list,
        )
        self.delete = to_raw_response_wrapper(
            companies.delete,
        )
        self.merge = to_raw_response_wrapper(
            companies.merge,
        )
        self.read = to_raw_response_wrapper(
            companies.read,
        )
        self.search = to_raw_response_wrapper(
            companies.search,
        )
        self.upsert = to_raw_response_wrapper(
            companies.upsert,
        )


class AsyncCompaniesResourceWithRawResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_raw_response_wrapper(
            companies.create,
        )
        self.update = async_to_raw_response_wrapper(
            companies.update,
        )
        self.list = async_to_raw_response_wrapper(
            companies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            companies.delete,
        )
        self.merge = async_to_raw_response_wrapper(
            companies.merge,
        )
        self.read = async_to_raw_response_wrapper(
            companies.read,
        )
        self.search = async_to_raw_response_wrapper(
            companies.search,
        )
        self.upsert = async_to_raw_response_wrapper(
            companies.upsert,
        )


class CompaniesResourceWithStreamingResponse:
    def __init__(self, companies: CompaniesResource) -> None:
        self._companies = companies

        self.create = to_streamed_response_wrapper(
            companies.create,
        )
        self.update = to_streamed_response_wrapper(
            companies.update,
        )
        self.list = to_streamed_response_wrapper(
            companies.list,
        )
        self.delete = to_streamed_response_wrapper(
            companies.delete,
        )
        self.merge = to_streamed_response_wrapper(
            companies.merge,
        )
        self.read = to_streamed_response_wrapper(
            companies.read,
        )
        self.search = to_streamed_response_wrapper(
            companies.search,
        )
        self.upsert = to_streamed_response_wrapper(
            companies.upsert,
        )


class AsyncCompaniesResourceWithStreamingResponse:
    def __init__(self, companies: AsyncCompaniesResource) -> None:
        self._companies = companies

        self.create = async_to_streamed_response_wrapper(
            companies.create,
        )
        self.update = async_to_streamed_response_wrapper(
            companies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            companies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            companies.delete,
        )
        self.merge = async_to_streamed_response_wrapper(
            companies.merge,
        )
        self.read = async_to_streamed_response_wrapper(
            companies.read,
        )
        self.search = async_to_streamed_response_wrapper(
            companies.search,
        )
        self.upsert = async_to_streamed_response_wrapper(
            companies.upsert,
        )
