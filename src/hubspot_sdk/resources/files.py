# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, Iterable, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    file_read_params,
    file_create_params,
    file_search_params,
    file_upload_params,
    file_replace_params,
    file_get_by_path_params,
    file_get_metadata_params,
    file_get_signed_url_params,
    file_import_from_url_params,
    file_update_properties_params,
    file_update_properties_recursively_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.files_file import FilesFile
from ..types.files_folder import FilesFolder
from ..types.files_file_stat import FilesFileStat
from ..types.files_signed_url import FilesSignedURL
from ..types.files_file_action_response import FilesFileActionResponse
from ..types.files_folder_action_response import FilesFolderActionResponse
from ..types.files_collection_response_file import FilesCollectionResponseFile
from ..types.files_folder_update_task_locator import FilesFolderUpdateTaskLocator
from ..types.files_import_from_url_task_locator import FilesImportFromURLTaskLocator

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

    def create(
        self,
        *,
        name: str,
        parent_folder_id: str | Omit = omit,
        parent_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFolder:
        """
        Create folder

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/files/v3/folders",
            body=maybe_transform(
                {
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "parent_path": parent_path,
                },
                file_create_params.FileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilesFolder,
        )

    def delete(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete folder by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/files/v3/folders/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def archive_by_path(
        self,
        folder_path: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete folder by path

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_path:
            raise ValueError(f"Expected a non-empty value for `folder_path` but received {folder_path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/files/v3/folders/{folder_path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def check_import(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFileActionResponse:
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
            cast_to=FilesFileActionResponse,
        )

    def check_update_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFolderActionResponse:
        """
        Check folder update status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            f"/files/v3/folders/update/async/tasks/{task_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilesFolderActionResponse,
        )

    def get_by_path(
        self,
        folder_path: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFolder:
        """
        Retrieve folder by path

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_path:
            raise ValueError(f"Expected a non-empty value for `folder_path` but received {folder_path!r}")
        return self._get(
            f"/files/v3/folders/{folder_path}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"properties": properties}, file_get_by_path_params.FileGetByPathParams),
            ),
            cast_to=FilesFolder,
        )

    def get_metadata(
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
    ) -> FilesFileStat:
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
                query=maybe_transform({"properties": properties}, file_get_metadata_params.FileGetMetadataParams),
            ),
            cast_to=FilesFileStat,
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
    ) -> FilesSignedURL:
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
            cast_to=FilesSignedURL,
        )

    def import_from_url(
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
    ) -> FilesImportFromURLTaskLocator:
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
                file_import_from_url_params.FileImportFromURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilesImportFromURLTaskLocator,
        )

    def purge(
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

    def read(
        self,
        folder_id: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFolder:
        """
        Retrieve folder by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._get(
            f"/files/v3/folders/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"properties": properties}, file_read_params.FileReadParams),
            ),
            cast_to=FilesFolder,
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
    ) -> FilesFile:
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
            cast_to=FilesFile,
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
    ) -> FilesCollectionResponseFile:
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
            cast_to=FilesCollectionResponseFile,
        )

    def update_properties(
        self,
        folder_id: str,
        *,
        name: str | Omit = omit,
        parent_folder_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFolder:
        """
        Update folder properties by folder ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._patch(
            f"/files/v3/folders/{folder_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                },
                file_update_properties_params.FileUpdatePropertiesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilesFolder,
        )

    def update_properties_recursively(
        self,
        *,
        id: str,
        name: str | Omit = omit,
        parent_folder_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFolderUpdateTaskLocator:
        """
        Update folder properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/files/v3/folders/update/async",
            body=maybe_transform(
                {
                    "id": id,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                },
                file_update_properties_recursively_params.FileUpdatePropertiesRecursivelyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilesFolderUpdateTaskLocator,
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
    ) -> FilesFile:
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
            cast_to=FilesFile,
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

    async def create(
        self,
        *,
        name: str,
        parent_folder_id: str | Omit = omit,
        parent_path: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFolder:
        """
        Create folder

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/files/v3/folders",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                    "parent_path": parent_path,
                },
                file_create_params.FileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilesFolder,
        )

    async def delete(
        self,
        folder_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete folder by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/files/v3/folders/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def archive_by_path(
        self,
        folder_path: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete folder by path

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_path:
            raise ValueError(f"Expected a non-empty value for `folder_path` but received {folder_path!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/files/v3/folders/{folder_path}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def check_import(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFileActionResponse:
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
            cast_to=FilesFileActionResponse,
        )

    async def check_update_status(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFolderActionResponse:
        """
        Check folder update status

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            f"/files/v3/folders/update/async/tasks/{task_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilesFolderActionResponse,
        )

    async def get_by_path(
        self,
        folder_path: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFolder:
        """
        Retrieve folder by path

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_path:
            raise ValueError(f"Expected a non-empty value for `folder_path` but received {folder_path!r}")
        return await self._get(
            f"/files/v3/folders/{folder_path}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"properties": properties}, file_get_by_path_params.FileGetByPathParams
                ),
            ),
            cast_to=FilesFolder,
        )

    async def get_metadata(
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
    ) -> FilesFileStat:
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
                    {"properties": properties}, file_get_metadata_params.FileGetMetadataParams
                ),
            ),
            cast_to=FilesFileStat,
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
    ) -> FilesSignedURL:
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
            cast_to=FilesSignedURL,
        )

    async def import_from_url(
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
    ) -> FilesImportFromURLTaskLocator:
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
                file_import_from_url_params.FileImportFromURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilesImportFromURLTaskLocator,
        )

    async def purge(
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

    async def read(
        self,
        folder_id: str,
        *,
        properties: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFolder:
        """
        Retrieve folder by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._get(
            f"/files/v3/folders/{folder_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"properties": properties}, file_read_params.FileReadParams),
            ),
            cast_to=FilesFolder,
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
    ) -> FilesFile:
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
            cast_to=FilesFile,
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
    ) -> FilesCollectionResponseFile:
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
            cast_to=FilesCollectionResponseFile,
        )

    async def update_properties(
        self,
        folder_id: str,
        *,
        name: str | Omit = omit,
        parent_folder_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFolder:
        """
        Update folder properties by folder ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._patch(
            f"/files/v3/folders/{folder_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                },
                file_update_properties_params.FileUpdatePropertiesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilesFolder,
        )

    async def update_properties_recursively(
        self,
        *,
        id: str,
        name: str | Omit = omit,
        parent_folder_id: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FilesFolderUpdateTaskLocator:
        """
        Update folder properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/files/v3/folders/update/async",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "name": name,
                    "parent_folder_id": parent_folder_id,
                },
                file_update_properties_recursively_params.FileUpdatePropertiesRecursivelyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FilesFolderUpdateTaskLocator,
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
    ) -> FilesFile:
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
            cast_to=FilesFile,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_raw_response_wrapper(
            files.create,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.archive_by_path = to_raw_response_wrapper(
            files.archive_by_path,
        )
        self.check_import = to_raw_response_wrapper(
            files.check_import,
        )
        self.check_update_status = to_raw_response_wrapper(
            files.check_update_status,
        )
        self.get_by_path = to_raw_response_wrapper(
            files.get_by_path,
        )
        self.get_metadata = to_raw_response_wrapper(
            files.get_metadata,
        )
        self.get_signed_url = to_raw_response_wrapper(
            files.get_signed_url,
        )
        self.import_from_url = to_raw_response_wrapper(
            files.import_from_url,
        )
        self.purge = to_raw_response_wrapper(
            files.purge,
        )
        self.read = to_raw_response_wrapper(
            files.read,
        )
        self.replace = to_raw_response_wrapper(
            files.replace,
        )
        self.search = to_raw_response_wrapper(
            files.search,
        )
        self.update_properties = to_raw_response_wrapper(
            files.update_properties,
        )
        self.update_properties_recursively = to_raw_response_wrapper(
            files.update_properties_recursively,
        )
        self.upload = to_raw_response_wrapper(
            files.upload,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_raw_response_wrapper(
            files.create,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.archive_by_path = async_to_raw_response_wrapper(
            files.archive_by_path,
        )
        self.check_import = async_to_raw_response_wrapper(
            files.check_import,
        )
        self.check_update_status = async_to_raw_response_wrapper(
            files.check_update_status,
        )
        self.get_by_path = async_to_raw_response_wrapper(
            files.get_by_path,
        )
        self.get_metadata = async_to_raw_response_wrapper(
            files.get_metadata,
        )
        self.get_signed_url = async_to_raw_response_wrapper(
            files.get_signed_url,
        )
        self.import_from_url = async_to_raw_response_wrapper(
            files.import_from_url,
        )
        self.purge = async_to_raw_response_wrapper(
            files.purge,
        )
        self.read = async_to_raw_response_wrapper(
            files.read,
        )
        self.replace = async_to_raw_response_wrapper(
            files.replace,
        )
        self.search = async_to_raw_response_wrapper(
            files.search,
        )
        self.update_properties = async_to_raw_response_wrapper(
            files.update_properties,
        )
        self.update_properties_recursively = async_to_raw_response_wrapper(
            files.update_properties_recursively,
        )
        self.upload = async_to_raw_response_wrapper(
            files.upload,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_streamed_response_wrapper(
            files.create,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.archive_by_path = to_streamed_response_wrapper(
            files.archive_by_path,
        )
        self.check_import = to_streamed_response_wrapper(
            files.check_import,
        )
        self.check_update_status = to_streamed_response_wrapper(
            files.check_update_status,
        )
        self.get_by_path = to_streamed_response_wrapper(
            files.get_by_path,
        )
        self.get_metadata = to_streamed_response_wrapper(
            files.get_metadata,
        )
        self.get_signed_url = to_streamed_response_wrapper(
            files.get_signed_url,
        )
        self.import_from_url = to_streamed_response_wrapper(
            files.import_from_url,
        )
        self.purge = to_streamed_response_wrapper(
            files.purge,
        )
        self.read = to_streamed_response_wrapper(
            files.read,
        )
        self.replace = to_streamed_response_wrapper(
            files.replace,
        )
        self.search = to_streamed_response_wrapper(
            files.search,
        )
        self.update_properties = to_streamed_response_wrapper(
            files.update_properties,
        )
        self.update_properties_recursively = to_streamed_response_wrapper(
            files.update_properties_recursively,
        )
        self.upload = to_streamed_response_wrapper(
            files.upload,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_streamed_response_wrapper(
            files.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.archive_by_path = async_to_streamed_response_wrapper(
            files.archive_by_path,
        )
        self.check_import = async_to_streamed_response_wrapper(
            files.check_import,
        )
        self.check_update_status = async_to_streamed_response_wrapper(
            files.check_update_status,
        )
        self.get_by_path = async_to_streamed_response_wrapper(
            files.get_by_path,
        )
        self.get_metadata = async_to_streamed_response_wrapper(
            files.get_metadata,
        )
        self.get_signed_url = async_to_streamed_response_wrapper(
            files.get_signed_url,
        )
        self.import_from_url = async_to_streamed_response_wrapper(
            files.import_from_url,
        )
        self.purge = async_to_streamed_response_wrapper(
            files.purge,
        )
        self.read = async_to_streamed_response_wrapper(
            files.read,
        )
        self.replace = async_to_streamed_response_wrapper(
            files.replace,
        )
        self.search = async_to_streamed_response_wrapper(
            files.search,
        )
        self.update_properties = async_to_streamed_response_wrapper(
            files.update_properties,
        )
        self.update_properties_recursively = async_to_streamed_response_wrapper(
            files.update_properties_recursively,
        )
        self.upload = async_to_streamed_response_wrapper(
            files.upload,
        )
