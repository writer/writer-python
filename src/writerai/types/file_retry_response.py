# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FileRetryResponse"]


class FileRetryResponse(BaseModel):
    success: Optional[bool] = None
    """Indicates whether the retry operation was successful."""
