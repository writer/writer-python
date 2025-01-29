# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["JobRetrieveResponse", "Job"]


class Job(BaseModel):
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


class JobRetrieveResponse(BaseModel):
    jobs: List[Job]
    """A list of jobs associated with the application."""
