# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types import (
    ToolAIDetectResponse,
    ToolParsePdfResponse,
    ToolWebSearchResponse,
    ToolContextAwareSplittingResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_ai_detect(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            tool = client.tools.ai_detect(
                input="AI and ML continue to be at the forefront of technological advancements. In 2025, we can expect more sophisticated AI systems that can handle complex tasks with greater efficiency. AI will play a crucial role in various sectors, including healthcare, finance, and manufacturing. For instance, AI-powered diagnostic tools will become more accurate, helping doctors detect diseases at an early stage. In finance, AI algorithms will enhance fraud detection and risk management.",
            )

        assert_matches_type(ToolAIDetectResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_ai_detect(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.tools.with_raw_response.ai_detect(
                input="AI and ML continue to be at the forefront of technological advancements. In 2025, we can expect more sophisticated AI systems that can handle complex tasks with greater efficiency. AI will play a crucial role in various sectors, including healthcare, finance, and manufacturing. For instance, AI-powered diagnostic tools will become more accurate, helping doctors detect diseases at an early stage. In finance, AI algorithms will enhance fraud detection and risk management.",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolAIDetectResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_ai_detect(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            with client.tools.with_streaming_response.ai_detect(
                input="AI and ML continue to be at the forefront of technological advancements. In 2025, we can expect more sophisticated AI systems that can handle complex tasks with greater efficiency. AI will play a crucial role in various sectors, including healthcare, finance, and manufacturing. For instance, AI-powered diagnostic tools will become more accurate, helping doctors detect diseases at an early stage. In finance, AI algorithms will enhance fraud detection and risk management.",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                tool = response.parse()
                assert_matches_type(ToolAIDetectResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_context_aware_splitting(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            tool = client.tools.context_aware_splitting(
                strategy="llm_split",
                text="text",
            )

        assert_matches_type(ToolContextAwareSplittingResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_context_aware_splitting(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.tools.with_raw_response.context_aware_splitting(
                strategy="llm_split",
                text="text",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolContextAwareSplittingResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_context_aware_splitting(self, client: Writer) -> None:
        with pytest.warns(DeprecationWarning):
            with client.tools.with_streaming_response.context_aware_splitting(
                strategy="llm_split",
                text="text",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                tool = response.parse()
                assert_matches_type(ToolContextAwareSplittingResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

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
    async def test_method_ai_detect(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            tool = await async_client.tools.ai_detect(
                input="AI and ML continue to be at the forefront of technological advancements. In 2025, we can expect more sophisticated AI systems that can handle complex tasks with greater efficiency. AI will play a crucial role in various sectors, including healthcare, finance, and manufacturing. For instance, AI-powered diagnostic tools will become more accurate, helping doctors detect diseases at an early stage. In finance, AI algorithms will enhance fraud detection and risk management.",
            )

        assert_matches_type(ToolAIDetectResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_ai_detect(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.tools.with_raw_response.ai_detect(
                input="AI and ML continue to be at the forefront of technological advancements. In 2025, we can expect more sophisticated AI systems that can handle complex tasks with greater efficiency. AI will play a crucial role in various sectors, including healthcare, finance, and manufacturing. For instance, AI-powered diagnostic tools will become more accurate, helping doctors detect diseases at an early stage. In finance, AI algorithms will enhance fraud detection and risk management.",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolAIDetectResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_ai_detect(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.tools.with_streaming_response.ai_detect(
                input="AI and ML continue to be at the forefront of technological advancements. In 2025, we can expect more sophisticated AI systems that can handle complex tasks with greater efficiency. AI will play a crucial role in various sectors, including healthcare, finance, and manufacturing. For instance, AI-powered diagnostic tools will become more accurate, helping doctors detect diseases at an early stage. In finance, AI algorithms will enhance fraud detection and risk management.",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                tool = await response.parse()
                assert_matches_type(ToolAIDetectResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_context_aware_splitting(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            tool = await async_client.tools.context_aware_splitting(
                strategy="llm_split",
                text="text",
            )

        assert_matches_type(ToolContextAwareSplittingResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_context_aware_splitting(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.tools.with_raw_response.context_aware_splitting(
                strategy="llm_split",
                text="text",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolContextAwareSplittingResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_context_aware_splitting(self, async_client: AsyncWriter) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.tools.with_streaming_response.context_aware_splitting(
                strategy="llm_split",
                text="text",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                tool = await response.parse()
                assert_matches_type(ToolContextAwareSplittingResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

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
