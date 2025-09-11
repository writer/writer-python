# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["GraphUpdateParams", "URL"]


class GraphUpdateParams(TypedDict, total=False):
    description: str
    """A description of the Knowledge Graph (max 255 characters).

    Omitting this field leaves the description unchanged.
    """

    name: str
    """The name of the Knowledge Graph (max 255 characters).

    Omitting this field leaves the name unchanged.
    """

    urls: Iterable[URL]
    """An array of web connector URLs to update for this Knowledge Graph.

    You can only connect URLs to Knowledge Graphs with the type `web`. To clear the
    list of URLs, set this field to an empty array.
    """


class URL(TypedDict, total=False):
    type: Required[Literal["single_page", "sub_pages"]]
    """The type of web connector processing for this URL."""

    url: Required[str]
    """The URL to be processed by the web connector."""

    exclude_urls: SequenceNotStr[str]
    """An array of URLs to exclude from processing within this web connector."""
