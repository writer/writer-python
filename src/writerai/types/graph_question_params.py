# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["GraphQuestionParamsBase", "GraphQuestionParamsNonStreaming", "GraphQuestionParamsStreaming"]


class GraphQuestionParamsBase(TypedDict, total=False):
    graph_ids: Required[List[str]]
    """The unique identifiers of the Knowledge Graphs to be queried."""

    question: Required[str]
    """The question to be answered using the Knowledge Graph."""

    subqueries: bool
    """Specify whether to include subqueries."""


class GraphQuestionParamsNonStreaming(GraphQuestionParamsBase, total=False):
    stream: Literal[False]
    """Determines whether the model's output should be streamed.

    If true, the output is generated and sent incrementally, which can be useful for
    real-time applications.
    """


class GraphQuestionParamsStreaming(GraphQuestionParamsBase):
    stream: Required[Literal[True]]
    """Determines whether the model's output should be streamed.

    If true, the output is generated and sent incrementally, which can be useful for
    real-time applications.
    """


GraphQuestionParams = Union[GraphQuestionParamsNonStreaming, GraphQuestionParamsStreaming]
