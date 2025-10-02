# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk.types import (
    FilesFile,
    FilesFolder,
    FilesFileStat,
    FilesSignedURL,
    FilesFileActionResponse,
    FilesFolderActionResponse,
    FilesCollectionResponseFile,
    FilesFolderUpdateTaskLocator,
    FilesImportFromURLTaskLocator,
)
from hubspot_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        file = client.files.create(
            name="name",
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: HubSpot) -> None:
        file = client.files.create(
            name="name",
            parent_folder_id="parentFolderId",
            parent_path="parentPath",
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FilesFolder, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        file = client.files.delete(
            "321669910225",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.delete(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.delete(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_archive_by_path(self, client: HubSpot) -> None:
        file = client.files.archive_by_path(
            "folderPath",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_archive_by_path(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.archive_by_path(
            "folderPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_archive_by_path(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.archive_by_path(
            "folderPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_archive_by_path(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_path` but received ''"):
            client.files.with_raw_response.archive_by_path(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_import(self, client: HubSpot) -> None:
        file = client.files.check_import(
            "taskId",
        )
        assert_matches_type(FilesFileActionResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check_import(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.check_import(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FilesFileActionResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check_import(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.check_import(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FilesFileActionResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_check_import(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.files.with_raw_response.check_import(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_update_status(self, client: HubSpot) -> None:
        file = client.files.check_update_status(
            "taskId",
        )
        assert_matches_type(FilesFolderActionResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check_update_status(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.check_update_status(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FilesFolderActionResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check_update_status(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.check_update_status(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FilesFolderActionResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_check_update_status(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.files.with_raw_response.check_update_status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_path(self, client: HubSpot) -> None:
        file = client.files.get_by_path(
            folder_path="folderPath",
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_path_with_all_params(self, client: HubSpot) -> None:
        file = client.files.get_by_path(
            folder_path="folderPath",
            properties=["string"],
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_path(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.get_by_path(
            folder_path="folderPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_path(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.get_by_path(
            folder_path="folderPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FilesFolder, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_by_path(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_path` but received ''"):
            client.files.with_raw_response.get_by_path(
                folder_path="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_metadata(self, client: HubSpot) -> None:
        file = client.files.get_metadata(
            path="path",
        )
        assert_matches_type(FilesFileStat, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_metadata_with_all_params(self, client: HubSpot) -> None:
        file = client.files.get_metadata(
            path="path",
            properties=["string"],
        )
        assert_matches_type(FilesFileStat, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_metadata(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.get_metadata(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FilesFileStat, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_metadata(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.get_metadata(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FilesFileStat, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_metadata(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            client.files.with_raw_response.get_metadata(
                path="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_signed_url(self, client: HubSpot) -> None:
        file = client.files.get_signed_url(
            file_id="321669910225",
        )
        assert_matches_type(FilesSignedURL, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_signed_url_with_all_params(self, client: HubSpot) -> None:
        file = client.files.get_signed_url(
            file_id="321669910225",
            expiration_seconds=0,
            size="thumb",
            upscale=True,
        )
        assert_matches_type(FilesSignedURL, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_signed_url(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.get_signed_url(
            file_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FilesSignedURL, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_signed_url(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.get_signed_url(
            file_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FilesSignedURL, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_signed_url(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.get_signed_url(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_from_url(self, client: HubSpot) -> None:
        file = client.files.import_from_url(
            access="PUBLIC_INDEXABLE",
            url="url",
        )
        assert_matches_type(FilesImportFromURLTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_import_from_url_with_all_params(self, client: HubSpot) -> None:
        file = client.files.import_from_url(
            access="PUBLIC_INDEXABLE",
            url="url",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            folder_id="folderId",
            folder_path="folderPath",
            name="name",
            overwrite=True,
            ttl="ttl",
        )
        assert_matches_type(FilesImportFromURLTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_import_from_url(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.import_from_url(
            access="PUBLIC_INDEXABLE",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FilesImportFromURLTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_import_from_url(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.import_from_url(
            access="PUBLIC_INDEXABLE",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FilesImportFromURLTaskLocator, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_purge(self, client: HubSpot) -> None:
        file = client.files.purge(
            "321669910225",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_purge(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.purge(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_purge(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.purge(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_purge(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.purge(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read(self, client: HubSpot) -> None:
        file = client.files.read(
            folder_id="321669910225",
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_with_all_params(self, client: HubSpot) -> None:
        file = client.files.read(
            folder_id="321669910225",
            properties=["string"],
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.read(
            folder_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.read(
            folder_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FilesFolder, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.files.with_raw_response.read(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace(self, client: HubSpot) -> None:
        file = client.files.replace(
            file_id="321669910225",
        )
        assert_matches_type(FilesFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: HubSpot) -> None:
        file = client.files.replace(
            file_id="321669910225",
            charset_hunch="charsetHunch",
            file=b"raw file contents",
            options="options",
        )
        assert_matches_type(FilesFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.replace(
            file_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FilesFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.replace(
            file_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FilesFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.replace(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: HubSpot) -> None:
        file = client.files.search()
        assert_matches_type(FilesCollectionResponseFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: HubSpot) -> None:
        file = client.files.search(
            after="after",
            allows_anonymous_access=True,
            before="before",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            encoding="encoding",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            expires_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            expires_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            extension="extension",
            file_md5="fileMd5",
            height=0,
            height_gte=0,
            height_lte=0,
            id_gte=0,
            id_lte=0,
            ids=[0],
            is_usable_in_content=True,
            limit=0,
            name="name",
            parent_folder_ids=[0],
            path="path",
            properties=["string"],
            size=0,
            size_gte=0,
            size_lte=0,
            sort=["string"],
            type="type",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            url="url",
            width=0,
            width_gte=0,
            width_lte=0,
        )
        assert_matches_type(FilesCollectionResponseFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FilesCollectionResponseFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FilesCollectionResponseFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_properties(self, client: HubSpot) -> None:
        file = client.files.update_properties(
            folder_id="321669910225",
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_properties_with_all_params(self, client: HubSpot) -> None:
        file = client.files.update_properties(
            folder_id="321669910225",
            name="name",
            parent_folder_id=0,
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_properties(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.update_properties(
            folder_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_properties(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.update_properties(
            folder_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FilesFolder, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_properties(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            client.files.with_raw_response.update_properties(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_properties_recursively(self, client: HubSpot) -> None:
        file = client.files.update_properties_recursively(
            id="id",
        )
        assert_matches_type(FilesFolderUpdateTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_properties_recursively_with_all_params(self, client: HubSpot) -> None:
        file = client.files.update_properties_recursively(
            id="id",
            name="name",
            parent_folder_id=0,
        )
        assert_matches_type(FilesFolderUpdateTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_properties_recursively(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.update_properties_recursively(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FilesFolderUpdateTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_properties_recursively(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.update_properties_recursively(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FilesFolderUpdateTaskLocator, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: HubSpot) -> None:
        file = client.files.upload()
        assert_matches_type(FilesFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: HubSpot) -> None:
        file = client.files.upload(
            charset_hunch="charsetHunch",
            file=b"raw file contents",
            file_name="fileName",
            folder_id="folderId",
            folder_path="folderPath",
            options="options",
        )
        assert_matches_type(FilesFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: HubSpot) -> None:
        response = client.files.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FilesFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: HubSpot) -> None:
        with client.files.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FilesFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.create(
            name="name",
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.create(
            name="name",
            parent_folder_id="parentFolderId",
            parent_path="parentPath",
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FilesFolder, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.delete(
            "321669910225",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.delete(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.delete(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_archive_by_path(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.archive_by_path(
            "folderPath",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_archive_by_path(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.archive_by_path(
            "folderPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_archive_by_path(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.archive_by_path(
            "folderPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_archive_by_path(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_path` but received ''"):
            await async_client.files.with_raw_response.archive_by_path(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_import(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.check_import(
            "taskId",
        )
        assert_matches_type(FilesFileActionResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check_import(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.check_import(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FilesFileActionResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check_import(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.check_import(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FilesFileActionResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_check_import(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.files.with_raw_response.check_import(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_update_status(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.check_update_status(
            "taskId",
        )
        assert_matches_type(FilesFolderActionResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check_update_status(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.check_update_status(
            "taskId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FilesFolderActionResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check_update_status(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.check_update_status(
            "taskId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FilesFolderActionResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_check_update_status(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.files.with_raw_response.check_update_status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_path(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.get_by_path(
            folder_path="folderPath",
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_path_with_all_params(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.get_by_path(
            folder_path="folderPath",
            properties=["string"],
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_path(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.get_by_path(
            folder_path="folderPath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_path(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.get_by_path(
            folder_path="folderPath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FilesFolder, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_by_path(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_path` but received ''"):
            await async_client.files.with_raw_response.get_by_path(
                folder_path="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_metadata(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.get_metadata(
            path="path",
        )
        assert_matches_type(FilesFileStat, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_metadata_with_all_params(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.get_metadata(
            path="path",
            properties=["string"],
        )
        assert_matches_type(FilesFileStat, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_metadata(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.get_metadata(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FilesFileStat, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_metadata(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.get_metadata(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FilesFileStat, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_metadata(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path` but received ''"):
            await async_client.files.with_raw_response.get_metadata(
                path="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_signed_url(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.get_signed_url(
            file_id="321669910225",
        )
        assert_matches_type(FilesSignedURL, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_signed_url_with_all_params(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.get_signed_url(
            file_id="321669910225",
            expiration_seconds=0,
            size="thumb",
            upscale=True,
        )
        assert_matches_type(FilesSignedURL, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_signed_url(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.get_signed_url(
            file_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FilesSignedURL, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_signed_url(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.get_signed_url(
            file_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FilesSignedURL, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_signed_url(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.get_signed_url(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_from_url(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.import_from_url(
            access="PUBLIC_INDEXABLE",
            url="url",
        )
        assert_matches_type(FilesImportFromURLTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_import_from_url_with_all_params(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.import_from_url(
            access="PUBLIC_INDEXABLE",
            url="url",
            duplicate_validation_scope="ENTIRE_PORTAL",
            duplicate_validation_strategy="NONE",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            folder_id="folderId",
            folder_path="folderPath",
            name="name",
            overwrite=True,
            ttl="ttl",
        )
        assert_matches_type(FilesImportFromURLTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_import_from_url(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.import_from_url(
            access="PUBLIC_INDEXABLE",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FilesImportFromURLTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_import_from_url(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.import_from_url(
            access="PUBLIC_INDEXABLE",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FilesImportFromURLTaskLocator, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_purge(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.purge(
            "321669910225",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_purge(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.purge(
            "321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_purge(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.purge(
            "321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_purge(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.purge(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.read(
            folder_id="321669910225",
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.read(
            folder_id="321669910225",
            properties=["string"],
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.read(
            folder_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.read(
            folder_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FilesFolder, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.files.with_raw_response.read(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.replace(
            file_id="321669910225",
        )
        assert_matches_type(FilesFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.replace(
            file_id="321669910225",
            charset_hunch="charsetHunch",
            file=b"raw file contents",
            options="options",
        )
        assert_matches_type(FilesFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.replace(
            file_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FilesFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.replace(
            file_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FilesFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.replace(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.search()
        assert_matches_type(FilesCollectionResponseFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.search(
            after="after",
            allows_anonymous_access=True,
            before="before",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            encoding="encoding",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            expires_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            expires_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            extension="extension",
            file_md5="fileMd5",
            height=0,
            height_gte=0,
            height_lte=0,
            id_gte=0,
            id_lte=0,
            ids=[0],
            is_usable_in_content=True,
            limit=0,
            name="name",
            parent_folder_ids=[0],
            path="path",
            properties=["string"],
            size=0,
            size_gte=0,
            size_lte=0,
            sort=["string"],
            type="type",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            updated_at_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            url="url",
            width=0,
            width_gte=0,
            width_lte=0,
        )
        assert_matches_type(FilesCollectionResponseFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FilesCollectionResponseFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FilesCollectionResponseFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_properties(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.update_properties(
            folder_id="321669910225",
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_properties_with_all_params(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.update_properties(
            folder_id="321669910225",
            name="name",
            parent_folder_id=0,
        )
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_properties(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.update_properties(
            folder_id="321669910225",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FilesFolder, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_properties(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.update_properties(
            folder_id="321669910225",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FilesFolder, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_properties(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `folder_id` but received ''"):
            await async_client.files.with_raw_response.update_properties(
                folder_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_properties_recursively(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.update_properties_recursively(
            id="id",
        )
        assert_matches_type(FilesFolderUpdateTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_properties_recursively_with_all_params(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.update_properties_recursively(
            id="id",
            name="name",
            parent_folder_id=0,
        )
        assert_matches_type(FilesFolderUpdateTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_properties_recursively(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.update_properties_recursively(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FilesFolderUpdateTaskLocator, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_properties_recursively(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.update_properties_recursively(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FilesFolderUpdateTaskLocator, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.upload()
        assert_matches_type(FilesFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncHubSpot) -> None:
        file = await async_client.files.upload(
            charset_hunch="charsetHunch",
            file=b"raw file contents",
            file_name="fileName",
            folder_id="folderId",
            folder_path="folderPath",
            options="options",
        )
        assert_matches_type(FilesFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.files.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FilesFile, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncHubSpot) -> None:
        async with async_client.files.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FilesFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True
