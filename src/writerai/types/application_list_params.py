# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ApplicationListParams"]


class ApplicationListParams(TypedDict, total=False):
    after: str
    """Return results after this application ID for pagination."""

    before: str
    """Return results before this application ID for pagination."""

    limit: int
    """Maximum number of applications to return in the response."""

    order: Literal["asc", "desc"]
    """Sort order for the results based on creation time."""

    type: Literal["generation"]
    """Filter applications by their type."""
