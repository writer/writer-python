# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["JobRetryResponse"]


class JobRetryResponse(BaseModel):
    job_id: str
    """The unique identifier for the async job created."""

    application_id: Optional[str] = None
    """The ID of the application associated with this job."""

    created_at: Optional[datetime] = None
    """The timestamp when the job was created."""

    status: Optional[str] = None
    """The initial status of the job (e.g., 'queued')."""
