# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GraphUpdateResponse", "URL", "URLStatus"]


class URLStatus(BaseModel):
    status: Literal["validating", "success", "error"]
    """The current status of the URL processing."""

    error_type: Optional[
        Literal["invalid_url", "not_searchable", "not_found", "paywall_or_login_page", "unexpected_error"]
    ] = None
    """The type of error that occurred during processing, if any."""


class URL(BaseModel):
    status: URLStatus
    """The current status of the URL processing."""

    type: Literal["single_page", "sub_pages"]
    """The type of web connector processing for this URL."""

    url: str
    """The URL to be processed by the web connector."""

    exclude_urls: Optional[List[str]] = None
    """An array of URLs to exclude from processing within this web connector."""


class GraphUpdateResponse(BaseModel):
    id: str
    """A unique identifier of the Knowledge Graph."""

    created_at: datetime
    """The timestamp when the Knowledge Graph was created."""

    name: str
    """The name of the Knowledge Graph (max 255 characters)."""

    description: Optional[str] = None
    """A description of the Knowledge Graph (max 255 characters)."""

    urls: Optional[List[URL]] = None
    """An array of web connector URLs associated with this Knowledge Graph."""
