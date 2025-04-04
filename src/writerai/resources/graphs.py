# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, overload

import httpx

from ..types import (
    graph_list_params,
    graph_create_params,
    graph_update_params,
    graph_question_params,
    graph_add_file_to_graph_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes
from .._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from ..pagination import SyncCursorPage, AsyncCursorPage
from ..types.file import File
from ..types.graph import Graph
from .._base_client import AsyncPaginator, make_request_options
from ..types.question import Question
from ..types.graph_create_response import GraphCreateResponse
from ..types.graph_delete_response import GraphDeleteResponse
from ..types.graph_update_response import GraphUpdateResponse
from ..types.question_response_chunk import QuestionResponseChunk
from ..types.graph_remove_file_from_graph_response import GraphRemoveFileFromGraphResponse

__all__ = ["GraphsResource", "AsyncGraphsResource"]


class GraphsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GraphsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return GraphsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GraphsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return GraphsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphCreateResponse:
        """
        Create a new Knowledge Graph.

        Args:
          description: A description of the Knowledge Graph (max 255 characters). Omitting this field
              leaves the description unchanged.

          name: The name of the Knowledge Graph (max 255 characters). Omitting this field leaves
              the name unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/graphs",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                graph_create_params.GraphCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphCreateResponse,
        )

    def retrieve(
        self,
        graph_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Graph:
        """
        Retrieve a Knowledge Graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        return self._get(
            f"/v1/graphs/{graph_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Graph,
        )

    def update(
        self,
        graph_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphUpdateResponse:
        """
        Update the name and description of a Knowledge Graph.

        Args:
          description: A description of the Knowledge Graph (max 255 characters). Omitting this field
              leaves the description unchanged.

          name: The name of the Knowledge Graph (max 255 characters). Omitting this field leaves
              the name unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        return self._put(
            f"/v1/graphs/{graph_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                graph_update_params.GraphUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Graph]:
        """
        Retrieve a list of Knowledge Graphs.

        Args:
          after: The ID of the last object in the previous page. This parameter instructs the API
              to return the next page of results.

          before: The ID of the first object in the previous page. This parameter instructs the
              API to return the previous page of results.

          limit: Specifies the maximum number of objects returned in a page. The default value
              is 50. The minimum value is 1, and the maximum value is 100.

          order: Specifies the order of the results. Valid values are asc for ascending and desc
              for descending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/graphs",
            page=SyncCursorPage[Graph],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                    },
                    graph_list_params.GraphListParams,
                ),
            ),
            model=Graph,
        )

    def delete(
        self,
        graph_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphDeleteResponse:
        """
        Delete a Knowledge Graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        return self._delete(
            f"/v1/graphs/{graph_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphDeleteResponse,
        )

    def add_file_to_graph(
        self,
        graph_id: str,
        *,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> File:
        """
        Add a file to a Knowledge Graph.

        Args:
          file_id: The unique identifier of the file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        return self._post(
            f"/v1/graphs/{graph_id}/file",
            body=maybe_transform({"file_id": file_id}, graph_add_file_to_graph_params.GraphAddFileToGraphParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    def upload_and_add_file_to_graph(
        self,
        graph_id: str,
        *,
        content: FileTypes,
        content_disposition: str,
        content_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> File:
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        uploaded_file = self._client.files.upload(
            content=content,
            content_disposition=content_disposition,
            content_type=content_type,
            extra_body=extra_body,
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
        )
        return self.add_file_to_graph(
            graph_id=graph_id,
            file_id=uploaded_file.id,
            extra_body=extra_body,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    @overload
    def question(
        self,
        *,
        graph_ids: List[str],
        question: str,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        subqueries: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Question:
        """
        Ask a question to specified Knowledge Graphs.

        Args:
          graph_ids: The unique identifiers of the Knowledge Graphs to be queried.

          question: The question to be answered using the Knowledge Graph.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          subqueries: Specify whether to include subqueries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def question(
        self,
        *,
        graph_ids: List[str],
        question: str,
        stream: Literal[True],
        subqueries: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[QuestionResponseChunk]:
        """
        Ask a question to specified Knowledge Graphs.

        Args:
          graph_ids: The unique identifiers of the Knowledge Graphs to be queried.

          question: The question to be answered using the Knowledge Graph.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          subqueries: Specify whether to include subqueries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def question(
        self,
        *,
        graph_ids: List[str],
        question: str,
        stream: bool,
        subqueries: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Question | Stream[QuestionResponseChunk]:
        """
        Ask a question to specified Knowledge Graphs.

        Args:
          graph_ids: The unique identifiers of the Knowledge Graphs to be queried.

          question: The question to be answered using the Knowledge Graph.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          subqueries: Specify whether to include subqueries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["graph_ids", "question"], ["graph_ids", "question", "stream"])
    def question(
        self,
        *,
        graph_ids: List[str],
        question: str,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        subqueries: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Question | Stream[QuestionResponseChunk]:
        return self._post(
            "/v1/graphs/question",
            body=maybe_transform(
                {
                    "graph_ids": graph_ids,
                    "question": question,
                    "stream": stream,
                    "subqueries": subqueries,
                },
                graph_question_params.GraphQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Question,
            stream=stream or False,
            stream_cls=Stream[QuestionResponseChunk],
        )

    def remove_file_from_graph(
        self,
        file_id: str,
        *,
        graph_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphRemoveFileFromGraphResponse:
        """
        Remove a file from a Knowledge Graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._delete(
            f"/v1/graphs/{graph_id}/file/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphRemoveFileFromGraphResponse,
        )


class AsyncGraphsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGraphsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGraphsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGraphsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return AsyncGraphsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphCreateResponse:
        """
        Create a new Knowledge Graph.

        Args:
          description: A description of the Knowledge Graph (max 255 characters). Omitting this field
              leaves the description unchanged.

          name: The name of the Knowledge Graph (max 255 characters). Omitting this field leaves
              the name unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/graphs",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                graph_create_params.GraphCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphCreateResponse,
        )

    async def retrieve(
        self,
        graph_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Graph:
        """
        Retrieve a Knowledge Graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        return await self._get(
            f"/v1/graphs/{graph_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Graph,
        )

    async def update(
        self,
        graph_id: str,
        *,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphUpdateResponse:
        """
        Update the name and description of a Knowledge Graph.

        Args:
          description: A description of the Knowledge Graph (max 255 characters). Omitting this field
              leaves the description unchanged.

          name: The name of the Knowledge Graph (max 255 characters). Omitting this field leaves
              the name unchanged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        return await self._put(
            f"/v1/graphs/{graph_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                graph_update_params.GraphUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Graph, AsyncCursorPage[Graph]]:
        """
        Retrieve a list of Knowledge Graphs.

        Args:
          after: The ID of the last object in the previous page. This parameter instructs the API
              to return the next page of results.

          before: The ID of the first object in the previous page. This parameter instructs the
              API to return the previous page of results.

          limit: Specifies the maximum number of objects returned in a page. The default value
              is 50. The minimum value is 1, and the maximum value is 100.

          order: Specifies the order of the results. Valid values are asc for ascending and desc
              for descending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/graphs",
            page=AsyncCursorPage[Graph],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "order": order,
                    },
                    graph_list_params.GraphListParams,
                ),
            ),
            model=Graph,
        )

    async def delete(
        self,
        graph_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphDeleteResponse:
        """
        Delete a Knowledge Graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        return await self._delete(
            f"/v1/graphs/{graph_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphDeleteResponse,
        )

    async def add_file_to_graph(
        self,
        graph_id: str,
        *,
        file_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> File:
        """
        Add a file to a Knowledge Graph.

        Args:
          file_id: The unique identifier of the file.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        return await self._post(
            f"/v1/graphs/{graph_id}/file",
            body=await async_maybe_transform(
                {"file_id": file_id}, graph_add_file_to_graph_params.GraphAddFileToGraphParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    async def upload_and_add_file_to_graph(
        self,
        graph_id: str,
        *,
        content: FileTypes,
        content_disposition: str,
        content_type: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> File:
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        uploaded_file = await self._client.files.upload(
            content=content,
            content_disposition=content_disposition,
            content_type=content_type,
            extra_body=extra_body,
            extra_query=extra_query,
            extra_headers=extra_headers,
            timeout=timeout,
        )
        return await self.add_file_to_graph(
            graph_id=graph_id,
            file_id=uploaded_file.id,
            extra_body=extra_body,
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    @overload
    async def question(
        self,
        *,
        graph_ids: List[str],
        question: str,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        subqueries: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Question:
        """
        Ask a question to specified Knowledge Graphs.

        Args:
          graph_ids: The unique identifiers of the Knowledge Graphs to be queried.

          question: The question to be answered using the Knowledge Graph.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          subqueries: Specify whether to include subqueries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def question(
        self,
        *,
        graph_ids: List[str],
        question: str,
        stream: Literal[True],
        subqueries: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[QuestionResponseChunk]:
        """
        Ask a question to specified Knowledge Graphs.

        Args:
          graph_ids: The unique identifiers of the Knowledge Graphs to be queried.

          question: The question to be answered using the Knowledge Graph.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          subqueries: Specify whether to include subqueries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def question(
        self,
        *,
        graph_ids: List[str],
        question: str,
        stream: bool,
        subqueries: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Question | AsyncStream[QuestionResponseChunk]:
        """
        Ask a question to specified Knowledge Graphs.

        Args:
          graph_ids: The unique identifiers of the Knowledge Graphs to be queried.

          question: The question to be answered using the Knowledge Graph.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          subqueries: Specify whether to include subqueries.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["graph_ids", "question"], ["graph_ids", "question", "stream"])
    async def question(
        self,
        *,
        graph_ids: List[str],
        question: str,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        subqueries: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Question | AsyncStream[QuestionResponseChunk]:
        return await self._post(
            "/v1/graphs/question",
            body=await async_maybe_transform(
                {
                    "graph_ids": graph_ids,
                    "question": question,
                    "stream": stream,
                    "subqueries": subqueries,
                },
                graph_question_params.GraphQuestionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Question,
            stream=stream or False,
            stream_cls=AsyncStream[QuestionResponseChunk],
        )

    async def remove_file_from_graph(
        self,
        file_id: str,
        *,
        graph_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphRemoveFileFromGraphResponse:
        """
        Remove a file from a Knowledge Graph.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._delete(
            f"/v1/graphs/{graph_id}/file/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GraphRemoveFileFromGraphResponse,
        )


class GraphsResourceWithRawResponse:
    def __init__(self, graphs: GraphsResource) -> None:
        self._graphs = graphs

        self.create = to_raw_response_wrapper(
            graphs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            graphs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            graphs.update,
        )
        self.list = to_raw_response_wrapper(
            graphs.list,
        )
        self.delete = to_raw_response_wrapper(
            graphs.delete,
        )
        self.add_file_to_graph = to_raw_response_wrapper(
            graphs.add_file_to_graph,
        )
        self.upload_and_add_file_to_graph = to_raw_response_wrapper(
            graphs.upload_and_add_file_to_graph,
        )
        self.question = to_raw_response_wrapper(
            graphs.question,
        )
        self.remove_file_from_graph = to_raw_response_wrapper(
            graphs.remove_file_from_graph,
        )


class AsyncGraphsResourceWithRawResponse:
    def __init__(self, graphs: AsyncGraphsResource) -> None:
        self._graphs = graphs

        self.create = async_to_raw_response_wrapper(
            graphs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            graphs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            graphs.update,
        )
        self.list = async_to_raw_response_wrapper(
            graphs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            graphs.delete,
        )
        self.add_file_to_graph = async_to_raw_response_wrapper(
            graphs.add_file_to_graph,
        )
        self.upload_and_add_file_to_graph = async_to_raw_response_wrapper(
            graphs.upload_and_add_file_to_graph,
        )
        self.question = async_to_raw_response_wrapper(
            graphs.question,
        )
        self.remove_file_from_graph = async_to_raw_response_wrapper(
            graphs.remove_file_from_graph,
        )


class GraphsResourceWithStreamingResponse:
    def __init__(self, graphs: GraphsResource) -> None:
        self._graphs = graphs

        self.create = to_streamed_response_wrapper(
            graphs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            graphs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            graphs.update,
        )
        self.list = to_streamed_response_wrapper(
            graphs.list,
        )
        self.delete = to_streamed_response_wrapper(
            graphs.delete,
        )
        self.add_file_to_graph = to_streamed_response_wrapper(
            graphs.add_file_to_graph,
        )
        self.upload_and_add_file_to_graph = to_streamed_response_wrapper(
            graphs.upload_and_add_file_to_graph,
        )
        self.question = to_streamed_response_wrapper(
            graphs.question,
        )
        self.remove_file_from_graph = to_streamed_response_wrapper(
            graphs.remove_file_from_graph,
        )


class AsyncGraphsResourceWithStreamingResponse:
    def __init__(self, graphs: AsyncGraphsResource) -> None:
        self._graphs = graphs

        self.create = async_to_streamed_response_wrapper(
            graphs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            graphs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            graphs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            graphs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            graphs.delete,
        )
        self.add_file_to_graph = async_to_streamed_response_wrapper(
            graphs.add_file_to_graph,
        )
        self.upload_and_add_file_to_graph = async_to_streamed_response_wrapper(
            graphs.upload_and_add_file_to_graph,
        )
        self.question = async_to_streamed_response_wrapper(
            graphs.question,
        )
        self.remove_file_from_graph = async_to_streamed_response_wrapper(
            graphs.remove_file_from_graph,
        )
