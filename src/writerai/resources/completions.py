# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, overload

import httpx

from ..types import completion_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .._base_client import make_request_options
from ..types.completion import Completion
from ..types.completion_chunk import CompletionChunk

__all__ = ["CompletionsResource", "AsyncCompletionsResource"]


class CompletionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return CompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return CompletionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        model: str,
        prompt: str,
        best_of: int | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        random_seed: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Completion:
        """
        Text generation

        Args:
          model: The identifier of the model to be used for processing the request.

          prompt: The input text that the model will process to generate a response.

          best_of: Specifies the number of completions to generate and return the best one. Useful
              for generating multiple outputs and choosing the best based on some criteria.

          max_tokens: The maximum number of tokens that the model can generate in the response.

          random_seed: A seed used to initialize the random number generator for the model, ensuring
              reproducibility of the output when the same inputs are provided.

          stop: Specifies stopping conditions for the model's output generation. This can be an
              array of strings or a single string that the model will look for as a signal to
              stop generating further tokens.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          temperature: Controls the randomness of the model's outputs. Higher values lead to more
              random outputs, while lower values make the model more deterministic.

          top_p: Used to control the nucleus sampling, where only the most probable tokens with a
              cumulative probability of top_p are considered for sampling, providing a way to
              fine-tune the randomness of predictions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        model: str,
        prompt: str,
        stream: Literal[True],
        best_of: int | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        random_seed: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[CompletionChunk]:
        """
        Text generation

        Args:
          model: The identifier of the model to be used for processing the request.

          prompt: The input text that the model will process to generate a response.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          best_of: Specifies the number of completions to generate and return the best one. Useful
              for generating multiple outputs and choosing the best based on some criteria.

          max_tokens: The maximum number of tokens that the model can generate in the response.

          random_seed: A seed used to initialize the random number generator for the model, ensuring
              reproducibility of the output when the same inputs are provided.

          stop: Specifies stopping conditions for the model's output generation. This can be an
              array of strings or a single string that the model will look for as a signal to
              stop generating further tokens.

          temperature: Controls the randomness of the model's outputs. Higher values lead to more
              random outputs, while lower values make the model more deterministic.

          top_p: Used to control the nucleus sampling, where only the most probable tokens with a
              cumulative probability of top_p are considered for sampling, providing a way to
              fine-tune the randomness of predictions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        model: str,
        prompt: str,
        stream: bool,
        best_of: int | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        random_seed: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Completion | Stream[CompletionChunk]:
        """
        Text generation

        Args:
          model: The identifier of the model to be used for processing the request.

          prompt: The input text that the model will process to generate a response.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          best_of: Specifies the number of completions to generate and return the best one. Useful
              for generating multiple outputs and choosing the best based on some criteria.

          max_tokens: The maximum number of tokens that the model can generate in the response.

          random_seed: A seed used to initialize the random number generator for the model, ensuring
              reproducibility of the output when the same inputs are provided.

          stop: Specifies stopping conditions for the model's output generation. This can be an
              array of strings or a single string that the model will look for as a signal to
              stop generating further tokens.

          temperature: Controls the randomness of the model's outputs. Higher values lead to more
              random outputs, while lower values make the model more deterministic.

          top_p: Used to control the nucleus sampling, where only the most probable tokens with a
              cumulative probability of top_p are considered for sampling, providing a way to
              fine-tune the randomness of predictions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt"], ["model", "prompt", "stream"])
    def create(
        self,
        *,
        model: str,
        prompt: str,
        best_of: int | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        random_seed: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Completion | Stream[CompletionChunk]:
        return self._post(
            "/v1/completions",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "best_of": best_of,
                    "max_tokens": max_tokens,
                    "random_seed": random_seed,
                    "stop": stop,
                    "stream": stream,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Completion,
            stream=stream or False,
            stream_cls=Stream[CompletionChunk],
        )


class AsyncCompletionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCompletionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return AsyncCompletionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        model: str,
        prompt: str,
        best_of: int | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        random_seed: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Completion:
        """
        Text generation

        Args:
          model: The identifier of the model to be used for processing the request.

          prompt: The input text that the model will process to generate a response.

          best_of: Specifies the number of completions to generate and return the best one. Useful
              for generating multiple outputs and choosing the best based on some criteria.

          max_tokens: The maximum number of tokens that the model can generate in the response.

          random_seed: A seed used to initialize the random number generator for the model, ensuring
              reproducibility of the output when the same inputs are provided.

          stop: Specifies stopping conditions for the model's output generation. This can be an
              array of strings or a single string that the model will look for as a signal to
              stop generating further tokens.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          temperature: Controls the randomness of the model's outputs. Higher values lead to more
              random outputs, while lower values make the model more deterministic.

          top_p: Used to control the nucleus sampling, where only the most probable tokens with a
              cumulative probability of top_p are considered for sampling, providing a way to
              fine-tune the randomness of predictions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        model: str,
        prompt: str,
        stream: Literal[True],
        best_of: int | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        random_seed: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[CompletionChunk]:
        """
        Text generation

        Args:
          model: The identifier of the model to be used for processing the request.

          prompt: The input text that the model will process to generate a response.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          best_of: Specifies the number of completions to generate and return the best one. Useful
              for generating multiple outputs and choosing the best based on some criteria.

          max_tokens: The maximum number of tokens that the model can generate in the response.

          random_seed: A seed used to initialize the random number generator for the model, ensuring
              reproducibility of the output when the same inputs are provided.

          stop: Specifies stopping conditions for the model's output generation. This can be an
              array of strings or a single string that the model will look for as a signal to
              stop generating further tokens.

          temperature: Controls the randomness of the model's outputs. Higher values lead to more
              random outputs, while lower values make the model more deterministic.

          top_p: Used to control the nucleus sampling, where only the most probable tokens with a
              cumulative probability of top_p are considered for sampling, providing a way to
              fine-tune the randomness of predictions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        model: str,
        prompt: str,
        stream: bool,
        best_of: int | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        random_seed: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Completion | AsyncStream[CompletionChunk]:
        """
        Text generation

        Args:
          model: The identifier of the model to be used for processing the request.

          prompt: The input text that the model will process to generate a response.

          stream: Determines whether the model's output should be streamed. If true, the output is
              generated and sent incrementally, which can be useful for real-time
              applications.

          best_of: Specifies the number of completions to generate and return the best one. Useful
              for generating multiple outputs and choosing the best based on some criteria.

          max_tokens: The maximum number of tokens that the model can generate in the response.

          random_seed: A seed used to initialize the random number generator for the model, ensuring
              reproducibility of the output when the same inputs are provided.

          stop: Specifies stopping conditions for the model's output generation. This can be an
              array of strings or a single string that the model will look for as a signal to
              stop generating further tokens.

          temperature: Controls the randomness of the model's outputs. Higher values lead to more
              random outputs, while lower values make the model more deterministic.

          top_p: Used to control the nucleus sampling, where only the most probable tokens with a
              cumulative probability of top_p are considered for sampling, providing a way to
              fine-tune the randomness of predictions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model", "prompt"], ["model", "prompt", "stream"])
    async def create(
        self,
        *,
        model: str,
        prompt: str,
        best_of: int | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        random_seed: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Completion | AsyncStream[CompletionChunk]:
        return await self._post(
            "/v1/completions",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "best_of": best_of,
                    "max_tokens": max_tokens,
                    "random_seed": random_seed,
                    "stop": stop,
                    "stream": stream,
                    "temperature": temperature,
                    "top_p": top_p,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Completion,
            stream=stream or False,
            stream_cls=AsyncStream[CompletionChunk],
        )


class CompletionsResourceWithRawResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithRawResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsResourceWithStreamingResponse:
    def __init__(self, completions: CompletionsResource) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsResourceWithStreamingResponse:
    def __init__(self, completions: AsyncCompletionsResource) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
