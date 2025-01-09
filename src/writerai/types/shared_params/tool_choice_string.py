# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolChoiceString"]


class ToolChoiceString(TypedDict, total=False):
    value: Required[Literal["none", "auto", "required"]]
