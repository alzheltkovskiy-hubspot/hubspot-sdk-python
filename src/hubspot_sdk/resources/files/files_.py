# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, Iterable, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NoneType,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.file import File
from ...types.files import (
    file_get_params,
    file_search_params,
    file_update_params,
    file_upload_params,
    file_replace_params,
    file_get_by_path_params,
    file_get_signed_url_params,
    file_import_from_url_async_params,
)
from ..._base_client import make_request_options
from ...types.file_stat import FileStat
from ...types.signed_url import SignedURL
from ...types.file_action_response import FileActionResponse
from ...types.collection_response_file import CollectionResponseFile
from ...types.import_from_url_task_locator import ImportFromURLTaskLocator

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def update(
        self,
        file_id: str,
        *,
        access: Literal[
            "PUBLIC_INDEXABLE",
            "PUBLIC_NOT_INDEXABLE",
            "HIDDEN_INDEXABLE",
            "HIDDEN_NOT_INDEXABLE",
            "HIDDEN_PRIVATE",
            "PRIVATE",
            "HIDDEN_SENSITIVE",
            "SENSITIVE",
        ]
        | Omit = omit,
        clear_expires: bool | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        is_usable_in_content: bool | Omit = omit,
        name: str | Omit = omit,
        parent_folder_id: str | Omit = omit,
        parent_folder_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Update file properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._patch(
            f"/files/v3/files/{file_id}",
            body=maybe_transform(
                {
                    "access": access,
                    "clear_expires": clear_expires,
                    "expires_at": expires_at,
                    "is_usable_in_content": is_usable_in_content,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "parent_folder_path": parent_folder_path,
                },
                file_update_params.FileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    def delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete file by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/files/v3/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def gdpr_delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        GDPR-delete file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/files/v3/files/{file_id}/gdpr-delete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        file_id: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Retrieve file by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/files/v3/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"properties": properties}, file_get_params.FileGetParams),
            ),
            cast_to=File,
        )

    def get_by_path(
        self,
        path: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileStat:
        """
        Retrieve file by path

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return self._get(
            f"/files/v3/files/stat/{path}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"properties": properties}, file_get_by_path_params.FileGetByPathParams),
            ),
            cast_to=FileStat,
        )

    def get_import_from_url_async_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileActionResponse:
        """
        Check import status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            f"/files/v3/files/import-from-url/async/tasks/{task_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileActionResponse,
        )

    def get_import_task_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileActionResponse:
        """
        Check import status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            f"/files/v3/files/import-from-url/async/tasks/{task_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileActionResponse,
        )

    def get_signed_url(
        self,
        file_id: str,
        *,
        expiration_seconds: int | Omit = omit,
        size: Literal["thumb", "icon", "medium", "preview"] | Omit = omit,
        upscale: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SignedURL:
        """
        Get signed URL to access private file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/files/v3/files/{file_id}/signed-url",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expiration_seconds": expiration_seconds,
                        "size": size,
                        "upscale": upscale,
                    },
                    file_get_signed_url_params.FileGetSignedURLParams,
                ),
            ),
            cast_to=SignedURL,
        )

    def import_from_url_async(
        self,
        *,
        access: Literal[
            "PUBLIC_INDEXABLE",
            "PUBLIC_NOT_INDEXABLE",
            "HIDDEN_INDEXABLE",
            "HIDDEN_NOT_INDEXABLE",
            "HIDDEN_PRIVATE",
            "PRIVATE",
            "HIDDEN_SENSITIVE",
            "SENSITIVE",
        ],
        url: str,
        duplicate_validation_scope: Literal["ENTIRE_PORTAL", "EXACT_FOLDER"] | Omit = omit,
        duplicate_validation_strategy: Literal["NONE", "REJECT", "RETURN_EXISTING"] | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        folder_id: str | Omit = omit,
        folder_path: str | Omit = omit,
        name: str | Omit = omit,
        overwrite: bool | Omit = omit,
        ttl: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportFromURLTaskLocator:
        """
        Import file from URL

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/files/v3/files/import-from-url/async",
            body=maybe_transform(
                {
                    "access": access,
                    "url": url,
                    "duplicate_validation_scope": duplicate_validation_scope,
                    "duplicate_validation_strategy": duplicate_validation_strategy,
                    "expires_at": expires_at,
                    "folder_id": folder_id,
                    "folder_path": folder_path,
                    "name": name,
                    "overwrite": overwrite,
                    "ttl": ttl,
                },
                file_import_from_url_async_params.FileImportFromURLAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportFromURLTaskLocator,
        )

    def replace(
        self,
        file_id: str,
        *,
        charset_hunch: str | Omit = omit,
        file: FileTypes | Omit = omit,
        options: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Replace file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        body = deepcopy_minimal(
            {
                "charset_hunch": charset_hunch,
                "file": file,
                "options": options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._put(
            f"/files/v3/files/{file_id}",
            body=maybe_transform(body, file_replace_params.FileReplaceParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    def search(
        self,
        *,
        after: str | Omit = omit,
        allows_anonymous_access: bool | Omit = omit,
        before: str | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        encoding: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        expires_at_gte: Union[str, datetime] | Omit = omit,
        expires_at_lte: Union[str, datetime] | Omit = omit,
        extension: str | Omit = omit,
        file_md5: str | Omit = omit,
        height: int | Omit = omit,
        height_gte: int | Omit = omit,
        height_lte: int | Omit = omit,
        id_gte: int | Omit = omit,
        id_lte: int | Omit = omit,
        ids: Iterable[int] | Omit = omit,
        is_usable_in_content: bool | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        parent_folder_ids: Iterable[int] | Omit = omit,
        path: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        size: int | Omit = omit,
        size_gte: int | Omit = omit,
        size_lte: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        type: str | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_at_gte: Union[str, datetime] | Omit = omit,
        updated_at_lte: Union[str, datetime] | Omit = omit,
        url: str | Omit = omit,
        width: int | Omit = omit,
        width_gte: int | Omit = omit,
        width_lte: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseFile:
        """
        Search files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/files/v3/files/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "allows_anonymous_access": allows_anonymous_access,
                        "before": before,
                        "created_at": created_at,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "encoding": encoding,
                        "expires_at": expires_at,
                        "expires_at_gte": expires_at_gte,
                        "expires_at_lte": expires_at_lte,
                        "extension": extension,
                        "file_md5": file_md5,
                        "height": height,
                        "height_gte": height_gte,
                        "height_lte": height_lte,
                        "id_gte": id_gte,
                        "id_lte": id_lte,
                        "ids": ids,
                        "is_usable_in_content": is_usable_in_content,
                        "limit": limit,
                        "name": name,
                        "parent_folder_ids": parent_folder_ids,
                        "path": path,
                        "properties": properties,
                        "size": size,
                        "size_gte": size_gte,
                        "size_lte": size_lte,
                        "sort": sort,
                        "type": type,
                        "updated_at": updated_at,
                        "updated_at_gte": updated_at_gte,
                        "updated_at_lte": updated_at_lte,
                        "url": url,
                        "width": width,
                        "width_gte": width_gte,
                        "width_lte": width_lte,
                    },
                    file_search_params.FileSearchParams,
                ),
            ),
            cast_to=CollectionResponseFile,
        )

    def upload(
        self,
        *,
        charset_hunch: str | Omit = omit,
        file: FileTypes | Omit = omit,
        file_name: str | Omit = omit,
        folder_id: str | Omit = omit,
        folder_path: str | Omit = omit,
        options: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Upload file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "charset_hunch": charset_hunch,
                "file": file,
                "file_name": file_name,
                "folder_id": folder_id,
                "folder_path": folder_path,
                "options": options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/files/v3/files",
            body=maybe_transform(body, file_upload_params.FileUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/hubspot-sdk-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def update(
        self,
        file_id: str,
        *,
        access: Literal[
            "PUBLIC_INDEXABLE",
            "PUBLIC_NOT_INDEXABLE",
            "HIDDEN_INDEXABLE",
            "HIDDEN_NOT_INDEXABLE",
            "HIDDEN_PRIVATE",
            "PRIVATE",
            "HIDDEN_SENSITIVE",
            "SENSITIVE",
        ]
        | Omit = omit,
        clear_expires: bool | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        is_usable_in_content: bool | Omit = omit,
        name: str | Omit = omit,
        parent_folder_id: str | Omit = omit,
        parent_folder_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Update file properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._patch(
            f"/files/v3/files/{file_id}",
            body=await async_maybe_transform(
                {
                    "access": access,
                    "clear_expires": clear_expires,
                    "expires_at": expires_at,
                    "is_usable_in_content": is_usable_in_content,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "parent_folder_path": parent_folder_path,
                },
                file_update_params.FileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    async def delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete file by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/files/v3/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def gdpr_delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        GDPR-delete file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/files/v3/files/{file_id}/gdpr-delete",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        file_id: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Retrieve file by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/files/v3/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"properties": properties}, file_get_params.FileGetParams),
            ),
            cast_to=File,
        )

    async def get_by_path(
        self,
        path: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileStat:
        """
        Retrieve file by path

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path:
            raise ValueError(f"Expected a non-empty value for `path` but received {path!r}")
        return await self._get(
            f"/files/v3/files/stat/{path}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"properties": properties}, file_get_by_path_params.FileGetByPathParams
                ),
            ),
            cast_to=FileStat,
        )

    async def get_import_from_url_async_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileActionResponse:
        """
        Check import status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            f"/files/v3/files/import-from-url/async/tasks/{task_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileActionResponse,
        )

    async def get_import_task_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileActionResponse:
        """
        Check import status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            f"/files/v3/files/import-from-url/async/tasks/{task_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileActionResponse,
        )

    async def get_signed_url(
        self,
        file_id: str,
        *,
        expiration_seconds: int | Omit = omit,
        size: Literal["thumb", "icon", "medium", "preview"] | Omit = omit,
        upscale: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SignedURL:
        """
        Get signed URL to access private file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/files/v3/files/{file_id}/signed-url",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expiration_seconds": expiration_seconds,
                        "size": size,
                        "upscale": upscale,
                    },
                    file_get_signed_url_params.FileGetSignedURLParams,
                ),
            ),
            cast_to=SignedURL,
        )

    async def import_from_url_async(
        self,
        *,
        access: Literal[
            "PUBLIC_INDEXABLE",
            "PUBLIC_NOT_INDEXABLE",
            "HIDDEN_INDEXABLE",
            "HIDDEN_NOT_INDEXABLE",
            "HIDDEN_PRIVATE",
            "PRIVATE",
            "HIDDEN_SENSITIVE",
            "SENSITIVE",
        ],
        url: str,
        duplicate_validation_scope: Literal["ENTIRE_PORTAL", "EXACT_FOLDER"] | Omit = omit,
        duplicate_validation_strategy: Literal["NONE", "REJECT", "RETURN_EXISTING"] | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        folder_id: str | Omit = omit,
        folder_path: str | Omit = omit,
        name: str | Omit = omit,
        overwrite: bool | Omit = omit,
        ttl: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImportFromURLTaskLocator:
        """
        Import file from URL

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/files/v3/files/import-from-url/async",
            body=await async_maybe_transform(
                {
                    "access": access,
                    "url": url,
                    "duplicate_validation_scope": duplicate_validation_scope,
                    "duplicate_validation_strategy": duplicate_validation_strategy,
                    "expires_at": expires_at,
                    "folder_id": folder_id,
                    "folder_path": folder_path,
                    "name": name,
                    "overwrite": overwrite,
                    "ttl": ttl,
                },
                file_import_from_url_async_params.FileImportFromURLAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImportFromURLTaskLocator,
        )

    async def replace(
        self,
        file_id: str,
        *,
        charset_hunch: str | Omit = omit,
        file: FileTypes | Omit = omit,
        options: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Replace file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        body = deepcopy_minimal(
            {
                "charset_hunch": charset_hunch,
                "file": file,
                "options": options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._put(
            f"/files/v3/files/{file_id}",
            body=await async_maybe_transform(body, file_replace_params.FileReplaceParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    async def search(
        self,
        *,
        after: str | Omit = omit,
        allows_anonymous_access: bool | Omit = omit,
        before: str | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        created_at_gte: Union[str, datetime] | Omit = omit,
        created_at_lte: Union[str, datetime] | Omit = omit,
        encoding: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        expires_at_gte: Union[str, datetime] | Omit = omit,
        expires_at_lte: Union[str, datetime] | Omit = omit,
        extension: str | Omit = omit,
        file_md5: str | Omit = omit,
        height: int | Omit = omit,
        height_gte: int | Omit = omit,
        height_lte: int | Omit = omit,
        id_gte: int | Omit = omit,
        id_lte: int | Omit = omit,
        ids: Iterable[int] | Omit = omit,
        is_usable_in_content: bool | Omit = omit,
        limit: int | Omit = omit,
        name: str | Omit = omit,
        parent_folder_ids: Iterable[int] | Omit = omit,
        path: str | Omit = omit,
        properties: SequenceNotStr[str] | Omit = omit,
        size: int | Omit = omit,
        size_gte: int | Omit = omit,
        size_lte: int | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        type: str | Omit = omit,
        updated_at: Union[str, datetime] | Omit = omit,
        updated_at_gte: Union[str, datetime] | Omit = omit,
        updated_at_lte: Union[str, datetime] | Omit = omit,
        url: str | Omit = omit,
        width: int | Omit = omit,
        width_gte: int | Omit = omit,
        width_lte: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionResponseFile:
        """
        Search files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/files/v3/files/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "allows_anonymous_access": allows_anonymous_access,
                        "before": before,
                        "created_at": created_at,
                        "created_at_gte": created_at_gte,
                        "created_at_lte": created_at_lte,
                        "encoding": encoding,
                        "expires_at": expires_at,
                        "expires_at_gte": expires_at_gte,
                        "expires_at_lte": expires_at_lte,
                        "extension": extension,
                        "file_md5": file_md5,
                        "height": height,
                        "height_gte": height_gte,
                        "height_lte": height_lte,
                        "id_gte": id_gte,
                        "id_lte": id_lte,
                        "ids": ids,
                        "is_usable_in_content": is_usable_in_content,
                        "limit": limit,
                        "name": name,
                        "parent_folder_ids": parent_folder_ids,
                        "path": path,
                        "properties": properties,
                        "size": size,
                        "size_gte": size_gte,
                        "size_lte": size_lte,
                        "sort": sort,
                        "type": type,
                        "updated_at": updated_at,
                        "updated_at_gte": updated_at_gte,
                        "updated_at_lte": updated_at_lte,
                        "url": url,
                        "width": width,
                        "width_gte": width_gte,
                        "width_lte": width_lte,
                    },
                    file_search_params.FileSearchParams,
                ),
            ),
            cast_to=CollectionResponseFile,
        )

    async def upload(
        self,
        *,
        charset_hunch: str | Omit = omit,
        file: FileTypes | Omit = omit,
        file_name: str | Omit = omit,
        folder_id: str | Omit = omit,
        folder_path: str | Omit = omit,
        options: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Upload file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "charset_hunch": charset_hunch,
                "file": file,
                "file_name": file_name,
                "folder_id": folder_id,
                "folder_path": folder_path,
                "options": options,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/files/v3/files",
            body=await async_maybe_transform(body, file_upload_params.FileUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.update = to_raw_response_wrapper(
            files.update,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.gdpr_delete = to_raw_response_wrapper(
            files.gdpr_delete,
        )
        self.get = to_raw_response_wrapper(
            files.get,
        )
        self.get_by_path = to_raw_response_wrapper(
            files.get_by_path,
        )
        self.get_import_from_url_async_status = to_raw_response_wrapper(
            files.get_import_from_url_async_status,
        )
        self.get_import_task_status = to_raw_response_wrapper(
            files.get_import_task_status,
        )
        self.get_signed_url = to_raw_response_wrapper(
            files.get_signed_url,
        )
        self.import_from_url_async = to_raw_response_wrapper(
            files.import_from_url_async,
        )
        self.replace = to_raw_response_wrapper(
            files.replace,
        )
        self.search = to_raw_response_wrapper(
            files.search,
        )
        self.upload = to_raw_response_wrapper(
            files.upload,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.update = async_to_raw_response_wrapper(
            files.update,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.gdpr_delete = async_to_raw_response_wrapper(
            files.gdpr_delete,
        )
        self.get = async_to_raw_response_wrapper(
            files.get,
        )
        self.get_by_path = async_to_raw_response_wrapper(
            files.get_by_path,
        )
        self.get_import_from_url_async_status = async_to_raw_response_wrapper(
            files.get_import_from_url_async_status,
        )
        self.get_import_task_status = async_to_raw_response_wrapper(
            files.get_import_task_status,
        )
        self.get_signed_url = async_to_raw_response_wrapper(
            files.get_signed_url,
        )
        self.import_from_url_async = async_to_raw_response_wrapper(
            files.import_from_url_async,
        )
        self.replace = async_to_raw_response_wrapper(
            files.replace,
        )
        self.search = async_to_raw_response_wrapper(
            files.search,
        )
        self.upload = async_to_raw_response_wrapper(
            files.upload,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.update = to_streamed_response_wrapper(
            files.update,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.gdpr_delete = to_streamed_response_wrapper(
            files.gdpr_delete,
        )
        self.get = to_streamed_response_wrapper(
            files.get,
        )
        self.get_by_path = to_streamed_response_wrapper(
            files.get_by_path,
        )
        self.get_import_from_url_async_status = to_streamed_response_wrapper(
            files.get_import_from_url_async_status,
        )
        self.get_import_task_status = to_streamed_response_wrapper(
            files.get_import_task_status,
        )
        self.get_signed_url = to_streamed_response_wrapper(
            files.get_signed_url,
        )
        self.import_from_url_async = to_streamed_response_wrapper(
            files.import_from_url_async,
        )
        self.replace = to_streamed_response_wrapper(
            files.replace,
        )
        self.search = to_streamed_response_wrapper(
            files.search,
        )
        self.upload = to_streamed_response_wrapper(
            files.upload,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.update = async_to_streamed_response_wrapper(
            files.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.gdpr_delete = async_to_streamed_response_wrapper(
            files.gdpr_delete,
        )
        self.get = async_to_streamed_response_wrapper(
            files.get,
        )
        self.get_by_path = async_to_streamed_response_wrapper(
            files.get_by_path,
        )
        self.get_import_from_url_async_status = async_to_streamed_response_wrapper(
            files.get_import_from_url_async_status,
        )
        self.get_import_task_status = async_to_streamed_response_wrapper(
            files.get_import_task_status,
        )
        self.get_signed_url = async_to_streamed_response_wrapper(
            files.get_signed_url,
        )
        self.import_from_url_async = async_to_streamed_response_wrapper(
            files.import_from_url_async,
        )
        self.replace = async_to_streamed_response_wrapper(
            files.replace,
        )
        self.search = async_to_streamed_response_wrapper(
            files.search,
        )
        self.upload = async_to_streamed_response_wrapper(
            files.upload,
        )
