# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["JobCreateParams", "Input"]


class JobCreateParams(TypedDict, total=False):
    inputs: Required[Iterable[Input]]
    """A list of input objects to generate content for."""

    metadata: Dict[str, str]
    """Optional metadata for the generation request."""


class Input(TypedDict, total=False):
    content: str
    """The input content to be processed."""

    input_id: str
    """A unique identifier for the input object."""
