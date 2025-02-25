# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Graph", "FileStatus"]


class FileStatus(BaseModel):
    completed: int
    """The number of files that have been successfully processed."""

    failed: int
    """The number of files that failed to process."""

    in_progress: int
    """The number of files currently being processed."""

    total: int
    """The total number of files associated with the Knowledge Graph."""


class Graph(BaseModel):
    id: str
    """The unique identifier of the Knowledge Graph."""

    created_at: datetime
    """The timestamp when the Knowledge Graph was created."""

    file_status: FileStatus

    name: str
    """The name of the Knowledge Graph."""

    type: Literal["manual", "connector"]
    """
    The type of Knowledge Graph, either `manual` (files are uploaded via UI or API)
    or `connector` (files are uploaded via a connector).
    """

    description: Optional[str] = None
    """A description of the Knowledge Graph."""
