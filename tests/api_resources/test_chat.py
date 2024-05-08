# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import WriterAI, AsyncWriterAI
from tests.utils import assert_matches_type
from writerai.types import ChatChatResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_chat(self, client: WriterAI) -> None:
        chat = client.chat.chat(
            messages=[
                {
                    "content": "Hello!",
                    "role": "user",
                }
            ],
            model="palmyra-x-chat-v2-32k",
        )
        assert_matches_type(ChatChatResponse, chat, path=["response"])

    @parametrize
    def test_method_chat_with_all_params(self, client: WriterAI) -> None:
        chat = client.chat.chat(
            messages=[
                {
                    "content": "Hello!",
                    "role": "user",
                    "name": "string",
                }
            ],
            model="palmyra-x-chat-v2-32k",
            max_tokens=0,
            n=0,
            stop=["string", "string", "string"],
            stream=True,
            temperature=0,
            top_p=0,
        )
        assert_matches_type(ChatChatResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_chat(self, client: WriterAI) -> None:
        response = client.chat.with_raw_response.chat(
            messages=[
                {
                    "content": "Hello!",
                    "role": "user",
                }
            ],
            model="palmyra-x-chat-v2-32k",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatChatResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_chat(self, client: WriterAI) -> None:
        with client.chat.with_streaming_response.chat(
            messages=[
                {
                    "content": "Hello!",
                    "role": "user",
                }
            ],
            model="palmyra-x-chat-v2-32k",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatChatResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_chat(self, async_client: AsyncWriterAI) -> None:
        chat = await async_client.chat.chat(
            messages=[
                {
                    "content": "Hello!",
                    "role": "user",
                }
            ],
            model="palmyra-x-chat-v2-32k",
        )
        assert_matches_type(ChatChatResponse, chat, path=["response"])

    @parametrize
    async def test_method_chat_with_all_params(self, async_client: AsyncWriterAI) -> None:
        chat = await async_client.chat.chat(
            messages=[
                {
                    "content": "Hello!",
                    "role": "user",
                    "name": "string",
                }
            ],
            model="palmyra-x-chat-v2-32k",
            max_tokens=0,
            n=0,
            stop=["string", "string", "string"],
            stream=True,
            temperature=0,
            top_p=0,
        )
        assert_matches_type(ChatChatResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_chat(self, async_client: AsyncWriterAI) -> None:
        response = await async_client.chat.with_raw_response.chat(
            messages=[
                {
                    "content": "Hello!",
                    "role": "user",
                }
            ],
            model="palmyra-x-chat-v2-32k",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatChatResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_chat(self, async_client: AsyncWriterAI) -> None:
        async with async_client.chat.with_streaming_response.chat(
            messages=[
                {
                    "content": "Hello!",
                    "role": "user",
                }
            ],
            model="palmyra-x-chat-v2-32k",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatChatResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
