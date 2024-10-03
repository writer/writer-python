# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GraphUpdateParams"]


class GraphUpdateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the graph. This can be at most 255 characters."""

    description: str
    """A description of the graph. This can be at most 255 characters."""
