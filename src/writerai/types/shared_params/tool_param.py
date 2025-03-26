# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .function_definition import FunctionDefinition

__all__ = [
    "ToolParam",
    "FunctionTool",
    "GraphTool",
    "GraphToolFunction",
    "LlmTool",
    "LlmToolFunction",
    "VisionTool",
    "VisionToolFunction",
    "VisionToolFunctionVariable",
]


class FunctionTool(TypedDict, total=False):
    function: Required[FunctionDefinition]
    """A tool that uses a custom function."""

    type: Required[Literal["function"]]
    """The type of tool."""


class GraphToolFunction(TypedDict, total=False):
    graph_ids: Required[List[str]]
    """An array of graph IDs to be used in the tool."""

    subqueries: Required[bool]
    """Boolean to indicate whether to include subqueries in the response."""

    description: str
    """A description of the graph content."""


class GraphTool(TypedDict, total=False):
    function: Required[GraphToolFunction]
    """A tool that uses Knowledge Graphs as context for responses."""

    type: Required[Literal["graph"]]
    """The type of tool."""


class LlmToolFunction(TypedDict, total=False):
    description: Required[str]
    """A description of the model to be used."""

    model: Required[str]
    """The model to be used."""


class LlmTool(TypedDict, total=False):
    function: Required[LlmToolFunction]
    """A tool that uses another Writer model to generate a response."""

    type: Required[Literal["llm"]]
    """The type of tool."""


class VisionToolFunctionVariable(TypedDict, total=False):
    file_id: Required[str]
    """The File ID of the image to be analyzed.

    The file must be uploaded to the Writer platform before you use it with the
    Vision tool.
    """

    name: Required[str]
    """The name of the file variable.

    You must reference this name in the `message.content` field of the request to
    the chat completions endpoint. Use double curly braces (`{{}}`) to reference the
    file. For example,
    `Describe the difference between the image {{image_1}} and the image {{image_2}}`.
    """


class VisionToolFunction(TypedDict, total=False):
    model: Required[str]
    """The model to be used for image analysis. Must be `palmyra-vision`."""

    variables: Required[Iterable[VisionToolFunctionVariable]]


class VisionTool(TypedDict, total=False):
    function: Required[VisionToolFunction]
    """A tool that uses Palmyra Vision to analyze images."""

    type: Required[Literal["vision"]]
    """The type of tool."""


ToolParam: TypeAlias = Union[FunctionTool, GraphTool, LlmTool, VisionTool]
