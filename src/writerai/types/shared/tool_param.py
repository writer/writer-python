# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .function_definition import FunctionDefinition

__all__ = ["ToolParam", "FunctionTool", "GraphTool", "GraphToolFunction"]


class FunctionTool(BaseModel):
    function: FunctionDefinition

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

    type: Literal["graph"]
    """The type of tool."""


ToolParam: TypeAlias = Union[FunctionTool, GraphTool]
