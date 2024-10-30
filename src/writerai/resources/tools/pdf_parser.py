# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.tools import pdf_parser_parse_params
from ..._base_client import make_request_options
from ...types.tools.pdf_parser_parse_response import PdfParserParseResponse

__all__ = ["PdfParserResource", "AsyncPdfParserResource"]


class PdfParserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PdfParserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return PdfParserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PdfParserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return PdfParserResourceWithStreamingResponse(self)

    def parse(
        self,
        file_id: str,
        *,
        format: Literal["text", "markdown"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PdfParserParseResponse:
        """
        Parse PDF to other formats.

        Args:
          format: The format into which the PDF content should be converted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._post(
            f"/v1/tools/pdf-parser/{file_id}",
            body=maybe_transform({"format": format}, pdf_parser_parse_params.PdfParserParseParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PdfParserParseResponse,
        )


class AsyncPdfParserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPdfParserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPdfParserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPdfParserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return AsyncPdfParserResourceWithStreamingResponse(self)

    async def parse(
        self,
        file_id: str,
        *,
        format: Literal["text", "markdown"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PdfParserParseResponse:
        """
        Parse PDF to other formats.

        Args:
          format: The format into which the PDF content should be converted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._post(
            f"/v1/tools/pdf-parser/{file_id}",
            body=await async_maybe_transform({"format": format}, pdf_parser_parse_params.PdfParserParseParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PdfParserParseResponse,
        )


class PdfParserResourceWithRawResponse:
    def __init__(self, pdf_parser: PdfParserResource) -> None:
        self._pdf_parser = pdf_parser

        self.parse = to_raw_response_wrapper(
            pdf_parser.parse,
        )


class AsyncPdfParserResourceWithRawResponse:
    def __init__(self, pdf_parser: AsyncPdfParserResource) -> None:
        self._pdf_parser = pdf_parser

        self.parse = async_to_raw_response_wrapper(
            pdf_parser.parse,
        )


class PdfParserResourceWithStreamingResponse:
    def __init__(self, pdf_parser: PdfParserResource) -> None:
        self._pdf_parser = pdf_parser

        self.parse = to_streamed_response_wrapper(
            pdf_parser.parse,
        )


class AsyncPdfParserResourceWithStreamingResponse:
    def __init__(self, pdf_parser: AsyncPdfParserResource) -> None:
        self._pdf_parser = pdf_parser

        self.parse = async_to_streamed_response_wrapper(
            pdf_parser.parse,
        )
