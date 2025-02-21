# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["JobCreateResponse"]


class JobCreateResponse(BaseModel):
    id: str
    """The unique identifier for the async job created."""

    created_at: datetime
    """The timestamp when the job was created."""

    status: Literal["in_progress", "failed", "completed"]
    """The status of the job."""
