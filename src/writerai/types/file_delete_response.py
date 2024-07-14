# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["FileDeleteResponse"]


class FileDeleteResponse(BaseModel):
    id: str
    """A unique identifier of the deleted graph."""

    deleted: bool
    """Indicates whether the graph was successfully deleted."""
