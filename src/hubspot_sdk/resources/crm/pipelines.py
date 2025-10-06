# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

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
from ...types.crm import pipeline_create_params, pipeline_update_params, pipeline_replace_params
from ..._base_client import make_request_options
from ...types.crm.pipeline import Pipeline
from ...types.crm.pipeline_stage import PipelineStage
from ...types.crm.pipeline_stage_input_param import PipelineStageInputParam
from ...types.crm.collection_response_pipeline_no_paging import CollectionResponsePipelineNoPaging
from ...types.crm.collection_response_public_audit_info_no_paging import CollectionResponsePublicAuditInfoNoPaging

__all__ = ["PipelinesResource", "AsyncPipelinesResource"]


class PipelinesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PipelinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PipelinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PipelinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return PipelinesResourceWithStreamingResponse(self)

    def create(
        self,
        object_type: str,
        *,
        display_order: int,
        label: str,
        stages: Iterable[PipelineStageInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Create a pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._post(
            f"/crm/v3/pipelines/{object_type}",
            body=maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "stages": stages,
                },
                pipeline_create_params.PipelineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    def update(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        archived: bool | Omit = omit,
        display_order: int | Omit = omit,
        label: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Update a pipeline stage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return self._patch(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            body=maybe_transform(
                {
                    "archived": archived,
                    "display_order": display_order,
                    "label": label,
                    "metadata": metadata,
                },
                pipeline_update_params.PipelineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
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
    ) -> CollectionResponsePipelineNoPaging:
        """
        Retrieve all pipelines

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return self._get(
            f"/crm/v3/pipelines/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePipelineNoPaging,
        )

    def delete(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a pipeline stage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_audit(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicAuditInfoNoPaging:
        """
        Return an audit of all changes to the pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._get(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/audit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAuditInfoNoPaging,
        )

    def read(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Return a pipeline stage by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return self._get(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    def replace(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        display_order: int,
        label: str,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Replace a pipeline stage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return self._put(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            body=maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "metadata": metadata,
                },
                pipeline_replace_params.PipelineReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )


class AsyncPipelinesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPipelinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPipelinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPipelinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncPipelinesResourceWithStreamingResponse(self)

    async def create(
        self,
        object_type: str,
        *,
        display_order: int,
        label: str,
        stages: Iterable[PipelineStageInputParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Create a pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._post(
            f"/crm/v3/pipelines/{object_type}",
            body=await async_maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "stages": stages,
                },
                pipeline_create_params.PipelineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    async def update(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        archived: bool | Omit = omit,
        display_order: int | Omit = omit,
        label: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Update a pipeline stage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return await self._patch(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            body=await async_maybe_transform(
                {
                    "archived": archived,
                    "display_order": display_order,
                    "label": label,
                    "metadata": metadata,
                },
                pipeline_update_params.PipelineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
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
    ) -> CollectionResponsePipelineNoPaging:
        """
        Retrieve all pipelines

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        return await self._get(
            f"/crm/v3/pipelines/{object_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePipelineNoPaging,
        )

    async def delete(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a pipeline stage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_audit(
        self,
        pipeline_id: str,
        *,
        object_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponsePublicAuditInfoNoPaging:
        """
        Return an audit of all changes to the pipeline

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._get(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/audit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionResponsePublicAuditInfoNoPaging,
        )

    async def read(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Return a pipeline stage by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return await self._get(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )

    async def replace(
        self,
        stage_id: str,
        *,
        object_type: str,
        pipeline_id: str,
        display_order: int,
        label: str,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineStage:
        """
        Replace a pipeline stage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not object_type:
            raise ValueError(f"Expected a non-empty value for `object_type` but received {object_type!r}")
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not stage_id:
            raise ValueError(f"Expected a non-empty value for `stage_id` but received {stage_id!r}")
        return await self._put(
            f"/crm/v3/pipelines/{object_type}/{pipeline_id}/stages/{stage_id}",
            body=await async_maybe_transform(
                {
                    "display_order": display_order,
                    "label": label,
                    "metadata": metadata,
                },
                pipeline_replace_params.PipelineReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineStage,
        )


class PipelinesResourceWithRawResponse:
    def __init__(self, pipelines: PipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = to_raw_response_wrapper(
            pipelines.create,
        )
        self.update = to_raw_response_wrapper(
            pipelines.update,
        )
        self.list = to_raw_response_wrapper(
            pipelines.list,
        )
        self.delete = to_raw_response_wrapper(
            pipelines.delete,
        )
        self.get_audit = to_raw_response_wrapper(
            pipelines.get_audit,
        )
        self.read = to_raw_response_wrapper(
            pipelines.read,
        )
        self.replace = to_raw_response_wrapper(
            pipelines.replace,
        )


class AsyncPipelinesResourceWithRawResponse:
    def __init__(self, pipelines: AsyncPipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = async_to_raw_response_wrapper(
            pipelines.create,
        )
        self.update = async_to_raw_response_wrapper(
            pipelines.update,
        )
        self.list = async_to_raw_response_wrapper(
            pipelines.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pipelines.delete,
        )
        self.get_audit = async_to_raw_response_wrapper(
            pipelines.get_audit,
        )
        self.read = async_to_raw_response_wrapper(
            pipelines.read,
        )
        self.replace = async_to_raw_response_wrapper(
            pipelines.replace,
        )


class PipelinesResourceWithStreamingResponse:
    def __init__(self, pipelines: PipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = to_streamed_response_wrapper(
            pipelines.create,
        )
        self.update = to_streamed_response_wrapper(
            pipelines.update,
        )
        self.list = to_streamed_response_wrapper(
            pipelines.list,
        )
        self.delete = to_streamed_response_wrapper(
            pipelines.delete,
        )
        self.get_audit = to_streamed_response_wrapper(
            pipelines.get_audit,
        )
        self.read = to_streamed_response_wrapper(
            pipelines.read,
        )
        self.replace = to_streamed_response_wrapper(
            pipelines.replace,
        )


class AsyncPipelinesResourceWithStreamingResponse:
    def __init__(self, pipelines: AsyncPipelinesResource) -> None:
        self._pipelines = pipelines

        self.create = async_to_streamed_response_wrapper(
            pipelines.create,
        )
        self.update = async_to_streamed_response_wrapper(
            pipelines.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pipelines.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pipelines.delete,
        )
        self.get_audit = async_to_streamed_response_wrapper(
            pipelines.get_audit,
        )
        self.read = async_to_streamed_response_wrapper(
            pipelines.read,
        )
        self.replace = async_to_streamed_response_wrapper(
            pipelines.replace,
        )
