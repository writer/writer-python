# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ApplicationGraphsResponse"]


class ApplicationGraphsResponse(BaseModel):
    graph_ids: List[str]
    """A list of Knowledge Graphs associated with the application."""
