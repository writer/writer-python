# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .application_generate_async_response import ApplicationGenerateAsyncResponse

__all__ = ["ApplicationJobsListResponse", "Pagination"]


class Pagination(BaseModel):
    limit: Optional[int] = None
    """The pagination limit for retrieving the jobs."""

    offset: Optional[int] = None
    """The pagination offset for retrieving the jobs."""


class ApplicationJobsListResponse(BaseModel):
    result: List[ApplicationGenerateAsyncResponse]

    pagination: Optional[Pagination] = None

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)
    """The total number of jobs associated with the application."""
