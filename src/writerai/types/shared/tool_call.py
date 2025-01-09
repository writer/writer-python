# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ToolCall", "Function"]


class Function(BaseModel):
    arguments: str

    name: Optional[str] = None


class ToolCall(BaseModel):
    id: str

    function: Function

    type: str

    index: Optional[int] = None
