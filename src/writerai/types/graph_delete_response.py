# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["GraphDeleteResponse"]


class GraphDeleteResponse(BaseModel):
    id: str
    """A unique identifier of the deleted Knowledge Graph."""

    deleted: bool
    """Indicates whether the Knowledge Graph was successfully deleted."""
