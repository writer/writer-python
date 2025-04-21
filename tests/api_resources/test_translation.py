# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types import TranslationResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTranslation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_translate(self, client: Writer) -> None:
        translation = client.translation.translate(
            formality=True,
            length_control=True,
            mask_profanity=True,
            model="palmyra-translate",
            source_language_code="en",
            target_language_code="es",
            text="Hello, world!",
        )
        assert_matches_type(TranslationResponse, translation, path=["response"])

    @parametrize
    def test_raw_response_translate(self, client: Writer) -> None:
        response = client.translation.with_raw_response.translate(
            formality=True,
            length_control=True,
            mask_profanity=True,
            model="palmyra-translate",
            source_language_code="en",
            target_language_code="es",
            text="Hello, world!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = response.parse()
        assert_matches_type(TranslationResponse, translation, path=["response"])

    @parametrize
    def test_streaming_response_translate(self, client: Writer) -> None:
        with client.translation.with_streaming_response.translate(
            formality=True,
            length_control=True,
            mask_profanity=True,
            model="palmyra-translate",
            source_language_code="en",
            target_language_code="es",
            text="Hello, world!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = response.parse()
            assert_matches_type(TranslationResponse, translation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTranslation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_translate(self, async_client: AsyncWriter) -> None:
        translation = await async_client.translation.translate(
            formality=True,
            length_control=True,
            mask_profanity=True,
            model="palmyra-translate",
            source_language_code="en",
            target_language_code="es",
            text="Hello, world!",
        )
        assert_matches_type(TranslationResponse, translation, path=["response"])

    @parametrize
    async def test_raw_response_translate(self, async_client: AsyncWriter) -> None:
        response = await async_client.translation.with_raw_response.translate(
            formality=True,
            length_control=True,
            mask_profanity=True,
            model="palmyra-translate",
            source_language_code="en",
            target_language_code="es",
            text="Hello, world!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        translation = await response.parse()
        assert_matches_type(TranslationResponse, translation, path=["response"])

    @parametrize
    async def test_streaming_response_translate(self, async_client: AsyncWriter) -> None:
        async with async_client.translation.with_streaming_response.translate(
            formality=True,
            length_control=True,
            mask_profanity=True,
            model="palmyra-translate",
            source_language_code="en",
            target_language_code="es",
            text="Hello, world!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            translation = await response.parse()
            assert_matches_type(TranslationResponse, translation, path=["response"])

        assert cast(Any, response.is_closed) is True
