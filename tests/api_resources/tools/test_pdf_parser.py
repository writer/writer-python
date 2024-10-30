# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types.tools import PdfParserParseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPdfParser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_parse(self, client: Writer) -> None:
        pdf_parser = client.tools.pdf_parser.parse(
            file_id="file_id",
            format="text",
        )
        assert_matches_type(PdfParserParseResponse, pdf_parser, path=["response"])

    @parametrize
    def test_raw_response_parse(self, client: Writer) -> None:
        response = client.tools.pdf_parser.with_raw_response.parse(
            file_id="file_id",
            format="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pdf_parser = response.parse()
        assert_matches_type(PdfParserParseResponse, pdf_parser, path=["response"])

    @parametrize
    def test_streaming_response_parse(self, client: Writer) -> None:
        with client.tools.pdf_parser.with_streaming_response.parse(
            file_id="file_id",
            format="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pdf_parser = response.parse()
            assert_matches_type(PdfParserParseResponse, pdf_parser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_parse(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.tools.pdf_parser.with_raw_response.parse(
                file_id="",
                format="text",
            )


class TestAsyncPdfParser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_parse(self, async_client: AsyncWriter) -> None:
        pdf_parser = await async_client.tools.pdf_parser.parse(
            file_id="file_id",
            format="text",
        )
        assert_matches_type(PdfParserParseResponse, pdf_parser, path=["response"])

    @parametrize
    async def test_raw_response_parse(self, async_client: AsyncWriter) -> None:
        response = await async_client.tools.pdf_parser.with_raw_response.parse(
            file_id="file_id",
            format="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pdf_parser = await response.parse()
        assert_matches_type(PdfParserParseResponse, pdf_parser, path=["response"])

    @parametrize
    async def test_streaming_response_parse(self, async_client: AsyncWriter) -> None:
        async with async_client.tools.pdf_parser.with_streaming_response.parse(
            file_id="file_id",
            format="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pdf_parser = await response.parse()
            assert_matches_type(PdfParserParseResponse, pdf_parser, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_parse(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.tools.pdf_parser.with_raw_response.parse(
                file_id="",
                format="text",
            )
