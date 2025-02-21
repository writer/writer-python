# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .function_params import FunctionParams

__all__ = ["FunctionDefinition"]


class FunctionDefinition(BaseModel):
    name: str
    """Name of the function."""

    description: Optional[str] = None
    """Description of the function."""

    parameters: Optional[FunctionParams] = None
    """The parameters of the function."""
