# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from .graphs import (
    GraphsResource,
    AsyncGraphsResource,
    GraphsResourceWithRawResponse,
    AsyncGraphsResourceWithRawResponse,
    GraphsResourceWithStreamingResponse,
    AsyncGraphsResourceWithStreamingResponse,
)
from ...types import application_list_params, application_generate_content_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
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
from ..._streaming import Stream, AsyncStream
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.application_list_response import ApplicationListResponse
from ...types.application_retrieve_response import ApplicationRetrieveResponse
from ...types.application_generate_content_chunk import ApplicationGenerateContentChunk
from ...types.application_generate_content_response import ApplicationGenerateContentResponse

__all__ = ["ApplicationsResource", "AsyncApplicationsResource"]


class ApplicationsResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def graphs(self) -> GraphsResource:
        return GraphsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return ApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return ApplicationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        application_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationRetrieveResponse:
        """
        Retrieves detailed information for a specific no-code application, including its
        configuration and current status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._get(
            f"/v1/applications/{application_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplicationRetrieveResponse,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        type: Literal["generation"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[ApplicationListResponse]:
        """
        Retrieves a paginated list of no-code applications with optional filtering and
        sorting capabilities.

        Args:
          after: Return results after this application ID for pagination.

          before: Return results before this application ID for pagination.

          limit: Maximum number of applications to return in the response.

          order: Sort order for the results based on creation time.

          type: Filter applications by their type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/applications",
            page=SyncCursorPage[ApplicationListResponse],
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
                        "type": type,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=ApplicationListResponse,
        )

    @overload
    def generate_content(
        self,
        application_id: str,
        *,
        inputs: Iterable[application_generate_content_params.Input],
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationGenerateContentResponse:
        """
        Generate content from an existing no-code application with inputs.

        Args:
          stream: Indicates whether the response should be streamed. Currently only supported for
              research assistant applications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def generate_content(
        self,
        application_id: str,
        *,
        inputs: Iterable[application_generate_content_params.Input],
        stream: Literal[True],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[ApplicationGenerateContentChunk]:
        """
        Generate content from an existing no-code application with inputs.

        Args:
          stream: Indicates whether the response should be streamed. Currently only supported for
              research assistant applications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def generate_content(
        self,
        application_id: str,
        *,
        inputs: Iterable[application_generate_content_params.Input],
        stream: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationGenerateContentResponse | Stream[ApplicationGenerateContentChunk]:
        """
        Generate content from an existing no-code application with inputs.

        Args:
          stream: Indicates whether the response should be streamed. Currently only supported for
              research assistant applications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["inputs"], ["inputs", "stream"])
    def generate_content(
        self,
        application_id: str,
        *,
        inputs: Iterable[application_generate_content_params.Input],
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationGenerateContentResponse | Stream[ApplicationGenerateContentChunk]:
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return self._post(
            f"/v1/applications/{application_id}",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "stream": stream,
                },
                application_generate_content_params.ApplicationGenerateContentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplicationGenerateContentResponse,
            stream=stream or False,
            stream_cls=Stream[ApplicationGenerateContentChunk],
        )


class AsyncApplicationsResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def graphs(self) -> AsyncGraphsResource:
        return AsyncGraphsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return AsyncApplicationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        application_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationRetrieveResponse:
        """
        Retrieves detailed information for a specific no-code application, including its
        configuration and current status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._get(
            f"/v1/applications/{application_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplicationRetrieveResponse,
        )

    def list(
        self,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        type: Literal["generation"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ApplicationListResponse, AsyncCursorPage[ApplicationListResponse]]:
        """
        Retrieves a paginated list of no-code applications with optional filtering and
        sorting capabilities.

        Args:
          after: Return results after this application ID for pagination.

          before: Return results before this application ID for pagination.

          limit: Maximum number of applications to return in the response.

          order: Sort order for the results based on creation time.

          type: Filter applications by their type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/applications",
            page=AsyncCursorPage[ApplicationListResponse],
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
                        "type": type,
                    },
                    application_list_params.ApplicationListParams,
                ),
            ),
            model=ApplicationListResponse,
        )

    @overload
    async def generate_content(
        self,
        application_id: str,
        *,
        inputs: Iterable[application_generate_content_params.Input],
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationGenerateContentResponse:
        """
        Generate content from an existing no-code application with inputs.

        Args:
          stream: Indicates whether the response should be streamed. Currently only supported for
              research assistant applications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def generate_content(
        self,
        application_id: str,
        *,
        inputs: Iterable[application_generate_content_params.Input],
        stream: Literal[True],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[ApplicationGenerateContentChunk]:
        """
        Generate content from an existing no-code application with inputs.

        Args:
          stream: Indicates whether the response should be streamed. Currently only supported for
              research assistant applications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def generate_content(
        self,
        application_id: str,
        *,
        inputs: Iterable[application_generate_content_params.Input],
        stream: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationGenerateContentResponse | AsyncStream[ApplicationGenerateContentChunk]:
        """
        Generate content from an existing no-code application with inputs.

        Args:
          stream: Indicates whether the response should be streamed. Currently only supported for
              research assistant applications.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["inputs"], ["inputs", "stream"])
    async def generate_content(
        self,
        application_id: str,
        *,
        inputs: Iterable[application_generate_content_params.Input],
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ApplicationGenerateContentResponse | AsyncStream[ApplicationGenerateContentChunk]:
        if not application_id:
            raise ValueError(f"Expected a non-empty value for `application_id` but received {application_id!r}")
        return await self._post(
            f"/v1/applications/{application_id}",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "stream": stream,
                },
                application_generate_content_params.ApplicationGenerateContentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ApplicationGenerateContentResponse,
            stream=stream or False,
            stream_cls=AsyncStream[ApplicationGenerateContentChunk],
        )


class ApplicationsResourceWithRawResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.retrieve = to_raw_response_wrapper(
            applications.retrieve,
        )
        self.list = to_raw_response_wrapper(
            applications.list,
        )
        self.generate_content = to_raw_response_wrapper(
            applications.generate_content,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._applications.jobs)

    @cached_property
    def graphs(self) -> GraphsResourceWithRawResponse:
        return GraphsResourceWithRawResponse(self._applications.graphs)


class AsyncApplicationsResourceWithRawResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.retrieve = async_to_raw_response_wrapper(
            applications.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            applications.list,
        )
        self.generate_content = async_to_raw_response_wrapper(
            applications.generate_content,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._applications.jobs)

    @cached_property
    def graphs(self) -> AsyncGraphsResourceWithRawResponse:
        return AsyncGraphsResourceWithRawResponse(self._applications.graphs)


class ApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.retrieve = to_streamed_response_wrapper(
            applications.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            applications.list,
        )
        self.generate_content = to_streamed_response_wrapper(
            applications.generate_content,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._applications.jobs)

    @cached_property
    def graphs(self) -> GraphsResourceWithStreamingResponse:
        return GraphsResourceWithStreamingResponse(self._applications.graphs)


class AsyncApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.retrieve = async_to_streamed_response_wrapper(
            applications.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            applications.list,
        )
        self.generate_content = async_to_streamed_response_wrapper(
            applications.generate_content,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._applications.jobs)

    @cached_property
    def graphs(self) -> AsyncGraphsResourceWithStreamingResponse:
        return AsyncGraphsResourceWithStreamingResponse(self._applications.graphs)
