# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["Source"]


class Source(BaseModel):
    file_id: str
    """The unique identifier of the file in your Writer account."""

    snippet: str
    """
    The exact text snippet from the source document that was used to support the
    response.
    """
