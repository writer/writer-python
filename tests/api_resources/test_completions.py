# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types import Completion

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Writer) -> None:
        completion = client.completions.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Writer) -> None:
        completion = client.completions.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
            best_of=1,
            max_tokens=150,
            random_seed=42,
            stop=["."],
            stream=False,
            temperature=0.7,
            top_p=0.9,
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Writer) -> None:
        response = client.completions.with_raw_response.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Writer) -> None:
        with client.completions.with_streaming_response.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(Completion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Writer) -> None:
        completion_stream = client.completions.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
            stream=True,
        )
        completion_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Writer) -> None:
        completion_stream = client.completions.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
            stream=True,
            best_of=1,
            max_tokens=150,
            random_seed=42,
            stop=["."],
            temperature=0.7,
            top_p=0.9,
        )
        completion_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: Writer) -> None:
        response = client.completions.with_raw_response.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Writer) -> None:
        with client.completions.with_streaming_response.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncWriter) -> None:
        completion = await async_client.completions.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncWriter) -> None:
        completion = await async_client.completions.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
            best_of=1,
            max_tokens=150,
            random_seed=42,
            stop=["."],
            stream=False,
            temperature=0.7,
            top_p=0.9,
        )
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncWriter) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(Completion, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncWriter) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(Completion, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncWriter) -> None:
        completion_stream = await async_client.completions.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
            stream=True,
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncWriter) -> None:
        completion_stream = await async_client.completions.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
            stream=True,
            best_of=1,
            max_tokens=150,
            random_seed=42,
            stop=["."],
            temperature=0.7,
            top_p=0.9,
        )
        await completion_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncWriter) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncWriter) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="palmyra-x-003-instruct",
            prompt="Write me an SEO article about...",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
