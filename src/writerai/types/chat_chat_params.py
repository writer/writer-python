# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .shared_params.tool_call import ToolCall
from .shared_params.graph_data import GraphData
from .shared_params.tool_param import ToolParam
from .shared_params.tool_choice_string import ToolChoiceString
from .shared_params.tool_choice_json_object import ToolChoiceJsonObject

__all__ = [
    "ChatChatParamsBase",
    "Message",
    "MessageContentMixedContent",
    "MessageContentMixedContentTextFragment",
    "MessageContentMixedContentImageFragment",
    "MessageContentMixedContentImageFragmentImageURL",
    "ResponseFormat",
    "StreamOptions",
    "ToolChoice",
    "ChatChatParamsNonStreaming",
    "ChatChatParamsStreaming",
]


class ChatChatParamsBase(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """
    An array of message objects that form the conversation history or context for
    the model to respond to. The array must contain at least one message.
    """

    model: Required[str]
    """
    The [ID of the model](https://dev.writer.com/home/models) to use for creating
    the chat completion. Supports `palmyra-x5`, `palmyra-x4`, `palmyra-fin`,
    `palmyra-med`, `palmyra-creative`, and `palmyra-x-003-instruct`.
    """

    logprobs: bool
    """Specifies whether to return log probabilities of the output tokens."""

    max_tokens: int
    """
    Defines the maximum number of tokens (words and characters) that the model can
    generate in the response. This can be adjusted to allow for longer or shorter
    responses as needed. The maximum value varies by model. See the
    [models overview](/home/models) for more information about the maximum number of
    tokens for each model.
    """

    n: int
    """
    Specifies the number of completions (responses) to generate from the model in a
    single request. This parameter allows for generating multiple responses,
    offering a variety of potential replies from which to choose.
    """

    response_format: ResponseFormat
    """
    The response format to use for the chat completion, available with `palmyra-x4`
    and `palmyra-x5`.

    `text` is the default response format. [JSON Schema](https://json-schema.org/)
    is supported for structured responses. If you specify `json_schema`, you must
    also provide a `json_schema` object.
    """

    stop: Union[SequenceNotStr[str], str]
    """
    A token or sequence of tokens that, when generated, will cause the model to stop
    producing further content. This can be a single token or an array of tokens,
    acting as a signal to end the output.
    """

    stream_options: StreamOptions
    """Additional options for streaming."""

    temperature: float
    """Controls the randomness or creativity of the model's responses.

    A higher temperature results in more varied and less predictable text, while a
    lower temperature produces more deterministic and conservative outputs.
    """

    tool_choice: ToolChoice
    """Configure how the model will call functions:

    - `auto`: allows the model to automatically choose the tool to use, or not call
      a tool
    - `none`: disables tool calling; the model will instead generate a message
    - `required`: requires the model to call one or more tools

    You can also use a JSON object to force the model to call a specific tool. For
    example, `{"type": "function", "function": {"name": "get_current_weather"}}`
    requires the model to call the `get_current_weather` function, regardless of the
    prompt.
    """

    tools: Iterable[ToolParam]
    """
    An array containing tool definitions for tools that the model can use to
    generate responses. The tool definitions use JSON schema. You can define your
    own functions or use one of the built-in `graph`, `llm`, `translation`, or
    `vision` tools. Note that you can only use one built-in tool type in the array
    (only one of `graph`, `llm`, `translation`, or `vision`). You can pass multiple
    [custom tools](https://dev.writer.com/home/tool-calling) of type `function` in
    the same request.
    """

    top_p: float
    """
    Sets the threshold for "nucleus sampling," a technique to focus the model's
    token generation on the most likely subset of tokens. Only tokens with
    cumulative probability above this threshold are considered, controlling the
    trade-off between creativity and coherence.
    """


class MessageContentMixedContentTextFragment(TypedDict, total=False):
    text: Required[str]
    """The actual text content of the message fragment."""

    type: Required[Literal["text"]]
    """The type of content fragment. Must be `text` for text fragments."""


class MessageContentMixedContentImageFragmentImageURL(TypedDict, total=False):
    url: Required[str]
    """The URL pointing to the image file.

    Supports common image formats like JPEG, PNG, GIF, etc.
    """


class MessageContentMixedContentImageFragment(TypedDict, total=False):
    image_url: Required[MessageContentMixedContentImageFragmentImageURL]
    """The image URL object containing the location of the image."""

    type: Required[Literal["image_url"]]
    """The type of content fragment. Must be `image_url` for image fragments."""


MessageContentMixedContent: TypeAlias = Union[
    MessageContentMixedContentTextFragment, MessageContentMixedContentImageFragment
]


class Message(TypedDict, total=False):
    role: Required[Literal["user", "assistant", "system", "tool"]]
    """The role of the chat message.

    You can provide a system prompt by setting the role to `system`, or specify that
    a message is the result of a
    [tool call](https://dev.writer.com/home/tool-calling) by setting the role to
    `tool`.
    """

    content: Union[str, Iterable[MessageContentMixedContent], None]
    """The content of the message.

    Can be either a string (for text-only messages) or an array of content fragments
    (for mixed text and image messages).
    """

    graph_data: Optional[GraphData]

    name: Optional[str]
    """An optional name for the message sender.

    Useful for identifying different users, personas, or tools in multi-participant
    conversations.
    """

    refusal: Optional[str]

    tool_call_id: Optional[str]

    tool_calls: Optional[Iterable[ToolCall]]


class ResponseFormat(TypedDict, total=False):
    type: Required[Literal["text", "json_schema"]]
    """The type of response format to use."""

    json_schema: object
    """The JSON schema to use for the response format."""


class StreamOptions(TypedDict, total=False):
    include_usage: Required[bool]
    """Indicate whether to include usage information."""


ToolChoice: TypeAlias = Union[ToolChoiceString, ToolChoiceJsonObject]


class ChatChatParamsNonStreaming(ChatChatParamsBase, total=False):
    stream: Literal[False]
    """
    Indicates whether the response should be streamed incrementally as it is
    generated or only returned once fully complete. Streaming can be useful for
    providing real-time feedback in interactive applications.
    """


class ChatChatParamsStreaming(ChatChatParamsBase):
    stream: Required[Literal[True]]
    """
    Indicates whether the response should be streamed incrementally as it is
    generated or only returned once fully complete. Streaming can be useful for
    providing real-time feedback in interactive applications.
    """


ChatChatParams = Union[ChatChatParamsNonStreaming, ChatChatParamsStreaming]
