# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolContextAwareSplittingParams"]


class ToolContextAwareSplittingParams(TypedDict, total=False):
    strategy: Required[Literal["llm_split", "fast_split", "hybrid_split"]]
    """The strategy to be used for splitting the text into chunks.

    `llm_split` uses the language model to split the text, `fast_split` uses a fast
    heuristic-based approach, and `hybrid_split` combines both strategies.
    """

    text: Required[str]
    """The text to be split into chunks."""
