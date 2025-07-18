# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types.tools import ComprehendMedicalResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComprehend:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_medical(self, client: Writer) -> None:
        comprehend = client.tools.comprehend.medical(
            content="content",
            response_type="Entities",
        )
        assert_matches_type(ComprehendMedicalResponse, comprehend, path=["response"])

    @parametrize
    def test_raw_response_medical(self, client: Writer) -> None:
        response = client.tools.comprehend.with_raw_response.medical(
            content="content",
            response_type="Entities",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comprehend = response.parse()
        assert_matches_type(ComprehendMedicalResponse, comprehend, path=["response"])

    @parametrize
    def test_streaming_response_medical(self, client: Writer) -> None:
        with client.tools.comprehend.with_streaming_response.medical(
            content="content",
            response_type="Entities",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comprehend = response.parse()
            assert_matches_type(ComprehendMedicalResponse, comprehend, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncComprehend:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_medical(self, async_client: AsyncWriter) -> None:
        comprehend = await async_client.tools.comprehend.medical(
            content="content",
            response_type="Entities",
        )
        assert_matches_type(ComprehendMedicalResponse, comprehend, path=["response"])

    @parametrize
    async def test_raw_response_medical(self, async_client: AsyncWriter) -> None:
        response = await async_client.tools.comprehend.with_raw_response.medical(
            content="content",
            response_type="Entities",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comprehend = await response.parse()
        assert_matches_type(ComprehendMedicalResponse, comprehend, path=["response"])

    @parametrize
    async def test_streaming_response_medical(self, async_client: AsyncWriter) -> None:
        async with async_client.tools.comprehend.with_streaming_response.medical(
            content="content",
            response_type="Entities",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comprehend = await response.parse()
            assert_matches_type(ComprehendMedicalResponse, comprehend, path=["response"])

        assert cast(Any, response.is_closed) is True
