# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GraphCreateParams"]


class GraphCreateParams(TypedDict, total=False):
    description: str
    """A description of the graph. This can be at most 255 characters."""

    name: str
    """The name of the graph. This can be at most 255 characters."""
