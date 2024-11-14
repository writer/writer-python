# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ChatChatParamsBase",
    "Message",
    "MessageGraphData",
    "MessageGraphDataSource",
    "MessageGraphDataSubquery",
    "MessageGraphDataSubquerySource",
    "MessageToolCall",
    "MessageToolCallFunction",
    "StreamOptions",
    "ToolChoice",
    "ToolChoiceStringToolChoice",
    "ToolChoiceJsonObjectToolChoice",
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
    pass a specific previously defined function.
    """

    tools: Iterable[Tool]
    """
    An array of tools described to the model using JSON schema that the model can
    use to generate responses. Passing graph IDs will automatically use the
    Knowledge Graph tool.
    """

    top_p: float
    """
    Sets the threshold for "nucleus sampling," a technique to focus the model's
    token generation on the most likely subset of tokens. Only tokens with
    cumulative probability above this threshold are considered, controlling the
    trade-off between creativity and coherence.
    """


class MessageGraphDataSource(TypedDict, total=False):
    file_id: Required[str]
    """The unique identifier of the file."""

    snippet: Required[str]
    """A snippet of text from the source file."""


class MessageGraphDataSubquerySource(TypedDict, total=False):
    file_id: Required[str]
    """The unique identifier of the file."""

    snippet: Required[str]
    """A snippet of text from the source file."""


class MessageGraphDataSubquery(TypedDict, total=False):
    answer: Required[str]
    """The answer to the subquery."""

    query: Required[str]
    """The subquery that was asked."""

    sources: Required[Iterable[MessageGraphDataSubquerySource]]


class MessageGraphData(TypedDict, total=False):
    sources: Iterable[MessageGraphDataSource]

    status: Literal["processing", "finished"]

    subqueries: Iterable[MessageGraphDataSubquery]


class MessageToolCallFunction(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


class MessageToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[MessageToolCallFunction]

    type: Required[str]

    index: int


class Message(TypedDict, total=False):
    role: Required[Literal["user", "assistant", "system", "tool"]]

    content: Optional[str]

    graph_data: Optional[MessageGraphData]

    name: Optional[str]

    refusal: Optional[str]

    tool_call_id: Optional[str]

    tool_calls: Optional[Iterable[MessageToolCall]]


class StreamOptions(TypedDict, total=False):
    include_usage: Required[bool]
    """Indicate whether to include usage information."""


class ToolChoiceStringToolChoice(TypedDict, total=False):
    value: Required[Literal["none", "auto", "required"]]


class ToolChoiceJsonObjectToolChoice(TypedDict, total=False):
    value: Required[Dict[str, object]]


ToolChoice: TypeAlias = Union[ToolChoiceStringToolChoice, ToolChoiceJsonObjectToolChoice]


class ToolFunctionToolFunction(TypedDict, total=False):
    name: Required[str]
    """Name of the function"""

    description: str
    """Description of the function"""

    parameters: Dict[str, object]


class ToolFunctionTool(TypedDict, total=False):
    function: Required[ToolFunctionToolFunction]

    type: Required[Literal["function"]]
    """The type of tool."""


class ToolGraphToolFunction(TypedDict, total=False):
    graph_ids: Required[List[str]]
    """An array of graph IDs to be used in the tool."""

    subqueries: Required[bool]
    """Boolean to indicate whether to include subqueries in the response."""

    description: str
    """A description of the graph content."""


class ToolGraphTool(TypedDict, total=False):
    function: Required[ToolGraphToolFunction]

    type: Required[Literal["graph"]]
    """The type of tool."""


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
