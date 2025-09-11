# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["GraphQuestionParamsBase", "QueryConfig", "GraphQuestionParamsNonStreaming", "GraphQuestionParamsStreaming"]


class GraphQuestionParamsBase(TypedDict, total=False):
    graph_ids: Required[SequenceNotStr[str]]
    """The unique identifiers of the Knowledge Graphs to query."""

    question: Required[str]
    """The question to answer using the Knowledge Graph."""

    query_config: QueryConfig
    """
    Configuration options for Knowledge Graph queries, including search parameters
    and citation settings.
    """

    subqueries: bool
    """Specify whether to include subqueries."""


class QueryConfig(TypedDict, total=False):
    grounding_level: float
    """
    Level of grounding required for responses, controlling how closely answers must
    be tied to source material. Set lower for grounded outputs, higher for
    creativity. Higher values (closer to 1.0) allow more creative interpretation,
    while lower values (closer to 0.0) stick more closely to source material. Range:
    0.0-1.0, Default: 0.0.
    """

    inline_citations: bool
    """
    Whether to include inline citations in the response, showing which Knowledge
    Graph sources were used. Default: false.
    """

    keyword_threshold: float
    """Threshold for keyword-based matching when searching Knowledge Graph content.

    Set higher for stricter relevance, lower for broader range. Higher values
    (closer to 1.0) require stronger keyword matches, while lower values (closer to
    0.0) allow more lenient matching. Range: 0.0-1.0, Default: 0.7.
    """

    max_snippets: int
    """Maximum number of text snippets to retrieve from the Knowledge Graph for
    context.

    Works in concert with `search_weight` to control best matches vs broader
    coverage. While technically supports 1-60, values below 5 may return no results
    due to RAG implementation. Recommended range: 5-25. Due to RAG system behavior,
    you may see more snippets than requested. Range: 1-60, Default: 30.
    """

    max_subquestions: int
    """Maximum number of subquestions to generate when processing complex queries.

    Set higher to improve detail, set lower to reduce response time. Range: 1-10,
    Default: 6.
    """

    max_tokens: int
    """Maximum number of tokens the model can generate in the response.

    This controls the length of the AI's answer. Set higher for longer answers, set
    lower for shorter, faster answers. Range: 100-8000, Default: 4000.
    """

    search_weight: int
    """Weight given to search results when ranking and selecting relevant information.

    Higher values (closer to 100) prioritize keyword-based matching, while lower
    values (closer to 0) prioritize semantic similarity matching. Use higher values
    for exact keyword searches, lower values for conceptual similarity searches.
    Range: 0-100, Default: 50.
    """

    semantic_threshold: float
    """
    Threshold for semantic similarity matching when searching Knowledge Graph
    content. Set higher for stricter relevance, lower for broader range. Higher
    values (closer to 1.0) require stronger semantic similarity, while lower values
    (closer to 0.0) allow more lenient semantic matching. Range: 0.0-1.0, Default:
    0.7.
    """


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
