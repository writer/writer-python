# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types import File
from writerai.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
