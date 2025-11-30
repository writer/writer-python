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
    """A list of Knowledge Graph IDs that the file is associated with.

    If you provided a `graphId` during upload, the file is associated with that
    Knowledge Graph. However, the `graph_ids` field in the upload response is an
    empty list. The association will be visible in the `graph_ids` list when you
    retrieve the file using the file retrieval endpoint.
    """

    name: str
    """The name of the file."""

    status: str
    """The processing status of the file."""
