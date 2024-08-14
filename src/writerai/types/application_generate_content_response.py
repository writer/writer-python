# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ApplicationGenerateContentResponse"]


class ApplicationGenerateContentResponse(BaseModel):
    suggestion: str
    """The response from the model specified in the application."""

    title: Optional[str] = None
    """The name of the output field."""
