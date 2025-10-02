# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .pipelines import (
    PipelinesResource,
    AsyncPipelinesResource,
    PipelinesResourceWithRawResponse,
    AsyncPipelinesResourceWithRawResponse,
    PipelinesResourceWithStreamingResponse,
    AsyncPipelinesResourceWithStreamingResponse,
)
from .properties import (
    PropertiesResource,
    AsyncPropertiesResource,
    PropertiesResourceWithRawResponse,
    AsyncPropertiesResourceWithRawResponse,
    PropertiesResourceWithStreamingResponse,
    AsyncPropertiesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .object_schemas import (
    ObjectSchemasResource,
    AsyncObjectSchemasResource,
    ObjectSchemasResourceWithRawResponse,
    AsyncObjectSchemasResourceWithRawResponse,
    ObjectSchemasResourceWithStreamingResponse,
    AsyncObjectSchemasResourceWithStreamingResponse,
)
from .objects.objects import (
    ObjectsResource,
    AsyncObjectsResource,
    ObjectsResourceWithRawResponse,
    AsyncObjectsResourceWithRawResponse,
    ObjectsResourceWithStreamingResponse,
    AsyncObjectsResourceWithStreamingResponse,
)
from .associations.associations import (
    AssociationsResource,
    AsyncAssociationsResource,
    AssociationsResourceWithRawResponse,
    AsyncAssociationsResourceWithRawResponse,
    AssociationsResourceWithStreamingResponse,
    AsyncAssociationsResourceWithStreamingResponse,
)

__all__ = ["CRMResource", "AsyncCRMResource"]


class CRMResource(SyncAPIResource):
    @cached_property
    def associations(self) -> AssociationsResource:
        return AssociationsResource(self._client)

    @cached_property
    def object_schemas(self) -> ObjectSchemasResource:
        return ObjectSchemasResource(self._client)

    @cached_property
    def objects(self) -> ObjectsResource:
        return ObjectsResource(self._client)

    @cached_property
    def pipelines(self) -> PipelinesResource:
        return PipelinesResource(self._client)

    @cached_property
    def properties(self) -> PropertiesResource:
        return PropertiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CRMResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CRMResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CRMResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return CRMResourceWithStreamingResponse(self)


class AsyncCRMResource(AsyncAPIResource):
    @cached_property
    def associations(self) -> AsyncAssociationsResource:
        return AsyncAssociationsResource(self._client)

    @cached_property
    def object_schemas(self) -> AsyncObjectSchemasResource:
        return AsyncObjectSchemasResource(self._client)

    @cached_property
    def objects(self) -> AsyncObjectsResource:
        return AsyncObjectsResource(self._client)

    @cached_property
    def pipelines(self) -> AsyncPipelinesResource:
        return AsyncPipelinesResource(self._client)

    @cached_property
    def properties(self) -> AsyncPropertiesResource:
        return AsyncPropertiesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCRMResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCRMResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCRMResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncCRMResourceWithStreamingResponse(self)


class CRMResourceWithRawResponse:
    def __init__(self, crm: CRMResource) -> None:
        self._crm = crm

    @cached_property
    def associations(self) -> AssociationsResourceWithRawResponse:
        return AssociationsResourceWithRawResponse(self._crm.associations)

    @cached_property
    def object_schemas(self) -> ObjectSchemasResourceWithRawResponse:
        return ObjectSchemasResourceWithRawResponse(self._crm.object_schemas)

    @cached_property
    def objects(self) -> ObjectsResourceWithRawResponse:
        return ObjectsResourceWithRawResponse(self._crm.objects)

    @cached_property
    def pipelines(self) -> PipelinesResourceWithRawResponse:
        return PipelinesResourceWithRawResponse(self._crm.pipelines)

    @cached_property
    def properties(self) -> PropertiesResourceWithRawResponse:
        return PropertiesResourceWithRawResponse(self._crm.properties)


class AsyncCRMResourceWithRawResponse:
    def __init__(self, crm: AsyncCRMResource) -> None:
        self._crm = crm

    @cached_property
    def associations(self) -> AsyncAssociationsResourceWithRawResponse:
        return AsyncAssociationsResourceWithRawResponse(self._crm.associations)

    @cached_property
    def object_schemas(self) -> AsyncObjectSchemasResourceWithRawResponse:
        return AsyncObjectSchemasResourceWithRawResponse(self._crm.object_schemas)

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithRawResponse:
        return AsyncObjectsResourceWithRawResponse(self._crm.objects)

    @cached_property
    def pipelines(self) -> AsyncPipelinesResourceWithRawResponse:
        return AsyncPipelinesResourceWithRawResponse(self._crm.pipelines)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithRawResponse:
        return AsyncPropertiesResourceWithRawResponse(self._crm.properties)


class CRMResourceWithStreamingResponse:
    def __init__(self, crm: CRMResource) -> None:
        self._crm = crm

    @cached_property
    def associations(self) -> AssociationsResourceWithStreamingResponse:
        return AssociationsResourceWithStreamingResponse(self._crm.associations)

    @cached_property
    def object_schemas(self) -> ObjectSchemasResourceWithStreamingResponse:
        return ObjectSchemasResourceWithStreamingResponse(self._crm.object_schemas)

    @cached_property
    def objects(self) -> ObjectsResourceWithStreamingResponse:
        return ObjectsResourceWithStreamingResponse(self._crm.objects)

    @cached_property
    def pipelines(self) -> PipelinesResourceWithStreamingResponse:
        return PipelinesResourceWithStreamingResponse(self._crm.pipelines)

    @cached_property
    def properties(self) -> PropertiesResourceWithStreamingResponse:
        return PropertiesResourceWithStreamingResponse(self._crm.properties)


class AsyncCRMResourceWithStreamingResponse:
    def __init__(self, crm: AsyncCRMResource) -> None:
        self._crm = crm

    @cached_property
    def associations(self) -> AsyncAssociationsResourceWithStreamingResponse:
        return AsyncAssociationsResourceWithStreamingResponse(self._crm.associations)

    @cached_property
    def object_schemas(self) -> AsyncObjectSchemasResourceWithStreamingResponse:
        return AsyncObjectSchemasResourceWithStreamingResponse(self._crm.object_schemas)

    @cached_property
    def objects(self) -> AsyncObjectsResourceWithStreamingResponse:
        return AsyncObjectsResourceWithStreamingResponse(self._crm.objects)

    @cached_property
    def pipelines(self) -> AsyncPipelinesResourceWithStreamingResponse:
        return AsyncPipelinesResourceWithStreamingResponse(self._crm.pipelines)

    @cached_property
    def properties(self) -> AsyncPropertiesResourceWithStreamingResponse:
        return AsyncPropertiesResourceWithStreamingResponse(self._crm.properties)
