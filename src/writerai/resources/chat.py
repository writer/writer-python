# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, TypeVar, Iterable
from functools import partial
from typing_extensions import Literal, overload

import httpx

from ..types import chat_chat_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
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
from ..lib._parsing import (
    ResponseFormatT,
    validate_input_tools,
    parse_chat_completion,
    type_to_response_format_param,
)
from .._utils._utils import is_given
from ..types.parsed_chat import ParsedChatCompletion
from ..lib.streaming.chat import ChatCompletionStreamManager, AsyncChatCompletionStreamManager
from ..types.chat_completion import ChatCompletion
from ..types.chat_completion_chunk import ChatCompletionChunk
from ..types.shared_params.tool_param import ToolParam

__all__ = ["ChatResource", "AsyncChatResource"]

T = TypeVar("T")


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        response_format: chat_chat_params.ResponseFormat | Omit = omit,
        stop: Union[SequenceNotStr[str], str] | Omit = omit,
        stream: Literal[False] | Omit = omit,
        stream_options: chat_chat_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_chat_params.ToolChoice | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletion:
        """Generate a chat completion based on the provided messages.

        The response shown
        below is for non-streaming. To learn about streaming responses, see the
        [chat completion guide](https://dev.writer.com/home/chat-completion).

        Args:
          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          model: The [ID of the model](https://dev.writer.com/home/models) to use for creating
              the chat completion. Supports `palmyra-x5`, `palmyra-x4`, `palmyra-fin`,
              `palmyra-med`, `palmyra-creative`, and `palmyra-x-003-instruct`.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. This can be adjusted to allow for longer or shorter
              responses as needed. The maximum value varies by model. See the
              [models overview](/home/models) for more information about the maximum number of
              tokens for each model.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows for generating multiple responses,
              offering a variety of potential replies from which to choose.

          response_format: The response format to use for the chat completion, available with `palmyra-x4`
              and `palmyra-x5`.

              `text` is the default response format. [JSON Schema](https://json-schema.org/)
              is supported for structured responses. If you specify `json_schema`, you must
              also provide a `json_schema` object.

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

          tool_choice:
              Configure how the model will call functions:

              - `auto`: allows the model to automatically choose the tool to use, or not call
                a tool
              - `none`: disables tool calling; the model will instead generate a message
              - `required`: requires the model to call one or more tools

              You can also use a JSON object to force the model to call a specific tool. For
              example, `{"type": "function", "function": {"name": "get_current_weather"}}`
              requires the model to call the `get_current_weather` function, regardless of the
              prompt.

          tools: An array containing tool definitions for tools that the model can use to
              generate responses. The tool definitions use JSON schema. You can define your
              own functions or use one of the built-in `graph`, `llm`, `translation`, or
              `vision` tools. Note that you can only use one built-in tool type in the array
              (only one of `graph`, `llm`, `translation`, or `vision`). You can pass multiple
              [custom tools](https://dev.writer.com/home/tool-calling) of type `function` in
              the same request.

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
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        response_format: chat_chat_params.ResponseFormat | Omit = omit,
        stop: Union[SequenceNotStr[str], str] | Omit = omit,
        stream_options: chat_chat_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_chat_params.ToolChoice | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ChatCompletionChunk]:
        """Generate a chat completion based on the provided messages.

        The response shown
        below is for non-streaming. To learn about streaming responses, see the
        [chat completion guide](https://dev.writer.com/home/chat-completion).

        Args:
          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          model: The [ID of the model](https://dev.writer.com/home/models) to use for creating
              the chat completion. Supports `palmyra-x5`, `palmyra-x4`, `palmyra-fin`,
              `palmyra-med`, `palmyra-creative`, and `palmyra-x-003-instruct`.

          stream: Indicates whether the response should be streamed incrementally as it is
              generated or only returned once fully complete. Streaming can be useful for
              providing real-time feedback in interactive applications.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. This can be adjusted to allow for longer or shorter
              responses as needed. The maximum value varies by model. See the
              [models overview](/home/models) for more information about the maximum number of
              tokens for each model.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows for generating multiple responses,
              offering a variety of potential replies from which to choose.

          response_format: The response format to use for the chat completion, available with `palmyra-x4`
              and `palmyra-x5`.

              `text` is the default response format. [JSON Schema](https://json-schema.org/)
              is supported for structured responses. If you specify `json_schema`, you must
              also provide a `json_schema` object.

          stop: A token or sequence of tokens that, when generated, will cause the model to stop
              producing further content. This can be a single token or an array of tokens,
              acting as a signal to end the output.

          stream_options: Additional options for streaming.

          temperature: Controls the randomness or creativity of the model's responses. A higher
              temperature results in more varied and less predictable text, while a lower
              temperature produces more deterministic and conservative outputs.

          tool_choice:
              Configure how the model will call functions:

              - `auto`: allows the model to automatically choose the tool to use, or not call
                a tool
              - `none`: disables tool calling; the model will instead generate a message
              - `required`: requires the model to call one or more tools

              You can also use a JSON object to force the model to call a specific tool. For
              example, `{"type": "function", "function": {"name": "get_current_weather"}}`
              requires the model to call the `get_current_weather` function, regardless of the
              prompt.

          tools: An array containing tool definitions for tools that the model can use to
              generate responses. The tool definitions use JSON schema. You can define your
              own functions or use one of the built-in `graph`, `llm`, `translation`, or
              `vision` tools. Note that you can only use one built-in tool type in the array
              (only one of `graph`, `llm`, `translation`, or `vision`). You can pass multiple
              [custom tools](https://dev.writer.com/home/tool-calling) of type `function` in
              the same request.

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
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        response_format: chat_chat_params.ResponseFormat | Omit = omit,
        stop: Union[SequenceNotStr[str], str] | Omit = omit,
        stream_options: chat_chat_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_chat_params.ToolChoice | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        """Generate a chat completion based on the provided messages.

        The response shown
        below is for non-streaming. To learn about streaming responses, see the
        [chat completion guide](https://dev.writer.com/home/chat-completion).

        Args:
          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          model: The [ID of the model](https://dev.writer.com/home/models) to use for creating
              the chat completion. Supports `palmyra-x5`, `palmyra-x4`, `palmyra-fin`,
              `palmyra-med`, `palmyra-creative`, and `palmyra-x-003-instruct`.

          stream: Indicates whether the response should be streamed incrementally as it is
              generated or only returned once fully complete. Streaming can be useful for
              providing real-time feedback in interactive applications.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. This can be adjusted to allow for longer or shorter
              responses as needed. The maximum value varies by model. See the
              [models overview](/home/models) for more information about the maximum number of
              tokens for each model.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows for generating multiple responses,
              offering a variety of potential replies from which to choose.

          response_format: The response format to use for the chat completion, available with `palmyra-x4`
              and `palmyra-x5`.

              `text` is the default response format. [JSON Schema](https://json-schema.org/)
              is supported for structured responses. If you specify `json_schema`, you must
              also provide a `json_schema` object.

          stop: A token or sequence of tokens that, when generated, will cause the model to stop
              producing further content. This can be a single token or an array of tokens,
              acting as a signal to end the output.

          stream_options: Additional options for streaming.

          temperature: Controls the randomness or creativity of the model's responses. A higher
              temperature results in more varied and less predictable text, while a lower
              temperature produces more deterministic and conservative outputs.

          tool_choice:
              Configure how the model will call functions:

              - `auto`: allows the model to automatically choose the tool to use, or not call
                a tool
              - `none`: disables tool calling; the model will instead generate a message
              - `required`: requires the model to call one or more tools

              You can also use a JSON object to force the model to call a specific tool. For
              example, `{"type": "function", "function": {"name": "get_current_weather"}}`
              requires the model to call the `get_current_weather` function, regardless of the
              prompt.

          tools: An array containing tool definitions for tools that the model can use to
              generate responses. The tool definitions use JSON schema. You can define your
              own functions or use one of the built-in `graph`, `llm`, `translation`, or
              `vision` tools. Note that you can only use one built-in tool type in the array
              (only one of `graph`, `llm`, `translation`, or `vision`). You can pass multiple
              [custom tools](https://dev.writer.com/home/tool-calling) of type `function` in
              the same request.

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
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        response_format: chat_chat_params.ResponseFormat | Omit = omit,
        stop: Union[SequenceNotStr[str], str] | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        stream_options: chat_chat_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_chat_params.ToolChoice | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        return self._post(
            "/v1/chat",
            body=maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "response_format": response_format,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                chat_chat_params.ChatChatParamsStreaming if stream else chat_chat_params.ChatChatParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionChunk],
        )

    def parse(
        self,
        *,
        model: str,
        messages: Iterable[chat_chat_params.Message],
        response_format: Type[T],
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        stop: Union[SequenceNotStr[str], str] | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_chat_params.ToolChoice | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsedChatCompletion[T]:
        """
        Generate a chat completion with a structured response based on the provided messages.

        This method provides automatic parsing of the response based on the provided Pydantic model
        or dataclass type.

        Args:
          model: The [ID of the model](https://dev.writer.com/home/models) to use for creating
              the chat completion. Supports `palmyra-x-004`, `palmyra-fin`, `palmyra-med`,
              `palmyra-creative`, and `palmyra-x-003-instruct`.

          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          response_format: A Pydantic model or dataclass type to parse the response content into.
              This automatically sets the JSON Schema response format parameter for the API request.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. The default value is set to 16, but it can be adjusted
              to allow for longer or shorter responses as needed.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows for generating multiple responses,
              offering a variety of potential replies from which to choose.

          stop: A token or sequence of tokens that, when generated, will cause the model to stop
              producing further content. This can be a single token or an array of tokens,
              acting as a signal to end the output.

          temperature: Controls the randomness or creativity of the model's responses. A higher
              temperature results in more varied and less predictable text, while a lower
              temperature produces more deterministic and conservative outputs.

          tool_choice: Configure how the model will call functions: `auto` will allow the model to
              automatically choose the best tool, `none` disables tool calling. You can also
              pass a specific previously defined function.

          tools: An array containing tool definitions for tools that the model can use to
              generate responses. The tool definitions use JSON schema. You can define your
              own functions or use one of the built-in `graph`, `llm`, or `vision` tools. Note
              that you can only use one built-in tool type in the array (only one of `graph`,
              `llm`, or `vision`). You can pass multiple custom
              tools](https://dev.writer.com/api-guides/tool-calling) of type `function` in the
              same request.

          top_p: Sets the threshold for "nucleus sampling," a technique to focus the model's
              token generation on the most likely subset of tokens. Only tokens with
              cumulative probability above this threshold are considered, controlling the
              trade-off between creativity and coherence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        validate_input_tools(tools)

        # Setting JSON Schema response format automatically
        response_format_param = type_to_response_format_param(response_format)

        chat_completion = self.chat(
            messages=messages,
            model=model,
            logprobs=logprobs,
            max_tokens=max_tokens,
            n=n,
            response_format=response_format_param,
            stop=stop,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_p=top_p,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

        return parse_chat_completion(
            response_format=response_format,
            input_tools=tools if is_given(tools) else [],
            chat_completion=chat_completion,
        )

    def stream(
        self,
        *,
        messages: Iterable[chat_chat_params.Message],
        model: str,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        stop: Union[SequenceNotStr[str], str] | Omit = omit,
        stream_options: chat_chat_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_chat_params.ToolChoice | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletionStreamManager[ResponseFormatT]:
        """Wrapper over the `client.chat.chat(stream=True)` method that provides a more granular event API
        and automatic accumulation of each delta.

        Unlike `.create(stream=True)`, the `.stream()` method requires usage within a context manager to prevent accidental leakage of the response:
        ```py
        with client.chat.stream(
            model="palmyra-x-003-instruct",
            messages=[...],
        ) as stream:
            for event in stream:
                if event.type == "content.delta":
                    print(event.delta, flush=True, end="")
        ```

        When the context manager is entered, a `ChatCompletionStream` instance is returned which, like `.create(stream=True)` is an iterator. The full list of events that are yielded by the iterator are outlined in [these docs](https://github.com/writer/writer-python/blob/main/helpers.md#chat-completions-events).

        When the context manager exits, the response will be closed, however the `stream` instance is still available outside
        the context manager.
        """
        extra_headers = {
            "X-Stainless-Helper-Method": "chat.stream",
            **(extra_headers or {}),
        }

        api_request: partial[Stream[ChatCompletionChunk]] = partial(
            self._client.chat.chat,
            messages=messages,
            model=model,
            stream=True,
            logprobs=logprobs,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            stream_options=stream_options,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_p=top_p,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return ChatCompletionStreamManager(
            api_request,
            response_format=omit,
            input_tools=tools,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        response_format: chat_chat_params.ResponseFormat | Omit = omit,
        stop: Union[SequenceNotStr[str], str] | Omit = omit,
        stream: Literal[False] | Omit = omit,
        stream_options: chat_chat_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_chat_params.ToolChoice | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletion:
        """Generate a chat completion based on the provided messages.

        The response shown
        below is for non-streaming. To learn about streaming responses, see the
        [chat completion guide](https://dev.writer.com/home/chat-completion).

        Args:
          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          model: The [ID of the model](https://dev.writer.com/home/models) to use for creating
              the chat completion. Supports `palmyra-x5`, `palmyra-x4`, `palmyra-fin`,
              `palmyra-med`, `palmyra-creative`, and `palmyra-x-003-instruct`.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. This can be adjusted to allow for longer or shorter
              responses as needed. The maximum value varies by model. See the
              [models overview](/home/models) for more information about the maximum number of
              tokens for each model.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows for generating multiple responses,
              offering a variety of potential replies from which to choose.

          response_format: The response format to use for the chat completion, available with `palmyra-x4`
              and `palmyra-x5`.

              `text` is the default response format. [JSON Schema](https://json-schema.org/)
              is supported for structured responses. If you specify `json_schema`, you must
              also provide a `json_schema` object.

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

          tool_choice:
              Configure how the model will call functions:

              - `auto`: allows the model to automatically choose the tool to use, or not call
                a tool
              - `none`: disables tool calling; the model will instead generate a message
              - `required`: requires the model to call one or more tools

              You can also use a JSON object to force the model to call a specific tool. For
              example, `{"type": "function", "function": {"name": "get_current_weather"}}`
              requires the model to call the `get_current_weather` function, regardless of the
              prompt.

          tools: An array containing tool definitions for tools that the model can use to
              generate responses. The tool definitions use JSON schema. You can define your
              own functions or use one of the built-in `graph`, `llm`, `translation`, or
              `vision` tools. Note that you can only use one built-in tool type in the array
              (only one of `graph`, `llm`, `translation`, or `vision`). You can pass multiple
              [custom tools](https://dev.writer.com/home/tool-calling) of type `function` in
              the same request.

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
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        response_format: chat_chat_params.ResponseFormat | Omit = omit,
        stop: Union[SequenceNotStr[str], str] | Omit = omit,
        stream_options: chat_chat_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_chat_params.ToolChoice | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ChatCompletionChunk]:
        """Generate a chat completion based on the provided messages.

        The response shown
        below is for non-streaming. To learn about streaming responses, see the
        [chat completion guide](https://dev.writer.com/home/chat-completion).

        Args:
          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          model: The [ID of the model](https://dev.writer.com/home/models) to use for creating
              the chat completion. Supports `palmyra-x5`, `palmyra-x4`, `palmyra-fin`,
              `palmyra-med`, `palmyra-creative`, and `palmyra-x-003-instruct`.

          stream: Indicates whether the response should be streamed incrementally as it is
              generated or only returned once fully complete. Streaming can be useful for
              providing real-time feedback in interactive applications.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. This can be adjusted to allow for longer or shorter
              responses as needed. The maximum value varies by model. See the
              [models overview](/home/models) for more information about the maximum number of
              tokens for each model.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows for generating multiple responses,
              offering a variety of potential replies from which to choose.

          response_format: The response format to use for the chat completion, available with `palmyra-x4`
              and `palmyra-x5`.

              `text` is the default response format. [JSON Schema](https://json-schema.org/)
              is supported for structured responses. If you specify `json_schema`, you must
              also provide a `json_schema` object.

          stop: A token or sequence of tokens that, when generated, will cause the model to stop
              producing further content. This can be a single token or an array of tokens,
              acting as a signal to end the output.

          stream_options: Additional options for streaming.

          temperature: Controls the randomness or creativity of the model's responses. A higher
              temperature results in more varied and less predictable text, while a lower
              temperature produces more deterministic and conservative outputs.

          tool_choice:
              Configure how the model will call functions:

              - `auto`: allows the model to automatically choose the tool to use, or not call
                a tool
              - `none`: disables tool calling; the model will instead generate a message
              - `required`: requires the model to call one or more tools

              You can also use a JSON object to force the model to call a specific tool. For
              example, `{"type": "function", "function": {"name": "get_current_weather"}}`
              requires the model to call the `get_current_weather` function, regardless of the
              prompt.

          tools: An array containing tool definitions for tools that the model can use to
              generate responses. The tool definitions use JSON schema. You can define your
              own functions or use one of the built-in `graph`, `llm`, `translation`, or
              `vision` tools. Note that you can only use one built-in tool type in the array
              (only one of `graph`, `llm`, `translation`, or `vision`). You can pass multiple
              [custom tools](https://dev.writer.com/home/tool-calling) of type `function` in
              the same request.

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
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        response_format: chat_chat_params.ResponseFormat | Omit = omit,
        stop: Union[SequenceNotStr[str], str] | Omit = omit,
        stream_options: chat_chat_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_chat_params.ToolChoice | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        """Generate a chat completion based on the provided messages.

        The response shown
        below is for non-streaming. To learn about streaming responses, see the
        [chat completion guide](https://dev.writer.com/home/chat-completion).

        Args:
          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          model: The [ID of the model](https://dev.writer.com/home/models) to use for creating
              the chat completion. Supports `palmyra-x5`, `palmyra-x4`, `palmyra-fin`,
              `palmyra-med`, `palmyra-creative`, and `palmyra-x-003-instruct`.

          stream: Indicates whether the response should be streamed incrementally as it is
              generated or only returned once fully complete. Streaming can be useful for
              providing real-time feedback in interactive applications.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. This can be adjusted to allow for longer or shorter
              responses as needed. The maximum value varies by model. See the
              [models overview](/home/models) for more information about the maximum number of
              tokens for each model.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows for generating multiple responses,
              offering a variety of potential replies from which to choose.

          response_format: The response format to use for the chat completion, available with `palmyra-x4`
              and `palmyra-x5`.

              `text` is the default response format. [JSON Schema](https://json-schema.org/)
              is supported for structured responses. If you specify `json_schema`, you must
              also provide a `json_schema` object.

          stop: A token or sequence of tokens that, when generated, will cause the model to stop
              producing further content. This can be a single token or an array of tokens,
              acting as a signal to end the output.

          stream_options: Additional options for streaming.

          temperature: Controls the randomness or creativity of the model's responses. A higher
              temperature results in more varied and less predictable text, while a lower
              temperature produces more deterministic and conservative outputs.

          tool_choice:
              Configure how the model will call functions:

              - `auto`: allows the model to automatically choose the tool to use, or not call
                a tool
              - `none`: disables tool calling; the model will instead generate a message
              - `required`: requires the model to call one or more tools

              You can also use a JSON object to force the model to call a specific tool. For
              example, `{"type": "function", "function": {"name": "get_current_weather"}}`
              requires the model to call the `get_current_weather` function, regardless of the
              prompt.

          tools: An array containing tool definitions for tools that the model can use to
              generate responses. The tool definitions use JSON schema. You can define your
              own functions or use one of the built-in `graph`, `llm`, `translation`, or
              `vision` tools. Note that you can only use one built-in tool type in the array
              (only one of `graph`, `llm`, `translation`, or `vision`). You can pass multiple
              [custom tools](https://dev.writer.com/home/tool-calling) of type `function` in
              the same request.

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
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        response_format: chat_chat_params.ResponseFormat | Omit = omit,
        stop: Union[SequenceNotStr[str], str] | Omit = omit,
        stream: Literal[False] | Literal[True] | Omit = omit,
        stream_options: chat_chat_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_chat_params.ToolChoice | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        return await self._post(
            "/v1/chat",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "model": model,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "response_format": response_format,
                    "stop": stop,
                    "stream": stream,
                    "stream_options": stream_options,
                    "temperature": temperature,
                    "tool_choice": tool_choice,
                    "tools": tools,
                    "top_p": top_p,
                },
                chat_chat_params.ChatChatParamsStreaming if stream else chat_chat_params.ChatChatParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionChunk],
        )

    async def parse(
        self,
        *,
        model: str,
        messages: Iterable[chat_chat_params.Message],
        response_format: Type[T],
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        stop: Union[SequenceNotStr[str], str] | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_chat_params.ToolChoice | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsedChatCompletion[T]:
        """
        Generate a chat completion with a structured response based on the provided messages.

        This method provides automatic parsing of the response based on the provided Pydantic model
        or dataclass type.

        Args:
          model: The [ID of the model](https://dev.writer.com/home/models) to use for creating
              the chat completion. Supports `palmyra-x-004`, `palmyra-fin`, `palmyra-med`,
              `palmyra-creative`, and `palmyra-x-003-instruct`.

          messages: An array of message objects that form the conversation history or context for
              the model to respond to. The array must contain at least one message.

          response_format: A Pydantic model or dataclass type to parse the response content into.
              This automatically sets the JSON Schema response format parameter for the API request.

          logprobs: Specifies whether to return log probabilities of the output tokens.

          max_tokens: Defines the maximum number of tokens (words and characters) that the model can
              generate in the response. The default value is set to 16, but it can be adjusted
              to allow for longer or shorter responses as needed.

          n: Specifies the number of completions (responses) to generate from the model in a
              single request. This parameter allows for generating multiple responses,
              offering a variety of potential replies from which to choose.

          stop: A token or sequence of tokens that, when generated, will cause the model to stop
              producing further content. This can be a single token or an array of tokens,
              acting as a signal to end the output.

          temperature: Controls the randomness or creativity of the model's responses. A higher
              temperature results in more varied and less predictable text, while a lower
              temperature produces more deterministic and conservative outputs.

          tool_choice: Configure how the model will call functions: `auto` will allow the model to
              automatically choose the best tool, `none` disables tool calling. You can also
              pass a specific previously defined function.

          tools: An array containing tool definitions for tools that the model can use to
              generate responses. The tool definitions use JSON schema. You can define your
              own functions or use one of the built-in `graph`, `llm`, or `vision` tools. Note
              that you can only use one built-in tool type in the array (only one of `graph`,
              `llm`, or `vision`). You can pass multiple custom
              tools](https://dev.writer.com/api-guides/tool-calling) of type `function` in the
              same request.

          top_p: Sets the threshold for "nucleus sampling," a technique to focus the model's
              token generation on the most likely subset of tokens. Only tokens with
              cumulative probability above this threshold are considered, controlling the
              trade-off between creativity and coherence.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        validate_input_tools(tools)

        # Setting JSON Schema response format automatically
        response_format_param = type_to_response_format_param(response_format)

        chat_completion = await self.chat(
            messages=messages,
            model=model,
            logprobs=logprobs,
            max_tokens=max_tokens,
            n=n,
            response_format=response_format_param,
            stop=stop,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_p=top_p,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

        return parse_chat_completion(
            response_format=response_format,
            input_tools=tools if is_given(tools) else [],
            chat_completion=chat_completion,
        )

    def stream(
        self,
        *,
        messages: Iterable[chat_chat_params.Message],
        model: str,
        logprobs: bool | Omit = omit,
        max_tokens: int | Omit = omit,
        n: int | Omit = omit,
        stop: Union[SequenceNotStr[str], str] | Omit = omit,
        stream_options: chat_chat_params.StreamOptions | Omit = omit,
        temperature: float | Omit = omit,
        tool_choice: chat_chat_params.ToolChoice | Omit = omit,
        tools: Iterable[ToolParam] | Omit = omit,
        top_p: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncChatCompletionStreamManager[ResponseFormatT]:
        """Wrapper over the `client.chat.chat(stream=True)` method that provides a more granular event API
        and automatic accumulation of each delta.

        Unlike `.create(stream=True)`, the `.stream()` method requires usage within a context manager to prevent accidental leakage of the response:
        ```py
        async with client.chat.stream(
            model="palmyra-x-003-instruct",
            messages=[...],
        ) as stream:
            async for event in stream:
                if event.type == "content.delta":
                    print(event.delta, flush=True, end="")
        ```

        When the context manager is entered, a `AsyncChatCompletionStream` instance is returned which, like `.create(stream=True)` is an async iterator. The full list of events that are yielded by the iterator are outlined in [these docs](https://github.com/writer/writer-python/blob/main/helpers.md#chat-completions-events).

        When the context manager exits, the response will be closed, however the `stream` instance is still available outside
        the context manager.
        """
        extra_headers = {
            "X-Stainless-Helper-Method": "chat.stream",
            **(extra_headers or {}),
        }

        api_request = self._client.chat.chat(
            messages=messages,
            model=model,
            stream=True,
            logprobs=logprobs,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            stream_options=stream_options,
            temperature=temperature,
            tool_choice=tool_choice,
            tools=tools,
            top_p=top_p,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return AsyncChatCompletionStreamManager(
            api_request,
            response_format=omit,
            input_tools=tools,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.chat = to_raw_response_wrapper(
            chat.chat,
        )

        self.parse = to_raw_response_wrapper(
            chat.parse,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.chat = async_to_raw_response_wrapper(
            chat.chat,
        )

        self.parse = async_to_raw_response_wrapper(
            chat.parse,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.chat = to_streamed_response_wrapper(
            chat.chat,
        )

        self.parse = to_streamed_response_wrapper(
            chat.parse,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.chat = async_to_streamed_response_wrapper(
            chat.chat,
        )

        self.parse = async_to_streamed_response_wrapper(
            chat.parse,
        )
