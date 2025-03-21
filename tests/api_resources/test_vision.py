# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types import VisionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVision:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_analyze(self, client: Writer) -> None:
        vision = client.vision.analyze(
            model="palmyra-vision",
            prompt="Describe the difference between the image {{image_1}} and the image {{image_2}}.",
            variables=[
                {
                    "file_id": "f1234",
                    "name": "image_1",
                },
                {
                    "file_id": "f9876",
                    "name": "image_2",
                },
            ],
        )
        assert_matches_type(VisionResponse, vision, path=["response"])

    @parametrize
    def test_raw_response_analyze(self, client: Writer) -> None:
        response = client.vision.with_raw_response.analyze(
            model="palmyra-vision",
            prompt="Describe the difference between the image {{image_1}} and the image {{image_2}}.",
            variables=[
                {
                    "file_id": "f1234",
                    "name": "image_1",
                },
                {
                    "file_id": "f9876",
                    "name": "image_2",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vision = response.parse()
        assert_matches_type(VisionResponse, vision, path=["response"])

    @parametrize
    def test_streaming_response_analyze(self, client: Writer) -> None:
        with client.vision.with_streaming_response.analyze(
            model="palmyra-vision",
            prompt="Describe the difference between the image {{image_1}} and the image {{image_2}}.",
            variables=[
                {
                    "file_id": "f1234",
                    "name": "image_1",
                },
                {
                    "file_id": "f9876",
                    "name": "image_2",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vision = response.parse()
            assert_matches_type(VisionResponse, vision, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVision:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_analyze(self, async_client: AsyncWriter) -> None:
        vision = await async_client.vision.analyze(
            model="palmyra-vision",
            prompt="Describe the difference between the image {{image_1}} and the image {{image_2}}.",
            variables=[
                {
                    "file_id": "f1234",
                    "name": "image_1",
                },
                {
                    "file_id": "f9876",
                    "name": "image_2",
                },
            ],
        )
        assert_matches_type(VisionResponse, vision, path=["response"])

    @parametrize
    async def test_raw_response_analyze(self, async_client: AsyncWriter) -> None:
        response = await async_client.vision.with_raw_response.analyze(
            model="palmyra-vision",
            prompt="Describe the difference between the image {{image_1}} and the image {{image_2}}.",
            variables=[
                {
                    "file_id": "f1234",
                    "name": "image_1",
                },
                {
                    "file_id": "f9876",
                    "name": "image_2",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vision = await response.parse()
        assert_matches_type(VisionResponse, vision, path=["response"])

    @parametrize
    async def test_streaming_response_analyze(self, async_client: AsyncWriter) -> None:
        async with async_client.vision.with_streaming_response.analyze(
            model="palmyra-vision",
            prompt="Describe the difference between the image {{image_1}} and the image {{image_2}}.",
            variables=[
                {
                    "file_id": "f1234",
                    "name": "image_1",
                },
                {
                    "file_id": "f9876",
                    "name": "image_2",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vision = await response.parse()
            assert_matches_type(VisionResponse, vision, path=["response"])

        assert cast(Any, response.is_closed) is True
