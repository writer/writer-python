# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import chat_chat_params
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
from ..types.chat import Chat
from .._base_client import make_request_options
from ..types.chat_completion_chunk import ChatCompletionChunk

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    @overload
    def chat(
        self,
        *,
        messages: Iterable[chat_chat_params.Message],
        model: str,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        stream_options: chat_chat_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_chat_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_chat_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Chat:
        """Generate a chat completion based on the provided messages.

        The response shown
        below is for non-streaming. To learn about streaming responses, see the
        [chat completion guide](/api-guides/chat-completion).

        Args:
          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          model: Specifies the model to be used for generating responses. The chat model is
              always `palmyra-x-004` for conversational use.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. The default value is set to 16, but it can be adjusted
              to allow for longer or shorter responses as needed.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows multiple responses to be generated,
              offering a variety of potential replies from which to choose.

          stop: A token or sequence of tokens that, when generated, will cause the model to stop
              producing further content. This can be a single token or an array of tokens,
              acting as a signal to end the output.

          stream: Indicates whether the response should be streamed incrementally as it is
              generated or only returned once fully complete. Streaming can be useful for
              providing real-time feedback in interactive applications.

          stream_options: Additional options for streaming.

          temperature: Controls the randomness or creativity of the model's responses. A higher
              temperature results in more varied and less predictable text, while a lower
              temperature produces more deterministic and conservative outputs.

          tool_choice: Configure how the model will call functions: `auto` will allow the model to
              automatically choose the best tool, `none` disables tool calling. You can also
              pass a specific previously defined function as a string.

          tools: [Beta] An array of tools described to the model using JSON schema that the model
              can use to generate responses. Please note that tool calling is in beta and
              subject to change. Passing graph IDs will automatically use the Knowledge Graph
              tool.

          top_p: Sets the threshold for "nucleus sampling," a technique to focus the model's
              token generation on the most likely subset of tokens. Only tokens with
              cumulative probability above this threshold are considered, controlling the
              trade-off between creativity and coherence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def chat(
        self,
        *,
        messages: Iterable[chat_chat_params.Message],
        model: str,
        stream: Literal[True],
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        stream_options: chat_chat_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_chat_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_chat_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[ChatCompletionChunk]:
        """Generate a chat completion based on the provided messages.

        The response shown
        below is for non-streaming. To learn about streaming responses, see the
        [chat completion guide](/api-guides/chat-completion).

        Args:
          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          model: Specifies the model to be used for generating responses. The chat model is
              always `palmyra-x-004` for conversational use.

          stream: Indicates whether the response should be streamed incrementally as it is
              generated or only returned once fully complete. Streaming can be useful for
              providing real-time feedback in interactive applications.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. The default value is set to 16, but it can be adjusted
              to allow for longer or shorter responses as needed.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows multiple responses to be generated,
              offering a variety of potential replies from which to choose.

          stop: A token or sequence of tokens that, when generated, will cause the model to stop
              producing further content. This can be a single token or an array of tokens,
              acting as a signal to end the output.

          stream_options: Additional options for streaming.

          temperature: Controls the randomness or creativity of the model's responses. A higher
              temperature results in more varied and less predictable text, while a lower
              temperature produces more deterministic and conservative outputs.

          tool_choice: Configure how the model will call functions: `auto` will allow the model to
              automatically choose the best tool, `none` disables tool calling. You can also
              pass a specific previously defined function as a string.

          tools: [Beta] An array of tools described to the model using JSON schema that the model
              can use to generate responses. Please note that tool calling is in beta and
              subject to change. Passing graph IDs will automatically use the Knowledge Graph
              tool.

          top_p: Sets the threshold for "nucleus sampling," a technique to focus the model's
              token generation on the most likely subset of tokens. Only tokens with
              cumulative probability above this threshold are considered, controlling the
              trade-off between creativity and coherence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def chat(
        self,
        *,
        messages: Iterable[chat_chat_params.Message],
        model: str,
        stream: bool,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        stream_options: chat_chat_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_chat_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_chat_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Chat | Stream[ChatCompletionChunk]:
        """Generate a chat completion based on the provided messages.

        The response shown
        below is for non-streaming. To learn about streaming responses, see the
        [chat completion guide](/api-guides/chat-completion).

        Args:
          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          model: Specifies the model to be used for generating responses. The chat model is
              always `palmyra-x-004` for conversational use.

          stream: Indicates whether the response should be streamed incrementally as it is
              generated or only returned once fully complete. Streaming can be useful for
              providing real-time feedback in interactive applications.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. The default value is set to 16, but it can be adjusted
              to allow for longer or shorter responses as needed.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows multiple responses to be generated,
              offering a variety of potential replies from which to choose.

          stop: A token or sequence of tokens that, when generated, will cause the model to stop
              producing further content. This can be a single token or an array of tokens,
              acting as a signal to end the output.

          stream_options: Additional options for streaming.

          temperature: Controls the randomness or creativity of the model's responses. A higher
              temperature results in more varied and less predictable text, while a lower
              temperature produces more deterministic and conservative outputs.

          tool_choice: Configure how the model will call functions: `auto` will allow the model to
              automatically choose the best tool, `none` disables tool calling. You can also
              pass a specific previously defined function as a string.

          tools: [Beta] An array of tools described to the model using JSON schema that the model
              can use to generate responses. Please note that tool calling is in beta and
              subject to change. Passing graph IDs will automatically use the Knowledge Graph
              tool.

          top_p: Sets the threshold for "nucleus sampling," a technique to focus the model's
              token generation on the most likely subset of tokens. Only tokens with
              cumulative probability above this threshold are considered, controlling the
              trade-off between creativity and coherence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    def chat(
        self,
        *,
        messages: Iterable[chat_chat_params.Message],
        model: str,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        stream_options: chat_chat_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_chat_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_chat_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Chat | Stream[ChatCompletionChunk]:
        return self._post(
            "/v1/chat",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                chat_chat_params.ChatChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chat,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionChunk],
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    @overload
    async def chat(
        self,
        *,
        messages: Iterable[chat_chat_params.Message],
        model: str,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        stream_options: chat_chat_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_chat_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_chat_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Chat:
        """Generate a chat completion based on the provided messages.

        The response shown
        below is for non-streaming. To learn about streaming responses, see the
        [chat completion guide](/api-guides/chat-completion).

        Args:
          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          model: Specifies the model to be used for generating responses. The chat model is
              always `palmyra-x-004` for conversational use.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. The default value is set to 16, but it can be adjusted
              to allow for longer or shorter responses as needed.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows multiple responses to be generated,
              offering a variety of potential replies from which to choose.

          stop: A token or sequence of tokens that, when generated, will cause the model to stop
              producing further content. This can be a single token or an array of tokens,
              acting as a signal to end the output.

          stream: Indicates whether the response should be streamed incrementally as it is
              generated or only returned once fully complete. Streaming can be useful for
              providing real-time feedback in interactive applications.

          stream_options: Additional options for streaming.

          temperature: Controls the randomness or creativity of the model's responses. A higher
              temperature results in more varied and less predictable text, while a lower
              temperature produces more deterministic and conservative outputs.

          tool_choice: Configure how the model will call functions: `auto` will allow the model to
              automatically choose the best tool, `none` disables tool calling. You can also
              pass a specific previously defined function as a string.

          tools: [Beta] An array of tools described to the model using JSON schema that the model
              can use to generate responses. Please note that tool calling is in beta and
              subject to change. Passing graph IDs will automatically use the Knowledge Graph
              tool.

          top_p: Sets the threshold for "nucleus sampling," a technique to focus the model's
              token generation on the most likely subset of tokens. Only tokens with
              cumulative probability above this threshold are considered, controlling the
              trade-off between creativity and coherence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def chat(
        self,
        *,
        messages: Iterable[chat_chat_params.Message],
        model: str,
        stream: Literal[True],
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        stream_options: chat_chat_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_chat_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_chat_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[ChatCompletionChunk]:
        """Generate a chat completion based on the provided messages.

        The response shown
        below is for non-streaming. To learn about streaming responses, see the
        [chat completion guide](/api-guides/chat-completion).

        Args:
          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          model: Specifies the model to be used for generating responses. The chat model is
              always `palmyra-x-004` for conversational use.

          stream: Indicates whether the response should be streamed incrementally as it is
              generated or only returned once fully complete. Streaming can be useful for
              providing real-time feedback in interactive applications.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. The default value is set to 16, but it can be adjusted
              to allow for longer or shorter responses as needed.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows multiple responses to be generated,
              offering a variety of potential replies from which to choose.

          stop: A token or sequence of tokens that, when generated, will cause the model to stop
              producing further content. This can be a single token or an array of tokens,
              acting as a signal to end the output.

          stream_options: Additional options for streaming.

          temperature: Controls the randomness or creativity of the model's responses. A higher
              temperature results in more varied and less predictable text, while a lower
              temperature produces more deterministic and conservative outputs.

          tool_choice: Configure how the model will call functions: `auto` will allow the model to
              automatically choose the best tool, `none` disables tool calling. You can also
              pass a specific previously defined function as a string.

          tools: [Beta] An array of tools described to the model using JSON schema that the model
              can use to generate responses. Please note that tool calling is in beta and
              subject to change. Passing graph IDs will automatically use the Knowledge Graph
              tool.

          top_p: Sets the threshold for "nucleus sampling," a technique to focus the model's
              token generation on the most likely subset of tokens. Only tokens with
              cumulative probability above this threshold are considered, controlling the
              trade-off between creativity and coherence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def chat(
        self,
        *,
        messages: Iterable[chat_chat_params.Message],
        model: str,
        stream: bool,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        stream_options: chat_chat_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_chat_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_chat_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Chat | AsyncStream[ChatCompletionChunk]:
        """Generate a chat completion based on the provided messages.

        The response shown
        below is for non-streaming. To learn about streaming responses, see the
        [chat completion guide](/api-guides/chat-completion).

        Args:
          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          model: Specifies the model to be used for generating responses. The chat model is
              always `palmyra-x-004` for conversational use.

          stream: Indicates whether the response should be streamed incrementally as it is
              generated or only returned once fully complete. Streaming can be useful for
              providing real-time feedback in interactive applications.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. The default value is set to 16, but it can be adjusted
              to allow for longer or shorter responses as needed.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows multiple responses to be generated,
              offering a variety of potential replies from which to choose.

          stop: A token or sequence of tokens that, when generated, will cause the model to stop
              producing further content. This can be a single token or an array of tokens,
              acting as a signal to end the output.

          stream_options: Additional options for streaming.

          temperature: Controls the randomness or creativity of the model's responses. A higher
              temperature results in more varied and less predictable text, while a lower
              temperature produces more deterministic and conservative outputs.

          tool_choice: Configure how the model will call functions: `auto` will allow the model to
              automatically choose the best tool, `none` disables tool calling. You can also
              pass a specific previously defined function as a string.

          tools: [Beta] An array of tools described to the model using JSON schema that the model
              can use to generate responses. Please note that tool calling is in beta and
              subject to change. Passing graph IDs will automatically use the Knowledge Graph
              tool.

          top_p: Sets the threshold for "nucleus sampling," a technique to focus the model's
              token generation on the most likely subset of tokens. Only tokens with
              cumulative probability above this threshold are considered, controlling the
              trade-off between creativity and coherence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages", "model"], ["messages", "model", "stream"])
    async def chat(
        self,
        *,
        messages: Iterable[chat_chat_params.Message],
        model: str,
        logprobs: bool | NotGiven = NOT_GIVEN,
        max_tokens: int | NotGiven = NOT_GIVEN,
        n: int | NotGiven = NOT_GIVEN,
        stop: Union[List[str], str] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        stream_options: chat_chat_params.StreamOptions | NotGiven = NOT_GIVEN,
        temperature: float | NotGiven = NOT_GIVEN,
        tool_choice: chat_chat_params.ToolChoice | NotGiven = NOT_GIVEN,
        tools: Iterable[chat_chat_params.Tool] | NotGiven = NOT_GIVEN,
        top_p: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Chat | AsyncStream[ChatCompletionChunk]:
        return await self._post(
            "/v1/chat",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                chat_chat_params.ChatChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Chat,
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionChunk],
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.chat = to_raw_response_wrapper(
            chat.chat,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.chat = async_to_raw_response_wrapper(
            chat.chat,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.chat = to_streamed_response_wrapper(
            chat.chat,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.chat = async_to_streamed_response_wrapper(
            chat.chat,
        )
