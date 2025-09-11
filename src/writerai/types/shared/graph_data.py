# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .source import Source
from ..._models import BaseModel

__all__ = ["GraphData", "Subquery"]


class Subquery(BaseModel):
    answer: str
    """The answer to the subquery based on Knowledge Graph content."""

    query: str
    """The subquery that was generated to help answer the main question."""

    sources: List[Optional[Source]]
    """Array of source snippets that were used to answer this subquery."""


class GraphData(BaseModel):
    sources: Optional[List[Optional[Source]]] = None

    status: Optional[Literal["processing", "finished"]] = None

    subqueries: Optional[List[Optional[Subquery]]] = None
