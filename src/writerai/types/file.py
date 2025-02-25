# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    id: str
    """A unique identifier of the file."""

    created_at: datetime
    """The timestamp when the file was uploaded."""

    graph_ids: List[str]
    """A list of Knowledge Graph IDs that the file is associated with."""

    name: str
    """The name of the file."""

    status: str
    """The processing status of the file."""
