# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.marketing import subscription_subscribe_params, subscription_unsubscribe_params
from ....types.marketing.subscriptions.public_subscription_status import PublicSubscriptionStatus
from ....types.marketing.subscriptions.subscription_definitions_response import SubscriptionDefinitionsResponse
from ....types.marketing.subscriptions.public_subscription_statuses_response import PublicSubscriptionStatusesResponse

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return SubscriptionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionDefinitionsResponse:
        """Get subscription definitions"""
        return self._get(
            "/communication-preferences/v3/definitions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDefinitionsResponse,
        )

    def get_email_status(
        self,
        email_address: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSubscriptionStatusesResponse:
        """
        Get subscription statuses for a contact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_address:
            raise ValueError(f"Expected a non-empty value for `email_address` but received {email_address!r}")
        return self._get(
            f"/communication-preferences/v3/status/email/{email_address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSubscriptionStatusesResponse,
        )

    def subscribe(
        self,
        *,
        email_address: str,
        subscription_id: str,
        legal_basis: Literal[
            "LEGITIMATE_INTEREST_PQL",
            "LEGITIMATE_INTEREST_CLIENT",
            "PERFORMANCE_OF_CONTRACT",
            "CONSENT_WITH_NOTICE",
            "NON_GDPR",
            "PROCESS_AND_STORE",
            "LEGITIMATE_INTEREST_OTHER",
        ]
        | Omit = omit,
        legal_basis_explanation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSubscriptionStatus:
        """
        Subscribe a contact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/communication-preferences/v3/subscribe",
            body=maybe_transform(
                {
                    "email_address": email_address,
                    "subscription_id": subscription_id,
                    "legal_basis": legal_basis,
                    "legal_basis_explanation": legal_basis_explanation,
                },
                subscription_subscribe_params.SubscriptionSubscribeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSubscriptionStatus,
        )

    def unsubscribe(
        self,
        *,
        email_address: str,
        subscription_id: str,
        legal_basis: Literal[
            "LEGITIMATE_INTEREST_PQL",
            "LEGITIMATE_INTEREST_CLIENT",
            "PERFORMANCE_OF_CONTRACT",
            "CONSENT_WITH_NOTICE",
            "NON_GDPR",
            "PROCESS_AND_STORE",
            "LEGITIMATE_INTEREST_OTHER",
        ]
        | Omit = omit,
        legal_basis_explanation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSubscriptionStatus:
        """
        Unsubscribe a contact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/communication-preferences/v3/unsubscribe",
            body=maybe_transform(
                {
                    "email_address": email_address,
                    "subscription_id": subscription_id,
                    "legal_basis": legal_basis,
                    "legal_basis_explanation": legal_basis_explanation,
                },
                subscription_unsubscribe_params.SubscriptionUnsubscribeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSubscriptionStatus,
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionDefinitionsResponse:
        """Get subscription definitions"""
        return await self._get(
            "/communication-preferences/v3/definitions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDefinitionsResponse,
        )

    async def get_email_status(
        self,
        email_address: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSubscriptionStatusesResponse:
        """
        Get subscription statuses for a contact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not email_address:
            raise ValueError(f"Expected a non-empty value for `email_address` but received {email_address!r}")
        return await self._get(
            f"/communication-preferences/v3/status/email/{email_address}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSubscriptionStatusesResponse,
        )

    async def subscribe(
        self,
        *,
        email_address: str,
        subscription_id: str,
        legal_basis: Literal[
            "LEGITIMATE_INTEREST_PQL",
            "LEGITIMATE_INTEREST_CLIENT",
            "PERFORMANCE_OF_CONTRACT",
            "CONSENT_WITH_NOTICE",
            "NON_GDPR",
            "PROCESS_AND_STORE",
            "LEGITIMATE_INTEREST_OTHER",
        ]
        | Omit = omit,
        legal_basis_explanation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSubscriptionStatus:
        """
        Subscribe a contact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/communication-preferences/v3/subscribe",
            body=await async_maybe_transform(
                {
                    "email_address": email_address,
                    "subscription_id": subscription_id,
                    "legal_basis": legal_basis,
                    "legal_basis_explanation": legal_basis_explanation,
                },
                subscription_subscribe_params.SubscriptionSubscribeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSubscriptionStatus,
        )

    async def unsubscribe(
        self,
        *,
        email_address: str,
        subscription_id: str,
        legal_basis: Literal[
            "LEGITIMATE_INTEREST_PQL",
            "LEGITIMATE_INTEREST_CLIENT",
            "PERFORMANCE_OF_CONTRACT",
            "CONSENT_WITH_NOTICE",
            "NON_GDPR",
            "PROCESS_AND_STORE",
            "LEGITIMATE_INTEREST_OTHER",
        ]
        | Omit = omit,
        legal_basis_explanation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublicSubscriptionStatus:
        """
        Unsubscribe a contact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/communication-preferences/v3/unsubscribe",
            body=await async_maybe_transform(
                {
                    "email_address": email_address,
                    "subscription_id": subscription_id,
                    "legal_basis": legal_basis,
                    "legal_basis_explanation": legal_basis_explanation,
                },
                subscription_unsubscribe_params.SubscriptionUnsubscribeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublicSubscriptionStatus,
        )


class SubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )
        self.get_email_status = to_raw_response_wrapper(
            subscriptions.get_email_status,
        )
        self.subscribe = to_raw_response_wrapper(
            subscriptions.subscribe,
        )
        self.unsubscribe = to_raw_response_wrapper(
            subscriptions.unsubscribe,
        )


class AsyncSubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.get_email_status = async_to_raw_response_wrapper(
            subscriptions.get_email_status,
        )
        self.subscribe = async_to_raw_response_wrapper(
            subscriptions.subscribe,
        )
        self.unsubscribe = async_to_raw_response_wrapper(
            subscriptions.unsubscribe,
        )


class SubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.get_email_status = to_streamed_response_wrapper(
            subscriptions.get_email_status,
        )
        self.subscribe = to_streamed_response_wrapper(
            subscriptions.subscribe,
        )
        self.unsubscribe = to_streamed_response_wrapper(
            subscriptions.unsubscribe,
        )


class AsyncSubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.get_email_status = async_to_streamed_response_wrapper(
            subscriptions.get_email_status,
        )
        self.subscribe = async_to_streamed_response_wrapper(
            subscriptions.subscribe,
        )
        self.unsubscribe = async_to_streamed_response_wrapper(
            subscriptions.unsubscribe,
        )
