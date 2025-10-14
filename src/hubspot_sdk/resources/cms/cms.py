# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .blogs.blogs import (
    BlogsResource,
    AsyncBlogsResource,
    BlogsResourceWithRawResponse,
    AsyncBlogsResourceWithRawResponse,
    BlogsResourceWithStreamingResponse,
    AsyncBlogsResourceWithStreamingResponse,
)
from .url_redirects import (
    URLRedirectsResource,
    AsyncURLRedirectsResource,
    URLRedirectsResourceWithRawResponse,
    AsyncURLRedirectsResourceWithRawResponse,
    URLRedirectsResourceWithStreamingResponse,
    AsyncURLRedirectsResourceWithStreamingResponse,
)

__all__ = ["CmsResource", "AsyncCmsResource"]


class CmsResource(SyncAPIResource):
    @cached_property
    def blogs(self) -> BlogsResource:
        return BlogsResource(self._client)

    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def url_redirects(self) -> URLRedirectsResource:
        return URLRedirectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CmsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CmsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CmsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CmsResourceWithStreamingResponse(self)


class AsyncCmsResource(AsyncAPIResource):
    @cached_property
    def blogs(self) -> AsyncBlogsResource:
        return AsyncBlogsResource(self._client)

    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def url_redirects(self) -> AsyncURLRedirectsResource:
        return AsyncURLRedirectsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCmsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCmsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCmsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCmsResourceWithStreamingResponse(self)


class CmsResourceWithRawResponse:
    def __init__(self, cms: CmsResource) -> None:
        self._cms = cms

    @cached_property
    def blogs(self) -> BlogsResourceWithRawResponse:
        return BlogsResourceWithRawResponse(self._cms.blogs)

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._cms.domains)

    @cached_property
    def url_redirects(self) -> URLRedirectsResourceWithRawResponse:
        return URLRedirectsResourceWithRawResponse(self._cms.url_redirects)


class AsyncCmsResourceWithRawResponse:
    def __init__(self, cms: AsyncCmsResource) -> None:
        self._cms = cms

    @cached_property
    def blogs(self) -> AsyncBlogsResourceWithRawResponse:
        return AsyncBlogsResourceWithRawResponse(self._cms.blogs)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._cms.domains)

    @cached_property
    def url_redirects(self) -> AsyncURLRedirectsResourceWithRawResponse:
        return AsyncURLRedirectsResourceWithRawResponse(self._cms.url_redirects)


class CmsResourceWithStreamingResponse:
    def __init__(self, cms: CmsResource) -> None:
        self._cms = cms

    @cached_property
    def blogs(self) -> BlogsResourceWithStreamingResponse:
        return BlogsResourceWithStreamingResponse(self._cms.blogs)

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._cms.domains)

    @cached_property
    def url_redirects(self) -> URLRedirectsResourceWithStreamingResponse:
        return URLRedirectsResourceWithStreamingResponse(self._cms.url_redirects)


class AsyncCmsResourceWithStreamingResponse:
    def __init__(self, cms: AsyncCmsResource) -> None:
        self._cms = cms

    @cached_property
    def blogs(self) -> AsyncBlogsResourceWithStreamingResponse:
        return AsyncBlogsResourceWithStreamingResponse(self._cms.blogs)

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._cms.domains)

    @cached_property
    def url_redirects(self) -> AsyncURLRedirectsResourceWithStreamingResponse:
        return AsyncURLRedirectsResourceWithStreamingResponse(self._cms.url_redirects)
