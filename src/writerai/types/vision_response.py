# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["VisionResponse"]


class VisionResponse(BaseModel):
    data: str
    """The result of the image analysis."""
