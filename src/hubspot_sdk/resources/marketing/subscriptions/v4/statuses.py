# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from .....types.marketing.subscriptions.v4 import (
    status_get_params,
    status_set_params,
    status_get_batch_params,
    status_update_batch_params,
    status_unsubscribe_all_params,
    status_unsubscribe_all_batch_params,
    status_get_unsubscribe_all_status_params,
    status_get_unsubscribe_all_status_batch_params,
)
from .....types.marketing.subscriptions.public_status_request_param import PublicStatusRequestParam
from .....types.marketing.subscriptions.batch_response_public_status import BatchResponsePublicStatus
from .....types.marketing.subscriptions.action_response_with_results_public_status import (
    ActionResponseWithResultsPublicStatus,
)
from .....types.marketing.subscriptions.batch_response_public_status_bulk_response import (
    BatchResponsePublicStatusBulkResponse,
)
from .....types.marketing.subscriptions.action_response_with_results_public_wide_status import (
    ActionResponseWithResultsPublicWideStatus,
)
from .....types.marketing.subscriptions.batch_response_public_wide_status_bulk_response import (
    BatchResponsePublicWideStatusBulkResponse,
)
from .....types.marketing.subscriptions.batch_response_public_bulk_opt_out_from_all_response import (
    BatchResponsePublicBulkOptOutFromAllResponse,
)

__all__ = ["StatusesResource", "AsyncStatusesResource"]


class StatusesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StatusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return StatusesResourceWithStreamingResponse(self)

    def get(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        business_unit_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicStatus:
        """
        Get subscription preferences for a specific contact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return self._get(
            f"/communication-preferences/v4/statuses/{subscriber_id_string}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    status_get_params.StatusGetParams,
                ),
            ),
            cast_to=ActionResponseWithResultsPublicStatus,
        )

    def get_batch(
        self,
        *,
        channel: Literal["EMAIL"],
        inputs: SequenceNotStr[str],
        business_unit_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicStatusBulkResponse:
        """
        Batch retrieve subscription statuses

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/communication-preferences/v4/statuses/batch/read",
            body=maybe_transform({"inputs": inputs}, status_get_batch_params.StatusGetBatchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    status_get_batch_params.StatusGetBatchParams,
                ),
            ),
            cast_to=BatchResponsePublicStatusBulkResponse,
        )

    def get_unsubscribe_all_status(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        business_unit_id: int | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicWideStatus:
        """
        Retrieve a contact's unsubscribed status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return self._get(
            f"/communication-preferences/v4/statuses/{subscriber_id_string}/unsubscribe-all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                        "verbose": verbose,
                    },
                    status_get_unsubscribe_all_status_params.StatusGetUnsubscribeAllStatusParams,
                ),
            ),
            cast_to=ActionResponseWithResultsPublicWideStatus,
        )

    def get_unsubscribe_all_status_batch(
        self,
        *,
        channel: Literal["EMAIL"],
        inputs: SequenceNotStr[str],
        business_unit_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicWideStatusBulkResponse:
        """
        Batch retrieve contacts who have opted out of all communications

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/communication-preferences/v4/statuses/batch/unsubscribe-all/read",
            body=maybe_transform(
                {"inputs": inputs},
                status_get_unsubscribe_all_status_batch_params.StatusGetUnsubscribeAllStatusBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    status_get_unsubscribe_all_status_batch_params.StatusGetUnsubscribeAllStatusBatchParams,
                ),
            ),
            cast_to=BatchResponsePublicWideStatusBulkResponse,
        )

    def set(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        status_state: Literal["SUBSCRIBED", "UNSUBSCRIBED", "NOT_SPECIFIED"],
        subscription_id: int,
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
    ) -> ActionResponseWithResultsPublicStatus:
        """
        Update a contact's subscription status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return self._post(
            f"/communication-preferences/v4/statuses/{subscriber_id_string}",
            body=maybe_transform(
                {
                    "channel": channel,
                    "status_state": status_state,
                    "subscription_id": subscription_id,
                    "legal_basis": legal_basis,
                    "legal_basis_explanation": legal_basis_explanation,
                },
                status_set_params.StatusSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResponseWithResultsPublicStatus,
        )

    def unsubscribe_all(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        business_unit_id: int | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicStatus:
        """
        Unsubscribe a contact from all subscriptions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return self._post(
            f"/communication-preferences/v4/statuses/{subscriber_id_string}/unsubscribe-all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                        "verbose": verbose,
                    },
                    status_unsubscribe_all_params.StatusUnsubscribeAllParams,
                ),
            ),
            cast_to=ActionResponseWithResultsPublicStatus,
        )

    def unsubscribe_all_batch(
        self,
        *,
        channel: Literal["EMAIL"],
        inputs: SequenceNotStr[str],
        business_unit_id: int | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicBulkOptOutFromAllResponse:
        """
        Batch unsubscribe contacts from all subscriptions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/communication-preferences/v4/statuses/batch/unsubscribe-all",
            body=maybe_transform(
                {"inputs": inputs}, status_unsubscribe_all_batch_params.StatusUnsubscribeAllBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                        "verbose": verbose,
                    },
                    status_unsubscribe_all_batch_params.StatusUnsubscribeAllBatchParams,
                ),
            ),
            cast_to=BatchResponsePublicBulkOptOutFromAllResponse,
        )

    def update_batch(
        self,
        *,
        inputs: Iterable[PublicStatusRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicStatus:
        """
        Batch update subscription status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/communication-preferences/v4/statuses/batch/write",
            body=maybe_transform({"inputs": inputs}, status_update_batch_params.StatusUpdateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicStatus,
        )


class AsyncStatusesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatusesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncStatusesResourceWithStreamingResponse(self)

    async def get(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        business_unit_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicStatus:
        """
        Get subscription preferences for a specific contact

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return await self._get(
            f"/communication-preferences/v4/statuses/{subscriber_id_string}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    status_get_params.StatusGetParams,
                ),
            ),
            cast_to=ActionResponseWithResultsPublicStatus,
        )

    async def get_batch(
        self,
        *,
        channel: Literal["EMAIL"],
        inputs: SequenceNotStr[str],
        business_unit_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicStatusBulkResponse:
        """
        Batch retrieve subscription statuses

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/communication-preferences/v4/statuses/batch/read",
            body=await async_maybe_transform({"inputs": inputs}, status_get_batch_params.StatusGetBatchParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    status_get_batch_params.StatusGetBatchParams,
                ),
            ),
            cast_to=BatchResponsePublicStatusBulkResponse,
        )

    async def get_unsubscribe_all_status(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        business_unit_id: int | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicWideStatus:
        """
        Retrieve a contact's unsubscribed status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return await self._get(
            f"/communication-preferences/v4/statuses/{subscriber_id_string}/unsubscribe-all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                        "verbose": verbose,
                    },
                    status_get_unsubscribe_all_status_params.StatusGetUnsubscribeAllStatusParams,
                ),
            ),
            cast_to=ActionResponseWithResultsPublicWideStatus,
        )

    async def get_unsubscribe_all_status_batch(
        self,
        *,
        channel: Literal["EMAIL"],
        inputs: SequenceNotStr[str],
        business_unit_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicWideStatusBulkResponse:
        """
        Batch retrieve contacts who have opted out of all communications

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/communication-preferences/v4/statuses/batch/unsubscribe-all/read",
            body=await async_maybe_transform(
                {"inputs": inputs},
                status_get_unsubscribe_all_status_batch_params.StatusGetUnsubscribeAllStatusBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                    },
                    status_get_unsubscribe_all_status_batch_params.StatusGetUnsubscribeAllStatusBatchParams,
                ),
            ),
            cast_to=BatchResponsePublicWideStatusBulkResponse,
        )

    async def set(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        status_state: Literal["SUBSCRIBED", "UNSUBSCRIBED", "NOT_SPECIFIED"],
        subscription_id: int,
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
    ) -> ActionResponseWithResultsPublicStatus:
        """
        Update a contact's subscription status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return await self._post(
            f"/communication-preferences/v4/statuses/{subscriber_id_string}",
            body=await async_maybe_transform(
                {
                    "channel": channel,
                    "status_state": status_state,
                    "subscription_id": subscription_id,
                    "legal_basis": legal_basis,
                    "legal_basis_explanation": legal_basis_explanation,
                },
                status_set_params.StatusSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionResponseWithResultsPublicStatus,
        )

    async def unsubscribe_all(
        self,
        subscriber_id_string: str,
        *,
        channel: Literal["EMAIL"],
        business_unit_id: int | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ActionResponseWithResultsPublicStatus:
        """
        Unsubscribe a contact from all subscriptions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not subscriber_id_string:
            raise ValueError(
                f"Expected a non-empty value for `subscriber_id_string` but received {subscriber_id_string!r}"
            )
        return await self._post(
            f"/communication-preferences/v4/statuses/{subscriber_id_string}/unsubscribe-all",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                        "verbose": verbose,
                    },
                    status_unsubscribe_all_params.StatusUnsubscribeAllParams,
                ),
            ),
            cast_to=ActionResponseWithResultsPublicStatus,
        )

    async def unsubscribe_all_batch(
        self,
        *,
        channel: Literal["EMAIL"],
        inputs: SequenceNotStr[str],
        business_unit_id: int | Omit = omit,
        verbose: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicBulkOptOutFromAllResponse:
        """
        Batch unsubscribe contacts from all subscriptions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/communication-preferences/v4/statuses/batch/unsubscribe-all",
            body=await async_maybe_transform(
                {"inputs": inputs}, status_unsubscribe_all_batch_params.StatusUnsubscribeAllBatchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "business_unit_id": business_unit_id,
                        "verbose": verbose,
                    },
                    status_unsubscribe_all_batch_params.StatusUnsubscribeAllBatchParams,
                ),
            ),
            cast_to=BatchResponsePublicBulkOptOutFromAllResponse,
        )

    async def update_batch(
        self,
        *,
        inputs: Iterable[PublicStatusRequestParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchResponsePublicStatus:
        """
        Batch update subscription status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/communication-preferences/v4/statuses/batch/write",
            body=await async_maybe_transform({"inputs": inputs}, status_update_batch_params.StatusUpdateBatchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchResponsePublicStatus,
        )


class StatusesResourceWithRawResponse:
    def __init__(self, statuses: StatusesResource) -> None:
        self._statuses = statuses

        self.get = to_raw_response_wrapper(
            statuses.get,
        )
        self.get_batch = to_raw_response_wrapper(
            statuses.get_batch,
        )
        self.get_unsubscribe_all_status = to_raw_response_wrapper(
            statuses.get_unsubscribe_all_status,
        )
        self.get_unsubscribe_all_status_batch = to_raw_response_wrapper(
            statuses.get_unsubscribe_all_status_batch,
        )
        self.set = to_raw_response_wrapper(
            statuses.set,
        )
        self.unsubscribe_all = to_raw_response_wrapper(
            statuses.unsubscribe_all,
        )
        self.unsubscribe_all_batch = to_raw_response_wrapper(
            statuses.unsubscribe_all_batch,
        )
        self.update_batch = to_raw_response_wrapper(
            statuses.update_batch,
        )


class AsyncStatusesResourceWithRawResponse:
    def __init__(self, statuses: AsyncStatusesResource) -> None:
        self._statuses = statuses

        self.get = async_to_raw_response_wrapper(
            statuses.get,
        )
        self.get_batch = async_to_raw_response_wrapper(
            statuses.get_batch,
        )
        self.get_unsubscribe_all_status = async_to_raw_response_wrapper(
            statuses.get_unsubscribe_all_status,
        )
        self.get_unsubscribe_all_status_batch = async_to_raw_response_wrapper(
            statuses.get_unsubscribe_all_status_batch,
        )
        self.set = async_to_raw_response_wrapper(
            statuses.set,
        )
        self.unsubscribe_all = async_to_raw_response_wrapper(
            statuses.unsubscribe_all,
        )
        self.unsubscribe_all_batch = async_to_raw_response_wrapper(
            statuses.unsubscribe_all_batch,
        )
        self.update_batch = async_to_raw_response_wrapper(
            statuses.update_batch,
        )


class StatusesResourceWithStreamingResponse:
    def __init__(self, statuses: StatusesResource) -> None:
        self._statuses = statuses

        self.get = to_streamed_response_wrapper(
            statuses.get,
        )
        self.get_batch = to_streamed_response_wrapper(
            statuses.get_batch,
        )
        self.get_unsubscribe_all_status = to_streamed_response_wrapper(
            statuses.get_unsubscribe_all_status,
        )
        self.get_unsubscribe_all_status_batch = to_streamed_response_wrapper(
            statuses.get_unsubscribe_all_status_batch,
        )
        self.set = to_streamed_response_wrapper(
            statuses.set,
        )
        self.unsubscribe_all = to_streamed_response_wrapper(
            statuses.unsubscribe_all,
        )
        self.unsubscribe_all_batch = to_streamed_response_wrapper(
            statuses.unsubscribe_all_batch,
        )
        self.update_batch = to_streamed_response_wrapper(
            statuses.update_batch,
        )


class AsyncStatusesResourceWithStreamingResponse:
    def __init__(self, statuses: AsyncStatusesResource) -> None:
        self._statuses = statuses

        self.get = async_to_streamed_response_wrapper(
            statuses.get,
        )
        self.get_batch = async_to_streamed_response_wrapper(
            statuses.get_batch,
        )
        self.get_unsubscribe_all_status = async_to_streamed_response_wrapper(
            statuses.get_unsubscribe_all_status,
        )
        self.get_unsubscribe_all_status_batch = async_to_streamed_response_wrapper(
            statuses.get_unsubscribe_all_status_batch,
        )
        self.set = async_to_streamed_response_wrapper(
            statuses.set,
        )
        self.unsubscribe_all = async_to_streamed_response_wrapper(
            statuses.unsubscribe_all,
        )
        self.unsubscribe_all_batch = async_to_streamed_response_wrapper(
            statuses.unsubscribe_all_batch,
        )
        self.update_batch = async_to_streamed_response_wrapper(
            statuses.update_batch,
        )
