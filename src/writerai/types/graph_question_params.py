# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["GraphQuestionParams"]


class GraphQuestionParams(TypedDict, total=False):
    graph_ids: Required[List[str]]
    """The unique identifiers of the Knowledge Graphs to be queried."""

    question: Required[str]
    """The question to be answered using the Knowledge Graph."""

    stream: Required[bool]
    """Determines whether the model's output should be streamed.

    If true, the output is generated and sent incrementally, which can be useful for
    real-time applications.
    """

    subqueries: Required[bool]
    """Specify whether to include subqueries."""
