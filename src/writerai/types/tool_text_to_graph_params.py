# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolTextToGraphParams"]


class ToolTextToGraphParams(TypedDict, total=False):
    text: Required[str]
    """The text to be converted into a graph structure. Maximum of 35000 words."""
