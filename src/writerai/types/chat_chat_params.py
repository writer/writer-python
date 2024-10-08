# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ChatChatParamsBase",
    "Message",
    "StreamOptions",
    "ToolChoice",
    "ToolChoiceJsonObjectToolChoice",
    "ToolChoiceStringToolChoice",
    "Tool",
    "ToolFunctionTool",
    "ToolFunctionToolFunction",
    "ToolGraphTool",
    "ToolGraphToolFunction",
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
    """Specifies the model to be used for generating responses.

    The chat model is always `palmyra-x-004` for conversational use.
    """

    logprobs: bool
    """Specifies whether to return log probabilities of the output tokens."""

    max_tokens: int
    """
    Defines the maximum number of tokens (words and characters) that the model can
    generate in the response. The default value is set to 16, but it can be adjusted
    to allow for longer or shorter responses as needed.
    """

    n: int
    """
    Specifies the number of completions (responses) to generate from the model in a
    single request. This parameter allows multiple responses to be generated,
    offering a variety of potential replies from which to choose.
    """

    stop: Union[List[str], str]
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
    """
    Configure how the model will call functions: `auto` will allow the model to
    automatically choose the best tool, `none` disables tool calling. You can also
    pass a specific previously defined function as a string.
    """

    tools: Iterable[Tool]
    """
    [Beta] An array of tools described to the model using JSON schema that the model
    can use to generate responses. Please note that tool calling is in beta and
    subject to change. Passing graph IDs will automatically use the Knowledge Graph
    tool.
    """

    top_p: float
    """
    Sets the threshold for "nucleus sampling," a technique to focus the model's
    token generation on the most likely subset of tokens. Only tokens with
    cumulative probability above this threshold are considered, controlling the
    trade-off between creativity and coherence.
    """


class Message(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["user", "assistant", "system"]]

    name: str


class StreamOptions(TypedDict, total=False):
    include_usage: Required[bool]
    """Indicate whether to include usage information."""


class ToolChoiceJsonObjectToolChoice(TypedDict, total=False):
    value: Required[object]


class ToolChoiceStringToolChoice(TypedDict, total=False):
    value: Required[Literal["none", "auto", "required"]]


ToolChoice: TypeAlias = Union[ToolChoiceJsonObjectToolChoice, ToolChoiceStringToolChoice]


class ToolFunctionToolFunction(TypedDict, total=False):
    name: Required[str]

    description: str

    parameters: object


class ToolFunctionTool(TypedDict, total=False):
    function: Required[ToolFunctionToolFunction]


class ToolGraphToolFunction(TypedDict, total=False):
    graph_ids: Required[List[str]]
    """An array of graph IDs to be used in the tool."""

    subqueries: Required[bool]
    """Boolean to indicate whether to include subqueries in the response."""

    description: str
    """A description of the graph content."""


class ToolGraphTool(TypedDict, total=False):
    function: Required[ToolGraphToolFunction]


Tool: TypeAlias = Union[ToolFunctionTool, ToolGraphTool]


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
