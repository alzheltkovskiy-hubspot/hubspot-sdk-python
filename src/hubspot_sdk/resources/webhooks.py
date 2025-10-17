# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    webhook_create_params,
    webhook_update_params,
    webhook_configure_params,
    webhook_update_batch_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.settings_response import SettingsResponse
from ..types.subscription_response import SubscriptionResponse
from ..types.throttling_settings_param import ThrottlingSettingsParam
from ..types.subscription_list_response import SubscriptionListResponse
from ..types.batch_response_subscription_response import BatchResponseSubscriptionResponse
from ..types.subscription_batch_update_request_param import SubscriptionBatchUpdateRequestParam

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)

    def create(
        self,
        app_id: int,
        *,
        event_type: Literal[
            "contact.propertyChange",
            "company.propertyChange",
            "deal.propertyChange",
            "ticket.propertyChange",
            "product.propertyChange",
            "line_item.propertyChange",
            "contact.creation",
            "contact.deletion",
            "contact.privacyDeletion",
            "company.creation",
            "company.deletion",
            "deal.creation",
            "deal.deletion",
            "ticket.creation",
            "ticket.deletion",
            "product.creation",
            "product.deletion",
            "line_item.creation",
            "line_item.deletion",
            "conversation.creation",
            "conversation.deletion",
            "conversation.newMessage",
            "conversation.privacyDeletion",
            "conversation.propertyChange",
            "contact.merge",
            "company.merge",
            "deal.merge",
            "ticket.merge",
            "product.merge",
            "line_item.merge",
            "contact.restore",
            "company.restore",
            "deal.restore",
            "ticket.restore",
            "product.restore",
            "line_item.restore",
            "contact.associationChange",
            "company.associationChange",
            "deal.associationChange",
            "ticket.associationChange",
            "line_item.associationChange",
            "object.propertyChange",
            "object.creation",
            "object.deletion",
            "object.merge",
            "object.restore",
            "object.associationChange",
        ],
        active: bool | Omit = omit,
        object_type_id: str | Omit = omit,
        property_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create new event subscription for the specified app.

        Args:
          event_type: Type of event to listen for. Can be one of `create`, `delete`,
              `deletedForPrivacy`, or `propertyChange`.

          active: Determines if the subscription is active or paused. Defaults to false.

          property_name: The internal name of the property to monitor for changes. Only applies when
              `eventType` is `propertyChange`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/webhooks/v3/{app_id}/subscriptions",
            body=maybe_transform(
                {
                    "event_type": event_type,
                    "active": active,
                    "object_type_id": object_type_id,
                    "property_name": property_name,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )

    def update(
        self,
        subscription_id: int,
        *,
        app_id: int,
        active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Update an existing event subscription by ID.

        Args:
          active: Determines if the subscription is active or paused.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/webhooks/v3/{app_id}/subscriptions/{subscription_id}",
            body=maybe_transform({"active": active}, webhook_update_params.WebhookUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )

    def list(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionListResponse:
        """
        Retrieve event subscriptions for the specified app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/webhooks/v3/{app_id}/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionListResponse,
        )

    def delete(
        self,
        subscription_id: int,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing event subscription by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/webhooks/v3/{app_id}/subscriptions/{subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def clear(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete the webhook settings for the specified app.

        Event subscriptions will not
        be deleted, but will be paused until another webhook is created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/webhooks/v3/{app_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def configure(
        self,
        app_id: int,
        *,
        target_url: str,
        throttling: ThrottlingSettingsParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsResponse:
        """
        Update webhook settings for the specified app.

        Args:
          target_url: A publicly available URL for HubSpot to call where event payloads will be
              delivered.

          throttling: Configuration details for webhook throttling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/webhooks/v3/{app_id}/settings",
            body=maybe_transform(
                {
                    "target_url": target_url,
                    "throttling": throttling,
                },
                webhook_configure_params.WebhookConfigureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsResponse,
        )

    def read(
        self,
        subscription_id: int,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Retrieve a specific event subscription by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/webhooks/v3/{app_id}/subscriptions/{subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )

    def update_batch(
        self,
        app_id: int,
        *,
        inputs: Iterable[SubscriptionBatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriptionResponse:
        """
        Batch create event subscriptions for the specified app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/webhooks/v3/{app_id}/subscriptions/batch/update",
            body=maybe_transform({"inputs": inputs}, webhook_update_batch_params.WebhookUpdateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriptionResponse,
        )


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)

    async def create(
        self,
        app_id: int,
        *,
        event_type: Literal[
            "contact.propertyChange",
            "company.propertyChange",
            "deal.propertyChange",
            "ticket.propertyChange",
            "product.propertyChange",
            "line_item.propertyChange",
            "contact.creation",
            "contact.deletion",
            "contact.privacyDeletion",
            "company.creation",
            "company.deletion",
            "deal.creation",
            "deal.deletion",
            "ticket.creation",
            "ticket.deletion",
            "product.creation",
            "product.deletion",
            "line_item.creation",
            "line_item.deletion",
            "conversation.creation",
            "conversation.deletion",
            "conversation.newMessage",
            "conversation.privacyDeletion",
            "conversation.propertyChange",
            "contact.merge",
            "company.merge",
            "deal.merge",
            "ticket.merge",
            "product.merge",
            "line_item.merge",
            "contact.restore",
            "company.restore",
            "deal.restore",
            "ticket.restore",
            "product.restore",
            "line_item.restore",
            "contact.associationChange",
            "company.associationChange",
            "deal.associationChange",
            "ticket.associationChange",
            "line_item.associationChange",
            "object.propertyChange",
            "object.creation",
            "object.deletion",
            "object.merge",
            "object.restore",
            "object.associationChange",
        ],
        active: bool | Omit = omit,
        object_type_id: str | Omit = omit,
        property_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Create new event subscription for the specified app.

        Args:
          event_type: Type of event to listen for. Can be one of `create`, `delete`,
              `deletedForPrivacy`, or `propertyChange`.

          active: Determines if the subscription is active or paused. Defaults to false.

          property_name: The internal name of the property to monitor for changes. Only applies when
              `eventType` is `propertyChange`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/webhooks/v3/{app_id}/subscriptions",
            body=await async_maybe_transform(
                {
                    "event_type": event_type,
                    "active": active,
                    "object_type_id": object_type_id,
                    "property_name": property_name,
                },
                webhook_create_params.WebhookCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )

    async def update(
        self,
        subscription_id: int,
        *,
        app_id: int,
        active: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Update an existing event subscription by ID.

        Args:
          active: Determines if the subscription is active or paused.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/webhooks/v3/{app_id}/subscriptions/{subscription_id}",
            body=await async_maybe_transform({"active": active}, webhook_update_params.WebhookUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )

    async def list(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionListResponse:
        """
        Retrieve event subscriptions for the specified app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/webhooks/v3/{app_id}/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionListResponse,
        )

    async def delete(
        self,
        subscription_id: int,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing event subscription by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/webhooks/v3/{app_id}/subscriptions/{subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def clear(
        self,
        app_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete the webhook settings for the specified app.

        Event subscriptions will not
        be deleted, but will be paused until another webhook is created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/webhooks/v3/{app_id}/settings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def configure(
        self,
        app_id: int,
        *,
        target_url: str,
        throttling: ThrottlingSettingsParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingsResponse:
        """
        Update webhook settings for the specified app.

        Args:
          target_url: A publicly available URL for HubSpot to call where event payloads will be
              delivered.

          throttling: Configuration details for webhook throttling.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/webhooks/v3/{app_id}/settings",
            body=await async_maybe_transform(
                {
                    "target_url": target_url,
                    "throttling": throttling,
                },
                webhook_configure_params.WebhookConfigureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingsResponse,
        )

    async def read(
        self,
        subscription_id: int,
        *,
        app_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionResponse:
        """
        Retrieve a specific event subscription by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/webhooks/v3/{app_id}/subscriptions/{subscription_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionResponse,
        )

    async def update_batch(
        self,
        app_id: int,
        *,
        inputs: Iterable[SubscriptionBatchUpdateRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponseSubscriptionResponse:
        """
        Batch create event subscriptions for the specified app.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/webhooks/v3/{app_id}/subscriptions/batch/update",
            body=await async_maybe_transform({"inputs": inputs}, webhook_update_batch_params.WebhookUpdateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponseSubscriptionResponse,
        )


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_raw_response_wrapper(
            webhooks.create,
        )
        self.update = to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = to_raw_response_wrapper(
            webhooks.delete,
        )
        self.clear = to_raw_response_wrapper(
            webhooks.clear,
        )
        self.configure = to_raw_response_wrapper(
            webhooks.configure,
        )
        self.read = to_raw_response_wrapper(
            webhooks.read,
        )
        self.update_batch = to_raw_response_wrapper(
            webhooks.update_batch,
        )


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_raw_response_wrapper(
            webhooks.create,
        )
        self.update = async_to_raw_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_raw_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            webhooks.delete,
        )
        self.clear = async_to_raw_response_wrapper(
            webhooks.clear,
        )
        self.configure = async_to_raw_response_wrapper(
            webhooks.configure,
        )
        self.read = async_to_raw_response_wrapper(
            webhooks.read,
        )
        self.update_batch = async_to_raw_response_wrapper(
            webhooks.update_batch,
        )


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = to_streamed_response_wrapper(
            webhooks.create,
        )
        self.update = to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.clear = to_streamed_response_wrapper(
            webhooks.clear,
        )
        self.configure = to_streamed_response_wrapper(
            webhooks.configure,
        )
        self.read = to_streamed_response_wrapper(
            webhooks.read,
        )
        self.update_batch = to_streamed_response_wrapper(
            webhooks.update_batch,
        )


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

        self.create = async_to_streamed_response_wrapper(
            webhooks.create,
        )
        self.update = async_to_streamed_response_wrapper(
            webhooks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            webhooks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhooks.delete,
        )
        self.clear = async_to_streamed_response_wrapper(
            webhooks.clear,
        )
        self.configure = async_to_streamed_response_wrapper(
            webhooks.configure,
        )
        self.read = async_to_streamed_response_wrapper(
            webhooks.read,
        )
        self.update_batch = async_to_streamed_response_wrapper(
            webhooks.update_batch,
        )
