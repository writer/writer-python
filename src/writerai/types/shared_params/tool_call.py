# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolCall", "Function"]


class Function(TypedDict, total=False):
    arguments: Required[str]

    name: str


class ToolCall(TypedDict, total=False):
    id: Required[str]

    function: Required[Function]

    type: Required[str]

    index: int
