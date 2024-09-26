# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Question", "Source", "Subquery", "SubquerySource"]


class Source(BaseModel):
    file_id: str
    """The unique identifier of the file."""

    snippet: str
    """A snippet of text from the source file."""


class SubquerySource(BaseModel):
    file_id: str
    """The unique identifier of the file."""

    snippet: str
    """A snippet of text from the source file."""


class Subquery(BaseModel):
    answer: str
    """The answer to the subquery."""

    query: str
    """The subquery that was asked."""

    sources: List[SubquerySource]


class Question(BaseModel):
    answer: str
    """The answer to the question."""

    question: str
    """The question that was asked."""

    sources: List[Source]

    subqueries: Optional[List[Subquery]] = None
