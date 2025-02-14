# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .source import Source

__all__ = ["GraphData", "Subquery"]


class Subquery(TypedDict, total=False):
    answer: Required[str]
    """The answer to the subquery."""

    query: Required[str]
    """The subquery that was asked."""

    sources: Required[Iterable[Optional[Source]]]


class GraphData(TypedDict, total=False):
    sources: Iterable[Optional[Source]]

    status: Optional[Literal["processing", "finished"]]

    subqueries: Iterable[Optional[Subquery]]
