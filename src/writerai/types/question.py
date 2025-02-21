# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.source import Source

__all__ = ["Question", "Subquery"]


class Subquery(BaseModel):
    answer: str
    """The answer to the subquery."""

    query: str
    """The subquery that was asked."""

    sources: List[Optional[Source]]


class Question(BaseModel):
    answer: str
    """The answer to the question."""

    question: str
    """The question that was asked."""

    sources: List[Optional[Source]]

    subqueries: Optional[List[Optional[Subquery]]] = None
