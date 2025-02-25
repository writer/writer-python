# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

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
from ..._base_client import make_request_options
from ...types.applications import graph_update_params
from ...types.applications.application_graphs_response import ApplicationGraphsResponse

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

    def update(
        self,
        application_id: str,
        *,
        graph_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationGraphsResponse:
        """
        Updates the Knowledge Graphs listed and associates them with the no-code chat
        app to be used.

        Args:
          graph_ids: A list of Knowledge Graph IDs to associate with the application. Note that this
              will replace the existing list of Knowledge Graphs associated with the
              application, not add to it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._put(
            f"/v1/applications/{application_id}/graphs",
            body=maybe_transform({"graph_ids": graph_ids}, graph_update_params.GraphUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplicationGraphsResponse,
        )

    def list(
        self,
        application_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationGraphsResponse:
        """
        Retrieve Knowledge Graphs associated with a no-code chat application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._get(
            f"/v1/applications/{application_id}/graphs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplicationGraphsResponse,
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

    async def update(
        self,
        application_id: str,
        *,
        graph_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationGraphsResponse:
        """
        Updates the Knowledge Graphs listed and associates them with the no-code chat
        app to be used.

        Args:
          graph_ids: A list of Knowledge Graph IDs to associate with the application. Note that this
              will replace the existing list of Knowledge Graphs associated with the
              application, not add to it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._put(
            f"/v1/applications/{application_id}/graphs",
            body=await async_maybe_transform({"graph_ids": graph_ids}, graph_update_params.GraphUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplicationGraphsResponse,
        )

    async def list(
        self,
        application_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationGraphsResponse:
        """
        Retrieve Knowledge Graphs associated with a no-code chat application.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._get(
            f"/v1/applications/{application_id}/graphs",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplicationGraphsResponse,
        )


class GraphsResourceWithRawResponse:
    def __init__(self, graphs: GraphsResource) -> None:
        self._graphs = graphs

        self.update = to_raw_response_wrapper(
            graphs.update,
        )
        self.list = to_raw_response_wrapper(
            graphs.list,
        )


class AsyncGraphsResourceWithRawResponse:
    def __init__(self, graphs: AsyncGraphsResource) -> None:
        self._graphs = graphs

        self.update = async_to_raw_response_wrapper(
            graphs.update,
        )
        self.list = async_to_raw_response_wrapper(
            graphs.list,
        )


class GraphsResourceWithStreamingResponse:
    def __init__(self, graphs: GraphsResource) -> None:
        self._graphs = graphs

        self.update = to_streamed_response_wrapper(
            graphs.update,
        )
        self.list = to_streamed_response_wrapper(
            graphs.list,
        )


class AsyncGraphsResourceWithStreamingResponse:
    def __init__(self, graphs: AsyncGraphsResource) -> None:
        self._graphs = graphs

        self.update = async_to_streamed_response_wrapper(
            graphs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            graphs.list,
        )
