# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["Source"]


class Source(BaseModel):
    file_id: str
    """The unique identifier of the file."""

    snippet: str
    """A snippet of text from the source file."""
