# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["FileRetryParams"]


class FileRetryParams(TypedDict, total=False):
    file_ids: Required[List[str]]
    """The unique identifier of the files to be retried."""
