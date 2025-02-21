# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["JobListParams"]


class JobListParams(TypedDict, total=False):
    limit: int
    """The pagination limit for retrieving the jobs."""

    offset: int
    """The pagination offset for retrieving the jobs."""

    status: Literal["in_progress", "failed", "completed"]
    """The status of the job."""
