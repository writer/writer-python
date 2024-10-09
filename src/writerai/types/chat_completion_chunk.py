# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ChatCompletionChunk",
    "Choice",
    "ChoiceDelta",
    "ChoiceDeltaGraphData",
    "ChoiceDeltaGraphDataSource",
    "ChoiceDeltaGraphDataSubquery",
    "ChoiceDeltaGraphDataSubquerySource",
    "ChoiceDeltaToolCall",
    "ChoiceDeltaToolCallFunction",
    "ChoiceLogprobs",
    "ChoiceLogprobsContent",
    "ChoiceLogprobsContentTopLogprob",
    "ChoiceLogprobsRefusal",
    "ChoiceLogprobsRefusalTopLogprob",
    "ChoiceMessage",
    "ChoiceMessageGraphData",
    "ChoiceMessageGraphDataSource",
    "ChoiceMessageGraphDataSubquery",
    "ChoiceMessageGraphDataSubquerySource",
    "ChoiceMessageToolCall",
    "ChoiceMessageToolCallFunction",
    "Usage",
    "UsageCompletionTokensDetails",
    "UsagePromptTokenDetails",
]


class ChoiceDeltaGraphDataSource(BaseModel):
    file_id: str
    """The unique identifier of the file."""

    snippet: str
    """A snippet of text from the source file."""


class ChoiceDeltaGraphDataSubquerySource(BaseModel):
    file_id: str
    """The unique identifier of the file."""

    snippet: str
    """A snippet of text from the source file."""


class ChoiceDeltaGraphDataSubquery(BaseModel):
    answer: str
    """The answer to the subquery."""

    query: str
    """The subquery that was asked."""

    sources: List[ChoiceDeltaGraphDataSubquerySource]


class ChoiceDeltaGraphData(BaseModel):
    sources: Optional[List[ChoiceDeltaGraphDataSource]] = None

    status: Optional[Literal["processing", "finished"]] = None

    subqueries: Optional[List[ChoiceDeltaGraphDataSubquery]] = None


class ChoiceDeltaToolCallFunction(BaseModel):
    arguments: str

    name: str


class ChoiceDeltaToolCall(BaseModel):
    index: int

    id: Optional[str] = None

    function: Optional[ChoiceDeltaToolCallFunction] = None

    type: Optional[str] = None


class ChoiceDelta(BaseModel):
    content: Optional[str] = None
    """The text content produced by the model.

    This field contains the actual output generated, reflecting the model's response
    to the input query or command.
    """

    graph_data: Optional[ChoiceDeltaGraphData] = None

    refusal: Optional[str] = None

    role: Optional[Literal["user", "assistant", "system"]] = None
    """
    Specifies the role associated with the content, indicating whether the message
    is from the 'assistant' or another defined role, helping to contextualize the
    output within the interaction flow.
    """

    tool_calls: Optional[List[ChoiceDeltaToolCall]] = None


class ChoiceLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class ChoiceLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChoiceLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChoiceLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None


class ChoiceLogprobs(BaseModel):
    content: Optional[List[ChoiceLogprobsContent]] = None

    refusal: Optional[List[ChoiceLogprobsRefusal]] = None


class ChoiceMessageGraphDataSource(BaseModel):
    file_id: str
    """The unique identifier of the file."""

    snippet: str
    """A snippet of text from the source file."""


class ChoiceMessageGraphDataSubquerySource(BaseModel):
    file_id: str
    """The unique identifier of the file."""

    snippet: str
    """A snippet of text from the source file."""


class ChoiceMessageGraphDataSubquery(BaseModel):
    answer: str
    """The answer to the subquery."""

    query: str
    """The subquery that was asked."""

    sources: List[ChoiceMessageGraphDataSubquerySource]


class ChoiceMessageGraphData(BaseModel):
    sources: Optional[List[ChoiceMessageGraphDataSource]] = None

    status: Optional[Literal["processing", "finished"]] = None

    subqueries: Optional[List[ChoiceMessageGraphDataSubquery]] = None


class ChoiceMessageToolCallFunction(BaseModel):
    arguments: str

    name: str


class ChoiceMessageToolCall(BaseModel):
    id: str

    function: ChoiceMessageToolCallFunction

    type: str

    index: Optional[int] = None


class ChoiceMessage(BaseModel):
    content: str
    """The text content produced by the model.

    This field contains the actual output generated, reflecting the model's response
    to the input query or command.
    """

    refusal: str

    role: Literal["assistant"]
    """Specifies the role associated with the content."""

    graph_data: Optional[ChoiceMessageGraphData] = None

    tool_calls: Optional[List[ChoiceMessageToolCall]] = None


class Choice(BaseModel):
    delta: ChoiceDelta
    """A chat completion delta generated by streamed model responses."""

    finish_reason: Literal["stop", "length", "content_filter", "tool_calls"]
    """Describes the condition under which the model ceased generating content.

    Common reasons include 'length' (reached the maximum output size), 'stop'
    (encountered a stop sequence), 'content_filter' (harmful content filtered out),
    or 'tool_calls' (encountered tool calls).
    """

    index: int
    """The index of the choice in the list of completions generated by the model."""

    logprobs: Optional[ChoiceLogprobs] = None
    """Log probability information for the choice."""

    message: Optional[ChoiceMessage] = None
    """The chat completion message from the model.

    Note: this field is deprecated for streaming. Use `delta` instead.
    """


class UsageCompletionTokensDetails(BaseModel):
    reasoning_tokens: int


class UsagePromptTokenDetails(BaseModel):
    cached_tokens: int


class Usage(BaseModel):
    completion_tokens: int

    prompt_tokens: int

    total_tokens: int

    completion_tokens_details: Optional[UsageCompletionTokensDetails] = None

    prompt_token_details: Optional[UsagePromptTokenDetails] = None


class ChatCompletionChunk(BaseModel):
    id: str
    """A globally unique identifier (UUID) for the response generated by the API.

    This ID can be used to reference the specific operation or transaction within
    the system for tracking or debugging purposes.
    """

    choices: List[Choice]
    """
    An array of objects representing the different outcomes or results produced by
    the model based on the input provided.
    """

    created: int
    """The Unix timestamp (in seconds) when the response was created.

    This timestamp can be used to verify the timing of the response relative to
    other events or operations.
    """

    model: str
    """Identifies the specific model used to generate the response."""

    object: str
    """
    The type of object returned, which is always `chat.completion.chunk` for
    streaming chat responses.
    """

    service_tier: Optional[str] = None

    system_fingerprint: Optional[str] = None

    usage: Optional[Usage] = None
    """Usage information for the chat completion response.

    Please note that at this time Knowledge Graph tool usage is not included in this
    object.
    """
