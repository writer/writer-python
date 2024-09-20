# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    after: str
    """The ID of the last object in the previous page.

    This parameter instructs the API to return the next page of results.
    """

    before: str
    """The ID of the first object in the previous page.

    This parameter instructs the API to return the previous page of results.
    """

    graph_id: str
    """The unique identifier of the graph to which the files belong."""

    limit: int
    """Specifies the maximum number of objects returned in a page.

    The default value is 50. The minimum value is 1, and the maximum value is 100.
    """

    order: Literal["asc", "desc"]
    """Specifies the order of the results.

    Valid values are asc for ascending and desc for descending.
    """

    status: Literal["in_progress", "completed", "failed"]
    """Specifies the status of the files to retrieve.

    Valid values are in_progress, completed or failed.
    """
