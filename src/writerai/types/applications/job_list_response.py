# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["JobListResponse"]


class JobListResponse(BaseModel):
    created_at: Optional[datetime] = None
    """The timestamp when the job was created."""

    job_id: Optional[str] = None
    """The unique identifier for the job."""

    result: Optional[str] = None
    """The result of the completed job, if applicable."""

    status: Optional[str] = None
    """The current status of the job."""

    updated_at: Optional[datetime] = None
    """The timestamp when the job was last updated."""
