# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["GraphListParams"]


class GraphListParams(TypedDict, total=False):
    after: str

    before: str

    limit: int

    order: Literal["asc", "desc"]
