# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ToolChoiceJsonObject"]


class ToolChoiceJsonObject(TypedDict, total=False):
    value: Required[Dict[str, object]]
    """A JSON object that specifies the tool to call.

    For example, `{"type": "function", "function": {"name": "get_current_weather"}}`
    """
