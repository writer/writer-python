# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types import ToolParsePdfResponse, ToolWebSearchResponse

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_parse_pdf(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            tool = client.tools.parse_pdf(
                file_id="file_id",
                format="text",
            )

        assert_matches_type(ToolParsePdfResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_parse_pdf(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.tools.with_raw_response.parse_pdf(
                file_id="file_id",
                format="text",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolParsePdfResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_parse_pdf(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            with client.tools.with_streaming_response.parse_pdf(
                file_id="file_id",
                format="text",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                tool = response.parse()
                assert_matches_type(ToolParsePdfResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_parse_pdf(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                client.tools.with_raw_response.parse_pdf(
                    file_id="",
                    format="text",
                )

    @parametrize
    def test_method_web_search(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            tool = client.tools.web_search()

        assert_matches_type(ToolWebSearchResponse, tool, path=["response"])

    @parametrize
    def test_method_web_search_with_all_params(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            tool = client.tools.web_search(
                chunks_per_source=0,
                country="afghanistan",
                days=0,
                exclude_domains=["string"],
                include_answer=True,
                include_domains=["dev.writer.com"],
                include_raw_content="text",
                max_results=0,
                query="How do I get an API key for the Writer API?",
                search_depth="basic",
                stream=True,
                time_range="day",
                topic="general",
            )

        assert_matches_type(ToolWebSearchResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_web_search(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.tools.with_raw_response.web_search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolWebSearchResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_web_search(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            with client.tools.with_streaming_response.web_search() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                tool = response.parse()
                assert_matches_type(ToolWebSearchResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_parse_pdf(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            tool = await async_client.tools.parse_pdf(
                file_id="file_id",
                format="text",
            )

        assert_matches_type(ToolParsePdfResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_parse_pdf(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.tools.with_raw_response.parse_pdf(
                file_id="file_id",
                format="text",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolParsePdfResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_parse_pdf(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.tools.with_streaming_response.parse_pdf(
                file_id="file_id",
                format="text",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                tool = await response.parse()
                assert_matches_type(ToolParsePdfResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_parse_pdf(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
                await async_client.tools.with_raw_response.parse_pdf(
                    file_id="",
                    format="text",
                )

    @parametrize
    async def test_method_web_search(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            tool = await async_client.tools.web_search()

        assert_matches_type(ToolWebSearchResponse, tool, path=["response"])

    @parametrize
    async def test_method_web_search_with_all_params(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            tool = await async_client.tools.web_search(
                chunks_per_source=0,
                country="afghanistan",
                days=0,
                exclude_domains=["string"],
                include_answer=True,
                include_domains=["dev.writer.com"],
                include_raw_content="text",
                max_results=0,
                query="How do I get an API key for the Writer API?",
                search_depth="basic",
                stream=True,
                time_range="day",
                topic="general",
            )

        assert_matches_type(ToolWebSearchResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_web_search(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.tools.with_raw_response.web_search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolWebSearchResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_web_search(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.tools.with_streaming_response.web_search() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                tool = await response.parse()
                assert_matches_type(ToolWebSearchResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True
