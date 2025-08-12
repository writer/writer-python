# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ToolWebSearchResponse", "Source"]


class Source(BaseModel):
    raw_content: Optional[str] = None
    """Raw content from the source URL.

    Not included if `include_raw_content` is `false`.
    """

    url: Optional[str] = None
    """URL of the search result."""


class ToolWebSearchResponse(BaseModel):
    query: str
    """The search query that was submitted."""

    sources: List[Source]
    """The search results found."""

    answer: Optional[str] = None
    """Generated answer based on the search results.

    Not included if `include_answer` is `false`.
    """
