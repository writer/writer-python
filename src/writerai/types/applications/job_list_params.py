# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JobListParams", "Status", "StatusJob"]


class JobListParams(TypedDict, total=False):
    limit: int

    offset: int

    status: Status


class StatusJob(TypedDict, total=False):
    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The timestamp when the job was created."""

    job_id: str
    """The unique identifier for the job."""

    result: str
    """The result of the completed job, if applicable."""

    status: str
    """The current status of the job."""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The timestamp when the job was last updated."""


class Status(TypedDict, total=False):
    jobs: Required[Iterable[StatusJob]]
    """A list of jobs associated with the application."""
