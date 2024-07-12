# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["GraphListParams"]


class GraphListParams(TypedDict, total=False):
    after: str
    """The ID of the last object in the previous page.

    This parameter instructs the API to return the next page of results.
    """

    before: str
    """The ID of the first object in the previous page.

    This parameter instructs the API to return the previous page of results.
    """

    limit: int
    """Specifies the maximum number of objects returned in a page.

    The default value is 50. The minimum value is 1, and the maximum value is 100.
    """

    order: Literal["asc", "desc"]
    """Specifies the order of the results.

    Valid values are asc for ascending and desc for descending.
    """
