# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["GraphUpdateResponse"]


class GraphUpdateResponse(BaseModel):
    id: str
    """A unique identifier of the Knowledge Graph."""

    created_at: datetime
    """The timestamp when the Knowledge Graph was created."""

    name: str
    """The name of the Knowledge Graph (max 255 characters)."""

    description: Optional[str] = None
    """A description of the Knowledge Graph (max 255 characters)."""
