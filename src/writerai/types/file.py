# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    id: str
    """A unique identifier of the graph."""

    created_at: datetime
    """The timestamp when the graph was created."""

    graph_ids: List[str]
    """A list of graph IDs that the file is associated with."""

    name: str
    """The name of the graph."""
