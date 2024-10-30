# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import tool_context_aware_splitting_params
from .medical import (
    MedicalResource,
    AsyncMedicalResource,
    MedicalResourceWithRawResponse,
    AsyncMedicalResourceWithRawResponse,
    MedicalResourceWithStreamingResponse,
    AsyncMedicalResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .pdf_parser import (
    PdfParserResource,
    AsyncPdfParserResource,
    PdfParserResourceWithRawResponse,
    AsyncPdfParserResourceWithRawResponse,
    PdfParserResourceWithStreamingResponse,
    AsyncPdfParserResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.tool_context_aware_splitting_response import ToolContextAwareSplittingResponse

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def medical(self) -> MedicalResource:
        return MedicalResource(self._client)

    @cached_property
    def pdf_parser(self) -> PdfParserResource:
        return PdfParserResource(self._client)

    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def context_aware_splitting(
        self,
        *,
        strategy: Literal["llm_split", "fast_split", "hybrid_split"],
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolContextAwareSplittingResponse:
        """
        Splits a long block of text (maximum 4000 words) into smaller chunks while
        preserving the semantic meaning of the text and context between the chunks.

        Args:
          strategy: The strategy to be used for splitting the text into chunks. `llm_split` uses the
              language model to split the text, `fast_split` uses a fast heuristic-based
              approach, and `hybrid_split` combines both strategies.

          text: The text to be split into chunks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/context-aware-splitting",
            body=maybe_transform(
                {
                    "strategy": strategy,
                    "text": text,
                },
                tool_context_aware_splitting_params.ToolContextAwareSplittingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolContextAwareSplittingResponse,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def medical(self) -> AsyncMedicalResource:
        return AsyncMedicalResource(self._client)

    @cached_property
    def pdf_parser(self) -> AsyncPdfParserResource:
        return AsyncPdfParserResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    async def context_aware_splitting(
        self,
        *,
        strategy: Literal["llm_split", "fast_split", "hybrid_split"],
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolContextAwareSplittingResponse:
        """
        Splits a long block of text (maximum 4000 words) into smaller chunks while
        preserving the semantic meaning of the text and context between the chunks.

        Args:
          strategy: The strategy to be used for splitting the text into chunks. `llm_split` uses the
              language model to split the text, `fast_split` uses a fast heuristic-based
              approach, and `hybrid_split` combines both strategies.

          text: The text to be split into chunks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/context-aware-splitting",
            body=await async_maybe_transform(
                {
                    "strategy": strategy,
                    "text": text,
                },
                tool_context_aware_splitting_params.ToolContextAwareSplittingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolContextAwareSplittingResponse,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.context_aware_splitting = to_raw_response_wrapper(
            tools.context_aware_splitting,
        )

    @cached_property
    def medical(self) -> MedicalResourceWithRawResponse:
        return MedicalResourceWithRawResponse(self._tools.medical)

    @cached_property
    def pdf_parser(self) -> PdfParserResourceWithRawResponse:
        return PdfParserResourceWithRawResponse(self._tools.pdf_parser)


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.context_aware_splitting = async_to_raw_response_wrapper(
            tools.context_aware_splitting,
        )

    @cached_property
    def medical(self) -> AsyncMedicalResourceWithRawResponse:
        return AsyncMedicalResourceWithRawResponse(self._tools.medical)

    @cached_property
    def pdf_parser(self) -> AsyncPdfParserResourceWithRawResponse:
        return AsyncPdfParserResourceWithRawResponse(self._tools.pdf_parser)


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.context_aware_splitting = to_streamed_response_wrapper(
            tools.context_aware_splitting,
        )

    @cached_property
    def medical(self) -> MedicalResourceWithStreamingResponse:
        return MedicalResourceWithStreamingResponse(self._tools.medical)

    @cached_property
    def pdf_parser(self) -> PdfParserResourceWithStreamingResponse:
        return PdfParserResourceWithStreamingResponse(self._tools.pdf_parser)


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.context_aware_splitting = async_to_streamed_response_wrapper(
            tools.context_aware_splitting,
        )

    @cached_property
    def medical(self) -> AsyncMedicalResourceWithStreamingResponse:
        return AsyncMedicalResourceWithStreamingResponse(self._tools.medical)

    @cached_property
    def pdf_parser(self) -> AsyncPdfParserResourceWithStreamingResponse:
        return AsyncPdfParserResourceWithStreamingResponse(self._tools.pdf_parser)
