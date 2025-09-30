# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Union
from typing_extensions import Literal

import httpx

from ...types import (
    tool_ai_detect_params,
    tool_parse_pdf_params,
    tool_web_search_params,
    tool_context_aware_splitting_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.tool_ai_detect_response import ToolAIDetectResponse
from ...types.tool_parse_pdf_response import ToolParsePdfResponse
from ...types.tool_web_search_response import ToolWebSearchResponse
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

    @typing_extensions.deprecated(
        "Will be removed in a future release. Please migrate to alternative solutions. See documentation at dev.writer.com for more information."
    )
    def ai_detect(
        self,
        *,
        input: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolAIDetectResponse:
        """Detects if content is AI- or human-generated, with a confidence score.

        Content
        must have at least 350 characters

        Args:
          input: The content to determine if it is AI- or human-generated. Content must have at
              least 350 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/ai-detect",
            body=maybe_transform({"input": input}, tool_ai_detect_params.ToolAIDetectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolAIDetectResponse,
        )

    @typing_extensions.deprecated(
        "Will be removed in a future release. Please migrate to alternative solutions. See documentation at dev.writer.com for more information."
    )
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolContextAwareSplittingResponse:
        """
        Splits a long block of text (maximum 4000 words) into smaller chunks while
        preserving the semantic meaning of the text and context between the chunks.

        Args:
          strategy: The strategy to use for splitting the text into chunks. `llm_split` uses the
              language model to split the text, `fast_split` uses a fast heuristic-based
              approach, and `hybrid_split` combines both strategies.

          text: The text to split into chunks.

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

    @typing_extensions.deprecated(
        "Will be removed in a future release. A replacement PDF parsing tool for chat completions is planned; see documentation at dev.writer.com for more information."
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @typing_extensions.deprecated(
        "Will be removed in a future release. Migrate to `chat.chat` with the web search tool for web search capabilities. See documentation at dev.writer.com for more information."
    )
    def web_search(
        self,
        *,
        chunks_per_source: int | Omit = omit,
        country: Literal[
            "afghanistan",
            "albania",
            "algeria",
            "andorra",
            "angola",
            "argentina",
            "armenia",
            "australia",
            "austria",
            "azerbaijan",
            "bahamas",
            "bahrain",
            "bangladesh",
            "barbados",
            "belarus",
            "belgium",
            "belize",
            "benin",
            "bhutan",
            "bolivia",
            "bosnia and herzegovina",
            "botswana",
            "brazil",
            "brunei",
            "bulgaria",
            "burkina faso",
            "burundi",
            "cambodia",
            "cameroon",
            "canada",
            "cape verde",
            "central african republic",
            "chad",
            "chile",
            "china",
            "colombia",
            "comoros",
            "congo",
            "costa rica",
            "croatia",
            "cuba",
            "cyprus",
            "czech republic",
            "denmark",
            "djibouti",
            "dominican republic",
            "ecuador",
            "egypt",
            "el salvador",
            "equatorial guinea",
            "eritrea",
            "estonia",
            "ethiopia",
            "fiji",
            "finland",
            "france",
            "gabon",
            "gambia",
            "georgia",
            "germany",
            "ghana",
            "greece",
            "guatemala",
            "guinea",
            "haiti",
            "honduras",
            "hungary",
            "iceland",
            "india",
            "indonesia",
            "iran",
            "iraq",
            "ireland",
            "israel",
            "italy",
            "jamaica",
            "japan",
            "jordan",
            "kazakhstan",
            "kenya",
            "kuwait",
            "kyrgyzstan",
            "latvia",
            "lebanon",
            "lesotho",
            "liberia",
            "libya",
            "liechtenstein",
            "lithuania",
            "luxembourg",
            "madagascar",
            "malawi",
            "malaysia",
            "maldives",
            "mali",
            "malta",
            "mauritania",
            "mauritius",
            "mexico",
            "moldova",
            "monaco",
            "mongolia",
            "montenegro",
            "morocco",
            "mozambique",
            "myanmar",
            "namibia",
            "nepal",
            "netherlands",
            "new zealand",
            "nicaragua",
            "niger",
            "nigeria",
            "north korea",
            "north macedonia",
            "norway",
            "oman",
            "pakistan",
            "panama",
            "papua new guinea",
            "paraguay",
            "peru",
            "philippines",
            "poland",
            "portugal",
            "qatar",
            "romania",
            "russia",
            "rwanda",
            "saudi arabia",
            "senegal",
            "serbia",
            "singapore",
            "slovakia",
            "slovenia",
            "somalia",
            "south africa",
            "south korea",
            "south sudan",
            "spain",
            "sri lanka",
            "sudan",
            "sweden",
            "switzerland",
            "syria",
            "taiwan",
            "tajikistan",
            "tanzania",
            "thailand",
            "togo",
            "trinidad and tobago",
            "tunisia",
            "turkey",
            "turkmenistan",
            "uganda",
            "ukraine",
            "united arab emirates",
            "united kingdom",
            "united states",
            "uruguay",
            "uzbekistan",
            "venezuela",
            "vietnam",
            "yemen",
            "zambia",
            "zimbabwe",
        ]
        | Omit = omit,
        days: int | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        include_answer: bool | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        include_raw_content: Union[Literal["text", "markdown"], bool] | Omit = omit,
        max_results: int | Omit = omit,
        query: str | Omit = omit,
        search_depth: Literal["basic", "advanced"] | Omit = omit,
        stream: bool | Omit = omit,
        time_range: Literal["day", "week", "month", "year", "d", "w", "m", "y"] | Omit = omit,
        topic: Literal["general", "news"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolWebSearchResponse:
        """
        Search the web for information about a given query and return relevant results
        with source URLs.

        Args:
          chunks_per_source: Only applies when `search_depth` is `advanced`. Specifies how many text segments
              to extract from each source. Limited to 3 chunks maximum.

          country: Localizes search results to a specific country. Only applies to general topic
              searches.

          days: For news topic searches, specifies how many days of news coverage to include.

          exclude_domains: Domains to exclude from the search. If unset, the search includes all domains.

          include_answer: Whether to include a generated answer to the query in the response. If `false`,
              only search results are returned.

          include_domains: Domains to include in the search. If unset, the search includes all domains.

          include_raw_content:
              Controls how raw content is included in search results:

              - `text`: Returns plain text without formatting markup
              - `markdown`: Returns structured content with markdown formatting (headers,
                links, bold text)
              - `true`: Same as `markdown`
              - `false`: Raw content is not included (default if unset)

          max_results: Limits the number of search results returned. Cannot exceed 20 sources.

          query: The search query.

          search_depth:
              Controls search comprehensiveness:

              - `basic`: Returns fewer but highly relevant results
              - `advanced`: Performs a deeper search with more results

          stream: Enables streaming of search results as they become available.

          time_range: Filters results to content published within the specified time range back from
              the current date. For example, `week` or `w` returns results from the past 7
              days.

          topic: The search topic category. Use `news` for current events and news articles, or
              `general` for broader web search.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/web-search",
            body=maybe_transform(
                {
                    "chunks_per_source": chunks_per_source,
                    "country": country,
                    "days": days,
                    "exclude_domains": exclude_domains,
                    "include_answer": include_answer,
                    "include_domains": include_domains,
                    "include_raw_content": include_raw_content,
                    "max_results": max_results,
                    "query": query,
                    "search_depth": search_depth,
                    "stream": stream,
                    "time_range": time_range,
                    "topic": topic,
                },
                tool_web_search_params.ToolWebSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolWebSearchResponse,
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

    @typing_extensions.deprecated(
        "Will be removed in a future release. Please migrate to alternative solutions. See documentation at dev.writer.com for more information."
    )
    async def ai_detect(
        self,
        *,
        input: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolAIDetectResponse:
        """Detects if content is AI- or human-generated, with a confidence score.

        Content
        must have at least 350 characters

        Args:
          input: The content to determine if it is AI- or human-generated. Content must have at
              least 350 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/ai-detect",
            body=await async_maybe_transform({"input": input}, tool_ai_detect_params.ToolAIDetectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolAIDetectResponse,
        )

    @typing_extensions.deprecated(
        "Will be removed in a future release. Please migrate to alternative solutions. See documentation at dev.writer.com for more information."
    )
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolContextAwareSplittingResponse:
        """
        Splits a long block of text (maximum 4000 words) into smaller chunks while
        preserving the semantic meaning of the text and context between the chunks.

        Args:
          strategy: The strategy to use for splitting the text into chunks. `llm_split` uses the
              language model to split the text, `fast_split` uses a fast heuristic-based
              approach, and `hybrid_split` combines both strategies.

          text: The text to split into chunks.

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

    @typing_extensions.deprecated(
        "Will be removed in a future release. A replacement PDF parsing tool for chat completions is planned; see documentation at dev.writer.com for more information."
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    @typing_extensions.deprecated(
        "Will be removed in a future release. Migrate to `chat.chat` with the web search tool for web search capabilities. See documentation at dev.writer.com for more information."
    )
    async def web_search(
        self,
        *,
        chunks_per_source: int | Omit = omit,
        country: Literal[
            "afghanistan",
            "albania",
            "algeria",
            "andorra",
            "angola",
            "argentina",
            "armenia",
            "australia",
            "austria",
            "azerbaijan",
            "bahamas",
            "bahrain",
            "bangladesh",
            "barbados",
            "belarus",
            "belgium",
            "belize",
            "benin",
            "bhutan",
            "bolivia",
            "bosnia and herzegovina",
            "botswana",
            "brazil",
            "brunei",
            "bulgaria",
            "burkina faso",
            "burundi",
            "cambodia",
            "cameroon",
            "canada",
            "cape verde",
            "central african republic",
            "chad",
            "chile",
            "china",
            "colombia",
            "comoros",
            "congo",
            "costa rica",
            "croatia",
            "cuba",
            "cyprus",
            "czech republic",
            "denmark",
            "djibouti",
            "dominican republic",
            "ecuador",
            "egypt",
            "el salvador",
            "equatorial guinea",
            "eritrea",
            "estonia",
            "ethiopia",
            "fiji",
            "finland",
            "france",
            "gabon",
            "gambia",
            "georgia",
            "germany",
            "ghana",
            "greece",
            "guatemala",
            "guinea",
            "haiti",
            "honduras",
            "hungary",
            "iceland",
            "india",
            "indonesia",
            "iran",
            "iraq",
            "ireland",
            "israel",
            "italy",
            "jamaica",
            "japan",
            "jordan",
            "kazakhstan",
            "kenya",
            "kuwait",
            "kyrgyzstan",
            "latvia",
            "lebanon",
            "lesotho",
            "liberia",
            "libya",
            "liechtenstein",
            "lithuania",
            "luxembourg",
            "madagascar",
            "malawi",
            "malaysia",
            "maldives",
            "mali",
            "malta",
            "mauritania",
            "mauritius",
            "mexico",
            "moldova",
            "monaco",
            "mongolia",
            "montenegro",
            "morocco",
            "mozambique",
            "myanmar",
            "namibia",
            "nepal",
            "netherlands",
            "new zealand",
            "nicaragua",
            "niger",
            "nigeria",
            "north korea",
            "north macedonia",
            "norway",
            "oman",
            "pakistan",
            "panama",
            "papua new guinea",
            "paraguay",
            "peru",
            "philippines",
            "poland",
            "portugal",
            "qatar",
            "romania",
            "russia",
            "rwanda",
            "saudi arabia",
            "senegal",
            "serbia",
            "singapore",
            "slovakia",
            "slovenia",
            "somalia",
            "south africa",
            "south korea",
            "south sudan",
            "spain",
            "sri lanka",
            "sudan",
            "sweden",
            "switzerland",
            "syria",
            "taiwan",
            "tajikistan",
            "tanzania",
            "thailand",
            "togo",
            "trinidad and tobago",
            "tunisia",
            "turkey",
            "turkmenistan",
            "uganda",
            "ukraine",
            "united arab emirates",
            "united kingdom",
            "united states",
            "uruguay",
            "uzbekistan",
            "venezuela",
            "vietnam",
            "yemen",
            "zambia",
            "zimbabwe",
        ]
        | Omit = omit,
        days: int | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        include_answer: bool | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        include_raw_content: Union[Literal["text", "markdown"], bool] | Omit = omit,
        max_results: int | Omit = omit,
        query: str | Omit = omit,
        search_depth: Literal["basic", "advanced"] | Omit = omit,
        stream: bool | Omit = omit,
        time_range: Literal["day", "week", "month", "year", "d", "w", "m", "y"] | Omit = omit,
        topic: Literal["general", "news"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolWebSearchResponse:
        """
        Search the web for information about a given query and return relevant results
        with source URLs.

        Args:
          chunks_per_source: Only applies when `search_depth` is `advanced`. Specifies how many text segments
              to extract from each source. Limited to 3 chunks maximum.

          country: Localizes search results to a specific country. Only applies to general topic
              searches.

          days: For news topic searches, specifies how many days of news coverage to include.

          exclude_domains: Domains to exclude from the search. If unset, the search includes all domains.

          include_answer: Whether to include a generated answer to the query in the response. If `false`,
              only search results are returned.

          include_domains: Domains to include in the search. If unset, the search includes all domains.

          include_raw_content:
              Controls how raw content is included in search results:

              - `text`: Returns plain text without formatting markup
              - `markdown`: Returns structured content with markdown formatting (headers,
                links, bold text)
              - `true`: Same as `markdown`
              - `false`: Raw content is not included (default if unset)

          max_results: Limits the number of search results returned. Cannot exceed 20 sources.

          query: The search query.

          search_depth:
              Controls search comprehensiveness:

              - `basic`: Returns fewer but highly relevant results
              - `advanced`: Performs a deeper search with more results

          stream: Enables streaming of search results as they become available.

          time_range: Filters results to content published within the specified time range back from
              the current date. For example, `week` or `w` returns results from the past 7
              days.

          topic: The search topic category. Use `news` for current events and news articles, or
              `general` for broader web search.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/web-search",
            body=await async_maybe_transform(
                {
                    "chunks_per_source": chunks_per_source,
                    "country": country,
                    "days": days,
                    "exclude_domains": exclude_domains,
                    "include_answer": include_answer,
                    "include_domains": include_domains,
                    "include_raw_content": include_raw_content,
                    "max_results": max_results,
                    "query": query,
                    "search_depth": search_depth,
                    "stream": stream,
                    "time_range": time_range,
                    "topic": topic,
                },
                tool_web_search_params.ToolWebSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolWebSearchResponse,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.ai_detect = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                tools.ai_detect,  # pyright: ignore[reportDeprecated],
            )
        )
        self.context_aware_splitting = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                tools.context_aware_splitting,  # pyright: ignore[reportDeprecated],
            )
        )
        self.parse_pdf = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                tools.parse_pdf,  # pyright: ignore[reportDeprecated],
            )
        )
        self.web_search = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                tools.web_search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def comprehend(self) -> ComprehendResourceWithRawResponse:
        return ComprehendResourceWithRawResponse(self._tools.comprehend)


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.ai_detect = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                tools.ai_detect,  # pyright: ignore[reportDeprecated],
            )
        )
        self.context_aware_splitting = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                tools.context_aware_splitting,  # pyright: ignore[reportDeprecated],
            )
        )
        self.parse_pdf = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                tools.parse_pdf,  # pyright: ignore[reportDeprecated],
            )
        )
        self.web_search = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                tools.web_search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def comprehend(self) -> AsyncComprehendResourceWithRawResponse:
        return AsyncComprehendResourceWithRawResponse(self._tools.comprehend)


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.ai_detect = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                tools.ai_detect,  # pyright: ignore[reportDeprecated],
            )
        )
        self.context_aware_splitting = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                tools.context_aware_splitting,  # pyright: ignore[reportDeprecated],
            )
        )
        self.parse_pdf = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                tools.parse_pdf,  # pyright: ignore[reportDeprecated],
            )
        )
        self.web_search = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                tools.web_search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def comprehend(self) -> ComprehendResourceWithStreamingResponse:
        return ComprehendResourceWithStreamingResponse(self._tools.comprehend)


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.ai_detect = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                tools.ai_detect,  # pyright: ignore[reportDeprecated],
            )
        )
        self.context_aware_splitting = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                tools.context_aware_splitting,  # pyright: ignore[reportDeprecated],
            )
        )
        self.parse_pdf = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                tools.parse_pdf,  # pyright: ignore[reportDeprecated],
            )
        )
        self.web_search = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                tools.web_search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def comprehend(self) -> AsyncComprehendResourceWithStreamingResponse:
        return AsyncComprehendResourceWithStreamingResponse(self._tools.comprehend)
