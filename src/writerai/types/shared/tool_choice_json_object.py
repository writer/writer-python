# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ..._models import BaseModel

__all__ = ["ToolChoiceJsonObject"]


class ToolChoiceJsonObject(BaseModel):
    value: Dict[str, object]
    """A JSON object that specifies the tool to call.

    For example, `{"type": "function", "function": {"name": "get_current_weather"}}`
    """
