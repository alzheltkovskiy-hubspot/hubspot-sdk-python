# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.crm import (
    property_read_params,
    property_create_params,
    property_update_params,
    property_get_by_name_params,
)
from ..._base_client import make_request_options
from ...types.property import Property
from ...types.crm.option_input_param import OptionInputParam
from ...types.crm.property_name_param import PropertyNameParam
from ...types.crm.batch_response_property import BatchResponseProperty
from ...types.crm.created_response_property_group import CreatedResponsePropertyGroup
from ...types.crm.collection_response_property_group import CollectionResponsePropertyGroup

__all__ = ["PropertiesResource", "AsyncPropertiesResource"]


class PropertiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#with_streaming_response
        """
        return PropertiesResourceWithStreamingResponse(self)

    def create(
        self,
        object_type: str,
        *,
        label: str,
        name: str,
        display_order: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedResponsePropertyGroup:
        """
        Create and return a copy of a new property group.

        Args:
          label: A human-readable label that will be shown in HubSpot.

          name: The internal property group name, which must be used when referencing the
              property group via the API.

          display_order: Property groups are displayed in order starting with the lowest positive integer
              value. Values of -1 will cause the property group to be displayed after any
              positive values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            f"/crm/v3/properties/{object_type}/groups",
            body=maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "display_order": display_order,
                },
                property_create_params.PropertyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedResponsePropertyGroup,
        )

    def update(
        self,
        property_name: str,
        *,
        object_type: str,
        calculation_formula: str | Omit = omit,
        description: str | Omit = omit,
        display_order: int | Omit = omit,
        field_type: Literal[
            "booleancheckbox",
            "calculation_equation",
            "checkbox",
            "date",
            "file",
            "html",
            "number",
            "phonenumber",
            "radio",
            "select",
            "text",
            "textarea",
        ]
        | Omit = omit,
        form_field: bool | Omit = omit,
        group_name: str | Omit = omit,
        hidden: bool | Omit = omit,
        label: str | Omit = omit,
        options: Iterable[OptionInputParam] | Omit = omit,
        type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """Perform a partial update of a property identified by { propertyName }.

        Provided
        fields will be overwritten.

        Args:
          calculation_formula: Represents a formula that is used to compute a calculated property.

          description: A description of the property that will be shown as help text in HubSpot.

          display_order: Properties are displayed in order starting with the lowest positive integer
              value. Values of -1 will cause the Property to be displayed after any positive
              values.

          field_type: Controls how the property appears in HubSpot.

          form_field: Whether or not the property can be used in a HubSpot form.

          group_name: The name of the property group the property belongs to.

          hidden: If true, the property won't be visible and can't be used in HubSpot.

          label: A human-readable property label that will be shown in HubSpot.

          options: A list of valid options for the property.

          type: The data type of the property.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return self._patch(
            f"/crm/v3/properties/{object_type}/{property_name}",
            body=maybe_transform(
                {
                    "calculation_formula": calculation_formula,
                    "description": description,
                    "display_order": display_order,
                    "field_type": field_type,
                    "form_field": form_field,
                    "group_name": group_name,
                    "hidden": hidden,
                    "label": label,
                    "options": options,
                    "type": type,
                },
                property_update_params.PropertyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )

    def list(
        self,
        object_type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePropertyGroup:
        """
        Read all existing property groups for the specified object type and HubSpot
        account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._get(
            f"/crm/v3/properties/{object_type}/groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePropertyGroup,
        )

    def delete(
        self,
        property_name: str,
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
        Move a property identified by {propertyName} to the recycling bin.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/crm/v3/properties/{object_type}/{property_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_by_name(
        self,
        property_name: str,
        *,
        object_type: str,
        archived: bool | Omit = omit,
        properties: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Read a property identified by {propertyName}.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return self._get(
            f"/crm/v3/properties/{object_type}/{property_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "properties": properties,
                    },
                    property_get_by_name_params.PropertyGetByNameParams,
                ),
            ),
            cast_to=Property,
        )

    def read(
        self,
        object_type: str,
        *,
        archived: bool,
        inputs: Iterable[PropertyNameParam],
        data_sensitivity: Literal["non_sensitive", "sensitive", "highly_sensitive"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseProperty:
        """
        Read a provided list of properties.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            f"/crm/v3/properties/{object_type}/batch/read",
            body=maybe_transform(
                {
                    "archived": archived,
                    "inputs": inputs,
                    "data_sensitivity": data_sensitivity,
                },
                property_read_params.PropertyReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseProperty,
        )


class AsyncPropertiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPropertiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPropertiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPropertiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPropertiesResourceWithStreamingResponse(self)

    async def create(
        self,
        object_type: str,
        *,
        label: str,
        name: str,
        display_order: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreatedResponsePropertyGroup:
        """
        Create and return a copy of a new property group.

        Args:
          label: A human-readable label that will be shown in HubSpot.

          name: The internal property group name, which must be used when referencing the
              property group via the API.

          display_order: Property groups are displayed in order starting with the lowest positive integer
              value. Values of -1 will cause the property group to be displayed after any
              positive values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            f"/crm/v3/properties/{object_type}/groups",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "display_order": display_order,
                },
                property_create_params.PropertyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreatedResponsePropertyGroup,
        )

    async def update(
        self,
        property_name: str,
        *,
        object_type: str,
        calculation_formula: str | Omit = omit,
        description: str | Omit = omit,
        display_order: int | Omit = omit,
        field_type: Literal[
            "booleancheckbox",
            "calculation_equation",
            "checkbox",
            "date",
            "file",
            "html",
            "number",
            "phonenumber",
            "radio",
            "select",
            "text",
            "textarea",
        ]
        | Omit = omit,
        form_field: bool | Omit = omit,
        group_name: str | Omit = omit,
        hidden: bool | Omit = omit,
        label: str | Omit = omit,
        options: Iterable[OptionInputParam] | Omit = omit,
        type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """Perform a partial update of a property identified by { propertyName }.

        Provided
        fields will be overwritten.

        Args:
          calculation_formula: Represents a formula that is used to compute a calculated property.

          description: A description of the property that will be shown as help text in HubSpot.

          display_order: Properties are displayed in order starting with the lowest positive integer
              value. Values of -1 will cause the Property to be displayed after any positive
              values.

          field_type: Controls how the property appears in HubSpot.

          form_field: Whether or not the property can be used in a HubSpot form.

          group_name: The name of the property group the property belongs to.

          hidden: If true, the property won't be visible and can't be used in HubSpot.

          label: A human-readable property label that will be shown in HubSpot.

          options: A list of valid options for the property.

          type: The data type of the property.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return await self._patch(
            f"/crm/v3/properties/{object_type}/{property_name}",
            body=await async_maybe_transform(
                {
                    "calculation_formula": calculation_formula,
                    "description": description,
                    "display_order": display_order,
                    "field_type": field_type,
                    "form_field": form_field,
                    "group_name": group_name,
                    "hidden": hidden,
                    "label": label,
                    "options": options,
                    "type": type,
                },
                property_update_params.PropertyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Property,
        )

    async def list(
        self,
        object_type: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePropertyGroup:
        """
        Read all existing property groups for the specified object type and HubSpot
        account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._get(
            f"/crm/v3/properties/{object_type}/groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePropertyGroup,
        )

    async def delete(
        self,
        property_name: str,
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
        Move a property identified by {propertyName} to the recycling bin.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/crm/v3/properties/{object_type}/{property_name}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_by_name(
        self,
        property_name: str,
        *,
        object_type: str,
        archived: bool | Omit = omit,
        properties: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Property:
        """
        Read a property identified by {propertyName}.

        Args:
          archived: Whether to return only results that have been archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not property_name:
            raise ValueError(f"Expected a non-empty value for `property_name` but received {property_name!r}")
        return await self._get(
            f"/crm/v3/properties/{object_type}/{property_name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "properties": properties,
                    },
                    property_get_by_name_params.PropertyGetByNameParams,
                ),
            ),
            cast_to=Property,
        )

    async def read(
        self,
        object_type: str,
        *,
        archived: bool,
        inputs: Iterable[PropertyNameParam],
        data_sensitivity: Literal["non_sensitive", "sensitive", "highly_sensitive"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseProperty:
        """
        Read a provided list of properties.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            f"/crm/v3/properties/{object_type}/batch/read",
            body=await async_maybe_transform(
                {
                    "archived": archived,
                    "inputs": inputs,
                    "data_sensitivity": data_sensitivity,
                },
                property_read_params.PropertyReadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseProperty,
        )


class PropertiesResourceWithRawResponse:
    def __init__(self, properties: PropertiesResource) -> None:
        self._properties = properties

        self.create = to_raw_response_wrapper(
            properties.create,
        )
        self.update = to_raw_response_wrapper(
            properties.update,
        )
        self.list = to_raw_response_wrapper(
            properties.list,
        )
        self.delete = to_raw_response_wrapper(
            properties.delete,
        )
        self.get_by_name = to_raw_response_wrapper(
            properties.get_by_name,
        )
        self.read = to_raw_response_wrapper(
            properties.read,
        )


class AsyncPropertiesResourceWithRawResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

        self.create = async_to_raw_response_wrapper(
            properties.create,
        )
        self.update = async_to_raw_response_wrapper(
            properties.update,
        )
        self.list = async_to_raw_response_wrapper(
            properties.list,
        )
        self.delete = async_to_raw_response_wrapper(
            properties.delete,
        )
        self.get_by_name = async_to_raw_response_wrapper(
            properties.get_by_name,
        )
        self.read = async_to_raw_response_wrapper(
            properties.read,
        )


class PropertiesResourceWithStreamingResponse:
    def __init__(self, properties: PropertiesResource) -> None:
        self._properties = properties

        self.create = to_streamed_response_wrapper(
            properties.create,
        )
        self.update = to_streamed_response_wrapper(
            properties.update,
        )
        self.list = to_streamed_response_wrapper(
            properties.list,
        )
        self.delete = to_streamed_response_wrapper(
            properties.delete,
        )
        self.get_by_name = to_streamed_response_wrapper(
            properties.get_by_name,
        )
        self.read = to_streamed_response_wrapper(
            properties.read,
        )


class AsyncPropertiesResourceWithStreamingResponse:
    def __init__(self, properties: AsyncPropertiesResource) -> None:
        self._properties = properties

        self.create = async_to_streamed_response_wrapper(
            properties.create,
        )
        self.update = async_to_streamed_response_wrapper(
            properties.update,
        )
        self.list = async_to_streamed_response_wrapper(
            properties.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            properties.delete,
        )
        self.get_by_name = async_to_streamed_response_wrapper(
            properties.get_by_name,
        )
        self.read = async_to_streamed_response_wrapper(
            properties.read,
        )
