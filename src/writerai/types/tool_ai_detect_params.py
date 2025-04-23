# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolAIDetectParams"]


class ToolAIDetectParams(TypedDict, total=False):
    input: Required[str]
    """The content to determine if it is AI- or human-generated.

    Content must have at least 350 characters.
    """
