# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..application_generate_content_response import ApplicationGenerateContentResponse

__all__ = ["ApplicationGenerateAsyncResponse"]


class ApplicationGenerateAsyncResponse(BaseModel):
    id: str
    """The unique identifier for the job."""

    application_id: str
    """The ID of the application associated with this job."""

    created_at: datetime
    """The timestamp when the job was created."""

    status: Literal["in_progress", "failed", "completed"]
    """The status of the job."""

    completed_at: Optional[datetime] = None
    """The timestamp when the job was completed."""

    data: Optional[ApplicationGenerateContentResponse] = None
    """The result of the completed job, if applicable."""

    error: Optional[str] = None
    """The error message if the job failed."""

    updated_at: Optional[datetime] = None
    """The timestamp when the job was last updated."""
