# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .forms import (
    FormsResource,
    AsyncFormsResource,
    FormsResourceWithRawResponse,
    AsyncFormsResourceWithRawResponse,
    FormsResourceWithStreamingResponse,
    AsyncFormsResourceWithStreamingResponse,
)
from .emails import (
    EmailsResource,
    AsyncEmailsResource,
    EmailsResourceWithRawResponse,
    AsyncEmailsResourceWithRawResponse,
    EmailsResourceWithStreamingResponse,
    AsyncEmailsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .subscriptions.subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)

__all__ = ["MarketingResource", "AsyncMarketingResource"]


class MarketingResource(SyncAPIResource):
    @cached_property
    def emails(self) -> EmailsResource:
        return EmailsResource(self._client)

    @cached_property
    def forms(self) -> FormsResource:
        return FormsResource(self._client)

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        return SubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MarketingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MarketingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#with_streaming_response
        """
        return MarketingResourceWithStreamingResponse(self)


class AsyncMarketingResource(AsyncAPIResource):
    @cached_property
    def emails(self) -> AsyncEmailsResource:
        return AsyncEmailsResource(self._client)

    @cached_property
    def forms(self) -> AsyncFormsResource:
        return AsyncFormsResource(self._client)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMarketingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/alzheltkovskiy-hubspot/hubspot-sdk-python#with_streaming_response
        """
        return AsyncMarketingResourceWithStreamingResponse(self)


class MarketingResourceWithRawResponse:
    def __init__(self, marketing: MarketingResource) -> None:
        self._marketing = marketing

    @cached_property
    def emails(self) -> EmailsResourceWithRawResponse:
        return EmailsResourceWithRawResponse(self._marketing.emails)

    @cached_property
    def forms(self) -> FormsResourceWithRawResponse:
        return FormsResourceWithRawResponse(self._marketing.forms)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self._marketing.subscriptions)


class AsyncMarketingResourceWithRawResponse:
    def __init__(self, marketing: AsyncMarketingResource) -> None:
        self._marketing = marketing

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithRawResponse:
        return AsyncEmailsResourceWithRawResponse(self._marketing.emails)

    @cached_property
    def forms(self) -> AsyncFormsResourceWithRawResponse:
        return AsyncFormsResourceWithRawResponse(self._marketing.forms)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self._marketing.subscriptions)


class MarketingResourceWithStreamingResponse:
    def __init__(self, marketing: MarketingResource) -> None:
        self._marketing = marketing

    @cached_property
    def emails(self) -> EmailsResourceWithStreamingResponse:
        return EmailsResourceWithStreamingResponse(self._marketing.emails)

    @cached_property
    def forms(self) -> FormsResourceWithStreamingResponse:
        return FormsResourceWithStreamingResponse(self._marketing.forms)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self._marketing.subscriptions)


class AsyncMarketingResourceWithStreamingResponse:
    def __init__(self, marketing: AsyncMarketingResource) -> None:
        self._marketing = marketing

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithStreamingResponse:
        return AsyncEmailsResourceWithStreamingResponse(self._marketing.emails)

    @cached_property
    def forms(self) -> AsyncFormsResourceWithStreamingResponse:
        return AsyncFormsResourceWithStreamingResponse(self._marketing.forms)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self._marketing.subscriptions)
