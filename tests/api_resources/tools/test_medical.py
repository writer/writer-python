# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types.tools import MedicalCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedical:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Writer) -> None:
        medical = client.tools.medical.create(
            content="content",
            response_type="Entities",
        )
        assert_matches_type(MedicalCreateResponse, medical, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Writer) -> None:
        response = client.tools.medical.with_raw_response.create(
            content="content",
            response_type="Entities",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medical = response.parse()
        assert_matches_type(MedicalCreateResponse, medical, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Writer) -> None:
        with client.tools.medical.with_streaming_response.create(
            content="content",
            response_type="Entities",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medical = response.parse()
            assert_matches_type(MedicalCreateResponse, medical, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMedical:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncWriter) -> None:
        medical = await async_client.tools.medical.create(
            content="content",
            response_type="Entities",
        )
        assert_matches_type(MedicalCreateResponse, medical, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWriter) -> None:
        response = await async_client.tools.medical.with_raw_response.create(
            content="content",
            response_type="Entities",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        medical = await response.parse()
        assert_matches_type(MedicalCreateResponse, medical, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWriter) -> None:
        async with async_client.tools.medical.with_streaming_response.create(
            content="content",
            response_type="Entities",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            medical = await response.parse()
            assert_matches_type(MedicalCreateResponse, medical, path=["response"])

        assert cast(Any, response.is_closed) is True
