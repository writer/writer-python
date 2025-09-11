# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["Source"]


class Source(TypedDict, total=False):
    file_id: Required[str]
    """The unique identifier of the file in your Writer account."""

    snippet: Required[str]
    """
    The exact text snippet from the source document that was used to support the
    response.
    """
