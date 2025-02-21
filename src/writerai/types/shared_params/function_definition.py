# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .function_params import FunctionParams

__all__ = ["FunctionDefinition"]


class FunctionDefinition(TypedDict, total=False):
    name: Required[str]
    """Name of the function."""

    description: str
    """Description of the function."""

    parameters: FunctionParams
    """The parameters of the function."""
