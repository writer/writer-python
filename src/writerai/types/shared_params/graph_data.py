# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .source import Source
from ..._utils import PropertyInfo

__all__ = ["GraphData", "References", "ReferencesFile", "ReferencesWeb", "Subquery"]


class ReferencesFile(TypedDict, total=False):
    file_id: Required[Annotated[str, PropertyInfo(alias="fileId")]]
    """The unique identifier of the file in your Writer account."""

    score: Required[float]
    """
    Internal score used during the retrieval process for ranking and selecting
    relevant snippets.
    """

    text: Required[str]
    """
    The exact text snippet from the source document that was used to support the
    response.
    """

    cite: str
    """
    Unique citation ID that appears in inline citations within the response text
    (null if not cited).
    """

    page: int
    """Page number where this snippet was found in the source document."""


class ReferencesWeb(TypedDict, total=False):
    score: Required[float]
    """
    Internal score used during the retrieval process for ranking and selecting
    relevant snippets.
    """

    text: Required[str]
    """
    The exact text snippet from the web source that was used to support the
    response.
    """

    title: Required[str]
    """The title of the web page where this content was found."""

    url: Required[str]
    """The URL of the web page where this content was found."""


class References(TypedDict, total=False):
    files: Iterable[ReferencesFile]
    """Array of file-based references from uploaded documents in the Knowledge Graph."""

    web: Iterable[ReferencesWeb]
    """Array of web-based references from online sources accessed during the query."""


class Subquery(TypedDict, total=False):
    answer: Required[str]
    """The answer to the subquery based on Knowledge Graph content."""

    query: Required[str]
    """The subquery that was generated to help answer the main question."""

    sources: Required[Iterable[Optional[Source]]]
    """Array of source snippets that were used to answer this subquery."""


class GraphData(TypedDict, total=False):
    references: References
    """
    Detailed source information organized by reference type, providing comprehensive
    metadata about the sources used to generate the response.
    """

    sources: Iterable[Optional[Source]]

    status: Optional[Literal["processing", "finished"]]

    subqueries: Iterable[Optional[Subquery]]
