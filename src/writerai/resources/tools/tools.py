# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import tool_parse_pdf_params, tool_context_aware_splitting_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .comprehend import (
    ComprehendResource,
    AsyncComprehendResource,
    ComprehendResourceWithRawResponse,
    AsyncComprehendResourceWithRawResponse,
    ComprehendResourceWithStreamingResponse,
    AsyncComprehendResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.tool_parse_pdf_response import ToolParsePdfResponse
from ...types.tool_context_aware_splitting_response import ToolContextAwareSplittingResponse

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def comprehend(self) -> ComprehendResource:
        return ComprehendResource(self._client)

    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    def parse_pdf(
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
    ) -> ToolParsePdfResponse:
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
            body=maybe_transform({"format": format}, tool_parse_pdf_params.ToolParsePdfParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolParsePdfResponse,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def comprehend(self) -> AsyncComprehendResource:
        return AsyncComprehendResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    async def parse_pdf(
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
    ) -> ToolParsePdfResponse:
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
            body=await async_maybe_transform({"format": format}, tool_parse_pdf_params.ToolParsePdfParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolParsePdfResponse,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.context_aware_splitting = to_raw_response_wrapper(
            tools.context_aware_splitting,
        )
        self.parse_pdf = to_raw_response_wrapper(
            tools.parse_pdf,
        )

    @cached_property
    def comprehend(self) -> ComprehendResourceWithRawResponse:
        return ComprehendResourceWithRawResponse(self._tools.comprehend)


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.context_aware_splitting = async_to_raw_response_wrapper(
            tools.context_aware_splitting,
        )
        self.parse_pdf = async_to_raw_response_wrapper(
            tools.parse_pdf,
        )

    @cached_property
    def comprehend(self) -> AsyncComprehendResourceWithRawResponse:
        return AsyncComprehendResourceWithRawResponse(self._tools.comprehend)


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.context_aware_splitting = to_streamed_response_wrapper(
            tools.context_aware_splitting,
        )
        self.parse_pdf = to_streamed_response_wrapper(
            tools.parse_pdf,
        )

    @cached_property
    def comprehend(self) -> ComprehendResourceWithStreamingResponse:
        return ComprehendResourceWithStreamingResponse(self._tools.comprehend)


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.context_aware_splitting = async_to_streamed_response_wrapper(
            tools.context_aware_splitting,
        )
        self.parse_pdf = async_to_streamed_response_wrapper(
            tools.parse_pdf,
        )

    @cached_property
    def comprehend(self) -> AsyncComprehendResourceWithStreamingResponse:
        return AsyncComprehendResourceWithStreamingResponse(self._tools.comprehend)
