# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolParsePdfParams"]


class ToolParsePdfParams(TypedDict, total=False):
    format: Required[Literal["text", "markdown"]]
    """The format into which the PDF content should be converted."""
