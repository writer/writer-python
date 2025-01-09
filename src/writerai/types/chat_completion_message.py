# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.tool_call import ToolCall
from .shared.graph_data import GraphData

__all__ = ["ChatCompletionMessage"]


class ChatCompletionMessage(BaseModel):
    content: str
    """The text content produced by the model.

    This field contains the actual output generated, reflecting the model's response
    to the input query or command.
    """

    refusal: Optional[str] = None

    role: Literal["assistant"]
    """Specifies the role associated with the content."""

    graph_data: Optional[GraphData] = None

    tool_calls: Optional[List[ToolCall]] = None
