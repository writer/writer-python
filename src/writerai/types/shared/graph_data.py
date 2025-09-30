# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .source import Source
from ..._models import BaseModel

__all__ = ["GraphData", "References", "ReferencesFile", "ReferencesWeb", "Subquery"]


class ReferencesFile(BaseModel):
    file_id: str = FieldInfo(alias="fileId")
    """The unique identifier of the file in your Writer account."""

    score: float
    """
    Internal score used during the retrieval process for ranking and selecting
    relevant snippets.
    """

    text: str
    """
    The exact text snippet from the source document that was used to support the
    response.
    """

    cite: Optional[str] = None
    """
    Unique citation ID that appears in inline citations within the response text
    (null if not cited).
    """

    page: Optional[int] = None
    """Page number where this snippet was found in the source document."""


class ReferencesWeb(BaseModel):
    score: float
    """
    Internal score used during the retrieval process for ranking and selecting
    relevant snippets.
    """

    text: str
    """
    The exact text snippet from the web source that was used to support the
    response.
    """

    title: str
    """The title of the web page where this content was found."""

    url: str
    """The URL of the web page where this content was found."""


class References(BaseModel):
    files: Optional[List[ReferencesFile]] = None
    """Array of file-based references from uploaded documents in the Knowledge Graph."""

    web: Optional[List[ReferencesWeb]] = None
    """Array of web-based references from online sources accessed during the query."""


class Subquery(BaseModel):
    answer: str
    """The answer to the subquery based on Knowledge Graph content."""

    query: str
    """The subquery that was generated to help answer the main question."""

    sources: List[Optional[Source]]
    """Array of source snippets that were used to answer this subquery."""


class GraphData(BaseModel):
    references: Optional[References] = None
    """
    Detailed source information organized by reference type, providing comprehensive
    metadata about the sources used to generate the response.
    """

    sources: Optional[List[Optional[Source]]] = None

    status: Optional[Literal["processing", "finished"]] = None

    subqueries: Optional[List[Optional[Subquery]]] = None
