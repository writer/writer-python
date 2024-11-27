# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .source import Source
from ..._models import BaseModel

__all__ = ["GraphData", "Subquery"]


class Subquery(BaseModel):
    answer: str
    """The answer to the subquery."""

    query: str
    """The subquery that was asked."""

    sources: List[Source]


class GraphData(BaseModel):
    sources: Optional[List[Source]] = None

    status: Optional[Literal["processing", "finished"]] = None

    subqueries: Optional[List[Subquery]] = None
