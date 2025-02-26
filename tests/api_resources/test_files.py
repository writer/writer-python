# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types import (
    File,
    FileRetryResponse,
    FileDeleteResponse,
)
from writerai._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from writerai.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Writer) -> None:
        file = client.files.retrieve(
            "file_id",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Writer) -> None:
        response = client.files.with_raw_response.retrieve(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Writer) -> None:
        with client.files.with_streaming_response.retrieve(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Writer) -> None:
        file = client.files.list()
        assert_matches_type(SyncCursorPage[File], file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Writer) -> None:
        file = client.files.list(
            after="after",
            before="before",
            graph_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            order="asc",
            status="in_progress",
        )
        assert_matches_type(SyncCursorPage[File], file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Writer) -> None:
        response = client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncCursorPage[File], file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Writer) -> None:
        with client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(SyncCursorPage[File], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Writer) -> None:
        file = client.files.delete(
            "file_id",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Writer) -> None:
        response = client.files.with_raw_response.delete(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Writer) -> None:
        with client.files.with_streaming_response.delete(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Writer, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files/file_id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        file = client.files.download(
            "file_id",
        )
        assert file.is_closed
        assert file.json() == {"foo": "bar"}
        assert cast(Any, file.is_closed) is True
        assert isinstance(file, BinaryAPIResponse)

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Writer, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files/file_id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        file = client.files.with_raw_response.download(
            "file_id",
        )

        assert file.is_closed is True
        assert file.http_request.headers.get("X-Stainless-Lang") == "python"
        assert file.json() == {"foo": "bar"}
        assert isinstance(file, BinaryAPIResponse)

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Writer, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files/file_id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.files.with_streaming_response.download(
            "file_id",
        ) as file:
            assert not file.is_closed
            assert file.http_request.headers.get("X-Stainless-Lang") == "python"

            assert file.json() == {"foo": "bar"}
            assert cast(Any, file.is_closed) is True
            assert isinstance(file, StreamedBinaryAPIResponse)

        assert cast(Any, file.is_closed) is True

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.download(
                "",
            )

    @parametrize
    def test_method_retry(self, client: Writer) -> None:
        file = client.files.retry(
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(FileRetryResponse, file, path=["response"])

    @parametrize
    def test_raw_response_retry(self, client: Writer) -> None:
        response = client.files.with_raw_response.retry(
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileRetryResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_retry(self, client: Writer) -> None:
        with client.files.with_streaming_response.retry(
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileRetryResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    def test_method_upload(self, client: Writer) -> None:
        file = client.files.upload(
            content=b"raw file contents",
            content_disposition="Content-Disposition",
            content_type="Content-Type",
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    def test_raw_response_upload(self, client: Writer) -> None:
        response = client.files.with_raw_response.upload(
            content=b"raw file contents",
            content_disposition="Content-Disposition",
            content_type="Content-Type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    def test_streaming_response_upload(self, client: Writer) -> None:
        with client.files.with_streaming_response.upload(
            content=b"raw file contents",
            content_disposition="Content-Disposition",
            content_type="Content-Type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWriter) -> None:
        file = await async_client.files.retrieve(
            "file_id",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWriter) -> None:
        response = await async_client.files.with_raw_response.retrieve(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWriter) -> None:
        async with async_client.files.with_streaming_response.retrieve(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncWriter) -> None:
        file = await async_client.files.list()
        assert_matches_type(AsyncCursorPage[File], file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWriter) -> None:
        file = await async_client.files.list(
            after="after",
            before="before",
            graph_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            order="asc",
            status="in_progress",
        )
        assert_matches_type(AsyncCursorPage[File], file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWriter) -> None:
        response = await async_client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(AsyncCursorPage[File], file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWriter) -> None:
        async with async_client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(AsyncCursorPage[File], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncWriter) -> None:
        file = await async_client.files.delete(
            "file_id",
        )
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWriter) -> None:
        response = await async_client.files.with_raw_response.delete(
            "file_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileDeleteResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWriter) -> None:
        async with async_client.files.with_streaming_response.delete(
            "file_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDeleteResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncWriter, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files/file_id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        file = await async_client.files.download(
            "file_id",
        )
        assert file.is_closed
        assert await file.json() == {"foo": "bar"}
        assert cast(Any, file.is_closed) is True
        assert isinstance(file, AsyncBinaryAPIResponse)

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncWriter, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files/file_id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        file = await async_client.files.with_raw_response.download(
            "file_id",
        )

        assert file.is_closed is True
        assert file.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await file.json() == {"foo": "bar"}
        assert isinstance(file, AsyncBinaryAPIResponse)

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncWriter, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/files/file_id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.files.with_streaming_response.download(
            "file_id",
        ) as file:
            assert not file.is_closed
            assert file.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await file.json() == {"foo": "bar"}
            assert cast(Any, file.is_closed) is True
            assert isinstance(file, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, file.is_closed) is True

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.download(
                "",
            )

    @parametrize
    async def test_method_retry(self, async_client: AsyncWriter) -> None:
        file = await async_client.files.retry(
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(FileRetryResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncWriter) -> None:
        response = await async_client.files.with_raw_response.retry(
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileRetryResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncWriter) -> None:
        async with async_client.files.with_streaming_response.retry(
            file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileRetryResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    async def test_method_upload(self, async_client: AsyncWriter) -> None:
        file = await async_client.files.upload(
            content=b"raw file contents",
            content_disposition="Content-Disposition",
            content_type="Content-Type",
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncWriter) -> None:
        response = await async_client.files.with_raw_response.upload(
            content=b"raw file contents",
            content_disposition="Content-Disposition",
            content_type="Content-Type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="requests with binary data not yet supported in test environment")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncWriter) -> None:
        async with async_client.files.with_streaming_response.upload(
            content=b"raw file contents",
            content_disposition="Content-Disposition",
            content_type="Content-Type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True
