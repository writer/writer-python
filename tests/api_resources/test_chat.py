# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types import Chat

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_chat_overload_1(self, client: Writer) -> None:
        chat = client.chat.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_method_chat_with_all_params_overload_1(self, client: Writer) -> None:
        chat = client.chat.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                    "name": "name",
                }
            ],
            model="model",
            max_tokens=0,
            n=0,
            stop=["string", "string", "string"],
            stream=False,
            temperature=0,
            top_p=0,
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_raw_response_chat_overload_1(self, client: Writer) -> None:
        response = client.chat.with_raw_response.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    def test_streaming_response_chat_overload_1(self, client: Writer) -> None:
        with client.chat.with_streaming_response.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_chat_overload_2(self, client: Writer) -> None:
        chat_stream = client.chat.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
        )
        chat_stream.response.close()

    @parametrize
    def test_method_chat_with_all_params_overload_2(self, client: Writer) -> None:
        chat_stream = client.chat.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                    "name": "name",
                }
            ],
            model="model",
            stream=True,
            max_tokens=0,
            n=0,
            stop=["string", "string", "string"],
            temperature=0,
            top_p=0,
        )
        chat_stream.response.close()

    @parametrize
    def test_raw_response_chat_overload_2(self, client: Writer) -> None:
        response = client.chat.with_raw_response.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_chat_overload_2(self, client: Writer) -> None:
        with client.chat.with_streaming_response.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_chat_overload_1(self, async_client: AsyncWriter) -> None:
        chat = await async_client.chat.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_method_chat_with_all_params_overload_1(self, async_client: AsyncWriter) -> None:
        chat = await async_client.chat.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                    "name": "name",
                }
            ],
            model="model",
            max_tokens=0,
            n=0,
            stop=["string", "string", "string"],
            stream=False,
            temperature=0,
            top_p=0,
        )
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_raw_response_chat_overload_1(self, async_client: AsyncWriter) -> None:
        response = await async_client.chat.with_raw_response.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(Chat, chat, path=["response"])

    @parametrize
    async def test_streaming_response_chat_overload_1(self, async_client: AsyncWriter) -> None:
        async with async_client.chat.with_streaming_response.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(Chat, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_chat_overload_2(self, async_client: AsyncWriter) -> None:
        chat_stream = await async_client.chat.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
        )
        await chat_stream.response.aclose()

    @parametrize
    async def test_method_chat_with_all_params_overload_2(self, async_client: AsyncWriter) -> None:
        chat_stream = await async_client.chat.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                    "name": "name",
                }
            ],
            model="model",
            stream=True,
            max_tokens=0,
            n=0,
            stop=["string", "string", "string"],
            temperature=0,
            top_p=0,
        )
        await chat_stream.response.aclose()

    @parametrize
    async def test_raw_response_chat_overload_2(self, async_client: AsyncWriter) -> None:
        response = await async_client.chat.with_raw_response.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_chat_overload_2(self, async_client: AsyncWriter) -> None:
        async with async_client.chat.with_streaming_response.chat(
            messages=[
                {
                    "content": "content",
                    "role": "user",
                }
            ],
            model="model",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
