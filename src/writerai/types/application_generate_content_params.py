# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ApplicationGenerateContentParams", "Input"]


class ApplicationGenerateContentParams(TypedDict, total=False):
    inputs: Required[Iterable[Input]]


class Input(TypedDict, total=False):
    id: Required[str]

    value: Required[List[str]]
