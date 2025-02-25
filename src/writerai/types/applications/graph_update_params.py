# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["GraphUpdateParams"]


class GraphUpdateParams(TypedDict, total=False):
    graph_ids: Required[List[str]]
    """A list of Knowledge Graph IDs to associate with the application.

    Note that this will replace the existing list of Knowledge Graphs associated
    with the application, not add to it.
    """
