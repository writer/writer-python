# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ToolCallStreaming", "Function"]


class Function(BaseModel):
    arguments: str

    name: Optional[str] = None


class ToolCallStreaming(BaseModel):
    index: int

    id: Optional[str] = None

    function: Optional[Function] = None

    type: Optional[Literal["function"]] = None
