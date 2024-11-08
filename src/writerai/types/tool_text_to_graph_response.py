# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ToolTextToGraphResponse"]


class ToolTextToGraphResponse(BaseModel):
    graph: List[List[str]]
    """
    The graph structure generated from the input text, represented by a string array
    of entities and relationships.
    """
