# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GraphUpdateParams"]


class GraphUpdateParams(TypedDict, total=False):
    description: str
    """A description of the Knowledge Graph (max 255 characters).

    Omitting this field leaves the description unchanged.
    """

    name: str
    """The name of the Knowledge Graph (max 255 characters).

    Omitting this field leaves the name unchanged.
    """
