# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
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


class FunctionTool(BaseModel):
    function: FunctionDefinition
    """A tool that uses a custom function."""

    type: Literal["function"]
    """The type of tool."""


class GraphToolFunction(BaseModel):
    graph_ids: List[str]
    """An array of graph IDs to be used in the tool."""

    subqueries: bool
    """Boolean to indicate whether to include subqueries in the response."""

    description: Optional[str] = None
    """A description of the graph content."""


class GraphTool(BaseModel):
    function: GraphToolFunction
    """A tool that uses Knowledge Graphs as context for responses."""

    type: Literal["graph"]
    """The type of tool."""


class LlmToolFunction(BaseModel):
    description: str
    """A description of the model to be used."""

    model: str
    """The model to be used."""


class LlmTool(BaseModel):
    function: LlmToolFunction
    """A tool that uses another Writer model to generate a response."""

    type: Literal["llm"]
    """The type of tool."""


class VisionToolFunctionVariable(BaseModel):
    file_id: str
    """The File ID of the image to be analyzed.

    The file must be uploaded to the Writer platform before you use it with the
    Vision tool.
    """

    name: str
    """The name of the file variable.

    You must reference this name in the `message.content` field of the request to
    the chat completions endpoint. Use double curly braces (`{{}}`) to reference the
    file. For example,
    `Describe the difference between the image {{image_1}} and the image {{image_2}}`.
    """


class VisionToolFunction(BaseModel):
    model: str
    """The model to be used for image analysis. Must be `palmyra-vision`."""

    variables: List[VisionToolFunctionVariable]


class VisionTool(BaseModel):
    function: VisionToolFunction
    """A tool that uses Palmyra Vision to analyze images."""

    type: Literal["vision"]
    """The type of tool."""


ToolParam: TypeAlias = Annotated[
    Union[FunctionTool, GraphTool, LlmTool, VisionTool], PropertyInfo(discriminator="type")
]
