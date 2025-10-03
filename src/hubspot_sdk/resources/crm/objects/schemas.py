# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
    schema_list_params,
    schema_create_params,
    schema_delete_params,
    schema_update_params,
    schema_create_association_params,
)
from ....types.crm_object_schema import CRMObjectSchema
from ....types.crm_association_definition import CRMAssociationDefinition
from ....types.crm_object_type_definition import CRMObjectTypeDefinition
from ....types.crm_object_type_property_create_param import CRMObjectTypePropertyCreateParam
from ....types.crm_object_type_definition_labels_param import CRMObjectTypeDefinitionLabelsParam
from ....types.crm_collection_response_object_schema_no_paging import CRMCollectionResponseObjectSchemaNoPaging

__all__ = ["SchemasResource", "AsyncSchemasResource"]


class SchemasResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return SchemasResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        associated_objects: SequenceNotStr[str],
        labels: CRMObjectTypeDefinitionLabelsParam,
        name: str,
        properties: Iterable[CRMObjectTypePropertyCreateParam],
        required_properties: SequenceNotStr[str],
        primary_display_property: str | Omit = omit,
        searchable_properties: SequenceNotStr[str] | Omit = omit,
        secondary_display_properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMObjectSchema:
        """
        Create a new schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/crm-object-schemas/v3/schemas",
            body=maybe_transform(
                {
                    "associated_objects": associated_objects,
                    "labels": labels,
                    "name": name,
                    "properties": properties,
                    "required_properties": required_properties,
                    "primary_display_property": primary_display_property,
                    "searchable_properties": searchable_properties,
                    "secondary_display_properties": secondary_display_properties,
                },
                schema_create_params.SchemaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectSchema,
        )

    def update(
        self,
        object_type: str,
        *,
        clear_description: bool | Omit = omit,
        labels: CRMObjectTypeDefinitionLabelsParam | Omit = omit,
        primary_display_property: str | Omit = omit,
        required_properties: SequenceNotStr[str] | Omit = omit,
        restorable: bool | Omit = omit,
        searchable_properties: SequenceNotStr[str] | Omit = omit,
        secondary_display_properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMObjectTypeDefinition:
        """
        Update a schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._patch(
            f"/crm-object-schemas/v3/schemas/{object_type}",
            body=maybe_transform(
                {
                    "clear_description": clear_description,
                    "labels": labels,
                    "primary_display_property": primary_display_property,
                    "required_properties": required_properties,
                    "restorable": restorable,
                    "searchable_properties": searchable_properties,
                    "secondary_display_properties": secondary_display_properties,
                },
                schema_update_params.SchemaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectTypeDefinition,
        )

    def list(
        self,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMCollectionResponseObjectSchemaNoPaging:
        """
        Get all schemas

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/crm-object-schemas/v3/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, schema_list_params.SchemaListParams),
            ),
            cast_to=CRMCollectionResponseObjectSchemaNoPaging,
        )

    def delete(
        self,
        object_type: str,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/crm-object-schemas/v3/schemas/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"archived": archived}, schema_delete_params.SchemaDeleteParams),
            ),
            cast_to=NoneType,
        )

    def archive_association(
        self,
        association_identifier: str,
        *,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove an association

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not association_identifier:
            raise ValueError(
                f"Expected a non-empty value for `association_identifier` but received {association_identifier!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/crm-object-schemas/v3/schemas/{object_type}/associations/{association_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_association(
        self,
        object_type: str,
        *,
        from_object_type_id: str,
        to_object_type_id: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMAssociationDefinition:
        """
        Create an association

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            f"/crm-object-schemas/v3/schemas/{object_type}/associations",
            body=maybe_transform(
                {
                    "from_object_type_id": from_object_type_id,
                    "to_object_type_id": to_object_type_id,
                    "name": name,
                },
                schema_create_association_params.SchemaCreateAssociationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMAssociationDefinition,
        )

    def read(
        self,
        object_type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMObjectSchema:
        """
        Get an existing schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._get(
            f"/crm-object-schemas/v3/schemas/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectSchema,
        )


class AsyncSchemasResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchemasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchemasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSchemasResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        associated_objects: SequenceNotStr[str],
        labels: CRMObjectTypeDefinitionLabelsParam,
        name: str,
        properties: Iterable[CRMObjectTypePropertyCreateParam],
        required_properties: SequenceNotStr[str],
        primary_display_property: str | Omit = omit,
        searchable_properties: SequenceNotStr[str] | Omit = omit,
        secondary_display_properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMObjectSchema:
        """
        Create a new schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/crm-object-schemas/v3/schemas",
            body=await async_maybe_transform(
                {
                    "associated_objects": associated_objects,
                    "labels": labels,
                    "name": name,
                    "properties": properties,
                    "required_properties": required_properties,
                    "primary_display_property": primary_display_property,
                    "searchable_properties": searchable_properties,
                    "secondary_display_properties": secondary_display_properties,
                },
                schema_create_params.SchemaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectSchema,
        )

    async def update(
        self,
        object_type: str,
        *,
        clear_description: bool | Omit = omit,
        labels: CRMObjectTypeDefinitionLabelsParam | Omit = omit,
        primary_display_property: str | Omit = omit,
        required_properties: SequenceNotStr[str] | Omit = omit,
        restorable: bool | Omit = omit,
        searchable_properties: SequenceNotStr[str] | Omit = omit,
        secondary_display_properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMObjectTypeDefinition:
        """
        Update a schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._patch(
            f"/crm-object-schemas/v3/schemas/{object_type}",
            body=await async_maybe_transform(
                {
                    "clear_description": clear_description,
                    "labels": labels,
                    "primary_display_property": primary_display_property,
                    "required_properties": required_properties,
                    "restorable": restorable,
                    "searchable_properties": searchable_properties,
                    "secondary_display_properties": secondary_display_properties,
                },
                schema_update_params.SchemaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectTypeDefinition,
        )

    async def list(
        self,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMCollectionResponseObjectSchemaNoPaging:
        """
        Get all schemas

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/crm-object-schemas/v3/schemas",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, schema_list_params.SchemaListParams),
            ),
            cast_to=CRMCollectionResponseObjectSchemaNoPaging,
        )

    async def delete(
        self,
        object_type: str,
        *,
        archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/crm-object-schemas/v3/schemas/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"archived": archived}, schema_delete_params.SchemaDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def archive_association(
        self,
        association_identifier: str,
        *,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove an association

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not association_identifier:
            raise ValueError(
                f"Expected a non-empty value for `association_identifier` but received {association_identifier!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/crm-object-schemas/v3/schemas/{object_type}/associations/{association_identifier}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_association(
        self,
        object_type: str,
        *,
        from_object_type_id: str,
        to_object_type_id: str,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMAssociationDefinition:
        """
        Create an association

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            f"/crm-object-schemas/v3/schemas/{object_type}/associations",
            body=await async_maybe_transform(
                {
                    "from_object_type_id": from_object_type_id,
                    "to_object_type_id": to_object_type_id,
                    "name": name,
                },
                schema_create_association_params.SchemaCreateAssociationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMAssociationDefinition,
        )

    async def read(
        self,
        object_type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMObjectSchema:
        """
        Get an existing schema

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._get(
            f"/crm-object-schemas/v3/schemas/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMObjectSchema,
        )


class SchemasResourceWithRawResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.create = to_raw_response_wrapper(
            schemas.create,
        )
        self.update = to_raw_response_wrapper(
            schemas.update,
        )
        self.list = to_raw_response_wrapper(
            schemas.list,
        )
        self.delete = to_raw_response_wrapper(
            schemas.delete,
        )
        self.archive_association = to_raw_response_wrapper(
            schemas.archive_association,
        )
        self.create_association = to_raw_response_wrapper(
            schemas.create_association,
        )
        self.read = to_raw_response_wrapper(
            schemas.read,
        )


class AsyncSchemasResourceWithRawResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.create = async_to_raw_response_wrapper(
            schemas.create,
        )
        self.update = async_to_raw_response_wrapper(
            schemas.update,
        )
        self.list = async_to_raw_response_wrapper(
            schemas.list,
        )
        self.delete = async_to_raw_response_wrapper(
            schemas.delete,
        )
        self.archive_association = async_to_raw_response_wrapper(
            schemas.archive_association,
        )
        self.create_association = async_to_raw_response_wrapper(
            schemas.create_association,
        )
        self.read = async_to_raw_response_wrapper(
            schemas.read,
        )


class SchemasResourceWithStreamingResponse:
    def __init__(self, schemas: SchemasResource) -> None:
        self._schemas = schemas

        self.create = to_streamed_response_wrapper(
            schemas.create,
        )
        self.update = to_streamed_response_wrapper(
            schemas.update,
        )
        self.list = to_streamed_response_wrapper(
            schemas.list,
        )
        self.delete = to_streamed_response_wrapper(
            schemas.delete,
        )
        self.archive_association = to_streamed_response_wrapper(
            schemas.archive_association,
        )
        self.create_association = to_streamed_response_wrapper(
            schemas.create_association,
        )
        self.read = to_streamed_response_wrapper(
            schemas.read,
        )


class AsyncSchemasResourceWithStreamingResponse:
    def __init__(self, schemas: AsyncSchemasResource) -> None:
        self._schemas = schemas

        self.create = async_to_streamed_response_wrapper(
            schemas.create,
        )
        self.update = async_to_streamed_response_wrapper(
            schemas.update,
        )
        self.list = async_to_streamed_response_wrapper(
            schemas.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            schemas.delete,
        )
        self.archive_association = async_to_streamed_response_wrapper(
            schemas.archive_association,
        )
        self.create_association = async_to_streamed_response_wrapper(
            schemas.create_association,
        )
        self.read = async_to_streamed_response_wrapper(
            schemas.read,
        )
