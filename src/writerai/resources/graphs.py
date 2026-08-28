# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import (
    graph_list_params,
    graph_create_params,
    graph_update_params,
    graph_question_params,
    graph_add_file_to_graph_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import path_template, required_args, maybe_transform, async_maybe_transform
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
        description: str | Omit = omit,
        name: str | Omit = omit,
        team_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphCreateResponse:
        """
        Create a new Knowledge Graph.

        By default, the new Knowledge Graph is org-wide (accessible to every team in the
        organization). To deploy the Knowledge Graph to specific teams instead, provide
        a `team_ids` array in the request body. When the request is authenticated with a
        team-scoped API key, the new Knowledge Graph is automatically assigned to that
        key's team and `team_ids` in the body is not accepted.

        Args:
          description: A description of the Knowledge Graph (max 255 characters). Omitting this field
              leaves the description unchanged.

          name: The name of the Knowledge Graph (max 255 characters). Omitting this field leaves
              the name unchanged.

          team_ids: Optional list of team IDs to deploy the Knowledge Graph to. Omit the field or
              pass an empty array to create an org-wide Knowledge Graph (accessible to every
              team in the organization), which is the default. Provide one or more team IDs to
              scope the Knowledge Graph to those teams. Only applies when using an org-scoped
              API key; requests made with a team-scoped API key ignore this field and always
              assign the graph to that key's team.

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
                    "team_ids": team_ids,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/graphs/{graph_id}", graph_id=graph_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Graph,
        )

    def update(
        self,
        graph_id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        team_ids: Iterable[int] | Omit = omit,
        urls: Iterable[graph_update_params.URL] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphUpdateResponse:
        """
        Update the name, description, web connector URLs, or team assignment of a
        Knowledge Graph.

        Including a `team_ids` array replaces the whole team assignment: an empty array
        makes the Knowledge Graph org-wide, one or more team IDs scope it to exactly
        those teams. Omitting `team_ids` leaves the current team assignment unchanged.
        Team-scoped API keys cannot change the team assignment of a Knowledge Graph.

        Args:
          description: A description of the Knowledge Graph (max 255 characters). Omitting this field
              leaves the description unchanged.

          name: The name of the Knowledge Graph (max 255 characters). Omitting this field leaves
              the name unchanged.

          team_ids: Optional list of team IDs the Knowledge Graph is deployed to. Omitting this
              field leaves the current team assignment unchanged. Passing an array replaces
              the whole team assignment: an empty array makes the graph org-wide, one or more
              team IDs scope it to exactly those teams. Not accepted from team-scoped API
              keys.

          urls: An array of web connector URLs to update for this Knowledge Graph. You can only
              connect URLs to Knowledge Graphs with the type `web`. To clear the list of URLs,
              set this field to an empty array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        return self._put(
            path_template("/v1/graphs/{graph_id}", graph_id=graph_id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "team_ids": team_ids,
                    "urls": urls,
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
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        team_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Graph]:
        """
        Retrieve a list of Knowledge Graphs.

        By default, the response contains only org-wide Knowledge Graphs. To include
        Knowledge Graphs that are deployed to specific teams, pass one or more team IDs
        in the `team_ids` query parameter. Requests authenticated with a team-scoped API
        key always return only that key's team; passing a different value in `team_ids`
        is rejected.

        Args:
          after: The ID of the last object in the previous page. This parameter instructs the API
              to return the next page of results.

          before: The ID of the first object in the previous page. This parameter instructs the
              API to return the previous page of results.

          limit: Specifies the maximum number of objects returned in a page. The default value
              is 50. The minimum value is 1, and the maximum value is 100.

          order: Specifies the order of the results. Valid values are asc for ascending and desc
              for descending.

          team_ids: Filter results to Knowledge Graphs deployed to any of the specified teams.
              Repeat the query parameter to pass multiple IDs (for example,
              `?team_ids=42&team_ids=43`). Omitting this parameter returns only org-wide
              Knowledge Graphs; Knowledge Graphs deployed to specific teams are excluded
              unless the caller opts them in via `team_ids`.

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
                        "team_ids": team_ids,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/graphs/{graph_id}", graph_id=graph_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """Add a file to a Knowledge Graph.

        Team access is inherited from the Knowledge
        Graph; the file itself does not carry team parameters.

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
            path_template("/v1/graphs/{graph_id}/file", graph_id=graph_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        graph_ids: SequenceNotStr[str],
        question: str,
        query_config: graph_question_params.QueryConfig | Omit = omit,
        stream: Literal[False] | Omit = omit,
        subqueries: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Question:
        """
        Ask a question to specified Knowledge Graphs.

        Args:
          graph_ids: The unique identifiers of the Knowledge Graphs to query.

          question: The question to answer using the Knowledge Graph.

          query_config: Configuration options for Knowledge Graph queries, including search parameters
              and citation settings.

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
        graph_ids: SequenceNotStr[str],
        question: str,
        stream: Literal[True],
        query_config: graph_question_params.QueryConfig | Omit = omit,
        subqueries: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[QuestionResponseChunk]:
        """
        Ask a question to specified Knowledge Graphs.

        Args:
          graph_ids: The unique identifiers of the Knowledge Graphs to query.

          question: The question to answer using the Knowledge Graph.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          query_config: Configuration options for Knowledge Graph queries, including search parameters
              and citation settings.

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
        graph_ids: SequenceNotStr[str],
        question: str,
        stream: bool,
        query_config: graph_question_params.QueryConfig | Omit = omit,
        subqueries: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Question | Stream[QuestionResponseChunk]:
        """
        Ask a question to specified Knowledge Graphs.

        Args:
          graph_ids: The unique identifiers of the Knowledge Graphs to query.

          question: The question to answer using the Knowledge Graph.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          query_config: Configuration options for Knowledge Graph queries, including search parameters
              and citation settings.

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
        graph_ids: SequenceNotStr[str],
        question: str,
        query_config: graph_question_params.QueryConfig | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        subqueries: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Question | Stream[QuestionResponseChunk]:
        return self._post(
            "/v1/graphs/question",
            body=maybe_transform(
                {
                    "graph_ids": graph_ids,
                    "question": question,
                    "query_config": query_config,
                    "stream": stream,
                    "subqueries": subqueries,
                },
                graph_question_params.GraphQuestionParamsStreaming
                if stream
                else graph_question_params.GraphQuestionParamsNonStreaming,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/graphs/{graph_id}/file/{file_id}", graph_id=graph_id, file_id=file_id),
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
        description: str | Omit = omit,
        name: str | Omit = omit,
        team_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphCreateResponse:
        """
        Create a new Knowledge Graph.

        By default, the new Knowledge Graph is org-wide (accessible to every team in the
        organization). To deploy the Knowledge Graph to specific teams instead, provide
        a `team_ids` array in the request body. When the request is authenticated with a
        team-scoped API key, the new Knowledge Graph is automatically assigned to that
        key's team and `team_ids` in the body is not accepted.

        Args:
          description: A description of the Knowledge Graph (max 255 characters). Omitting this field
              leaves the description unchanged.

          name: The name of the Knowledge Graph (max 255 characters). Omitting this field leaves
              the name unchanged.

          team_ids: Optional list of team IDs to deploy the Knowledge Graph to. Omit the field or
              pass an empty array to create an org-wide Knowledge Graph (accessible to every
              team in the organization), which is the default. Provide one or more team IDs to
              scope the Knowledge Graph to those teams. Only applies when using an org-scoped
              API key; requests made with a team-scoped API key ignore this field and always
              assign the graph to that key's team.

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
                    "team_ids": team_ids,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/graphs/{graph_id}", graph_id=graph_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Graph,
        )

    async def update(
        self,
        graph_id: str,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        team_ids: Iterable[int] | Omit = omit,
        urls: Iterable[graph_update_params.URL] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GraphUpdateResponse:
        """
        Update the name, description, web connector URLs, or team assignment of a
        Knowledge Graph.

        Including a `team_ids` array replaces the whole team assignment: an empty array
        makes the Knowledge Graph org-wide, one or more team IDs scope it to exactly
        those teams. Omitting `team_ids` leaves the current team assignment unchanged.
        Team-scoped API keys cannot change the team assignment of a Knowledge Graph.

        Args:
          description: A description of the Knowledge Graph (max 255 characters). Omitting this field
              leaves the description unchanged.

          name: The name of the Knowledge Graph (max 255 characters). Omitting this field leaves
              the name unchanged.

          team_ids: Optional list of team IDs the Knowledge Graph is deployed to. Omitting this
              field leaves the current team assignment unchanged. Passing an array replaces
              the whole team assignment: an empty array makes the graph org-wide, one or more
              team IDs scope it to exactly those teams. Not accepted from team-scoped API
              keys.

          urls: An array of web connector URLs to update for this Knowledge Graph. You can only
              connect URLs to Knowledge Graphs with the type `web`. To clear the list of URLs,
              set this field to an empty array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not graph_id:
            raise ValueError(f"Expected a non-empty value for `graph_id` but received {graph_id!r}")
        return await self._put(
            path_template("/v1/graphs/{graph_id}", graph_id=graph_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "team_ids": team_ids,
                    "urls": urls,
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
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        team_ids: Iterable[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Graph, AsyncCursorPage[Graph]]:
        """
        Retrieve a list of Knowledge Graphs.

        By default, the response contains only org-wide Knowledge Graphs. To include
        Knowledge Graphs that are deployed to specific teams, pass one or more team IDs
        in the `team_ids` query parameter. Requests authenticated with a team-scoped API
        key always return only that key's team; passing a different value in `team_ids`
        is rejected.

        Args:
          after: The ID of the last object in the previous page. This parameter instructs the API
              to return the next page of results.

          before: The ID of the first object in the previous page. This parameter instructs the
              API to return the previous page of results.

          limit: Specifies the maximum number of objects returned in a page. The default value
              is 50. The minimum value is 1, and the maximum value is 100.

          order: Specifies the order of the results. Valid values are asc for ascending and desc
              for descending.

          team_ids: Filter results to Knowledge Graphs deployed to any of the specified teams.
              Repeat the query parameter to pass multiple IDs (for example,
              `?team_ids=42&team_ids=43`). Omitting this parameter returns only org-wide
              Knowledge Graphs; Knowledge Graphs deployed to specific teams are excluded
              unless the caller opts them in via `team_ids`.

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
                        "team_ids": team_ids,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/graphs/{graph_id}", graph_id=graph_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """Add a file to a Knowledge Graph.

        Team access is inherited from the Knowledge
        Graph; the file itself does not carry team parameters.

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
            path_template("/v1/graphs/{graph_id}/file", graph_id=graph_id),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        graph_ids: SequenceNotStr[str],
        question: str,
        query_config: graph_question_params.QueryConfig | Omit = omit,
        stream: Literal[False] | Omit = omit,
        subqueries: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Question:
        """
        Ask a question to specified Knowledge Graphs.

        Args:
          graph_ids: The unique identifiers of the Knowledge Graphs to query.

          question: The question to answer using the Knowledge Graph.

          query_config: Configuration options for Knowledge Graph queries, including search parameters
              and citation settings.

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
        graph_ids: SequenceNotStr[str],
        question: str,
        stream: Literal[True],
        query_config: graph_question_params.QueryConfig | Omit = omit,
        subqueries: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[QuestionResponseChunk]:
        """
        Ask a question to specified Knowledge Graphs.

        Args:
          graph_ids: The unique identifiers of the Knowledge Graphs to query.

          question: The question to answer using the Knowledge Graph.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          query_config: Configuration options for Knowledge Graph queries, including search parameters
              and citation settings.

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
        graph_ids: SequenceNotStr[str],
        question: str,
        stream: bool,
        query_config: graph_question_params.QueryConfig | Omit = omit,
        subqueries: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Question | AsyncStream[QuestionResponseChunk]:
        """
        Ask a question to specified Knowledge Graphs.

        Args:
          graph_ids: The unique identifiers of the Knowledge Graphs to query.

          question: The question to answer using the Knowledge Graph.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          query_config: Configuration options for Knowledge Graph queries, including search parameters
              and citation settings.

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
        graph_ids: SequenceNotStr[str],
        question: str,
        query_config: graph_question_params.QueryConfig | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        subqueries: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Question | AsyncStream[QuestionResponseChunk]:
        return await self._post(
            "/v1/graphs/question",
            body=await async_maybe_transform(
                {
                    "graph_ids": graph_ids,
                    "question": question,
                    "query_config": query_config,
                    "stream": stream,
                    "subqueries": subqueries,
                },
                graph_question_params.GraphQuestionParamsStreaming
                if stream
                else graph_question_params.GraphQuestionParamsNonStreaming,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/graphs/{graph_id}/file/{file_id}", graph_id=graph_id, file_id=file_id),
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
