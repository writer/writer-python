# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    graph_list_params,
    graph_create_params,
    graph_update_params,
    graph_add_file_to_graph_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
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
from ..pagination import SyncCursorPage, AsyncCursorPage
from ..types.file import File
from ..types.graph import Graph
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ..types.graph_create_response import GraphCreateResponse
from ..types.graph_delete_response import GraphDeleteResponse
from ..types.graph_update_response import GraphUpdateResponse
from ..types.graph_remove_file_from_graph_response import GraphRemoveFileFromGraphResponse

__all__ = ["GraphsResource", "AsyncGraphsResource"]


class GraphsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GraphsResourceWithRawResponse:
        return GraphsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GraphsResourceWithStreamingResponse:
        return GraphsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/graphs",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
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
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphUpdateResponse:
        """
        Args:
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
                    "name": name,
                    "description": description,
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
        Args:
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
        Args:
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
        return AsyncGraphsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGraphsResourceWithStreamingResponse:
        return AsyncGraphsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphCreateResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/graphs",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
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
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GraphUpdateResponse:
        """
        Args:
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
                    "name": name,
                    "description": description,
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
        Args:
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
        Args:
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
        self.remove_file_from_graph = async_to_streamed_response_wrapper(
            graphs.remove_file_from_graph,
        )
