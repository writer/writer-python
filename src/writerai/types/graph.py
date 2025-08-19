# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Graph", "FileStatus", "URL", "URLStatus"]


class FileStatus(BaseModel):
    completed: int
    """The number of files that have been successfully processed."""

    failed: int
    """The number of files that failed to process."""

    in_progress: int
    """The number of files currently being processed."""

    total: int
    """The total number of files associated with the Knowledge Graph."""


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


class Graph(BaseModel):
    id: str
    """The unique identifier of the Knowledge Graph."""

    created_at: datetime
    """The timestamp when the Knowledge Graph was created."""

    file_status: FileStatus
    """The processing status of files in the Knowledge Graph."""

    name: str
    """The name of the Knowledge Graph."""

    type: Literal["manual", "connector", "web"]
    """The type of Knowledge Graph.

    - `manual`: files are uploaded via UI or API
    - `connector`: files are uploaded via a data connector such as Google Drive or
      Confluence
    - `web`: URLs are connected to the Knowledge Graph
    """

    description: Optional[str] = None
    """A description of the Knowledge Graph."""

    urls: Optional[List[URL]] = None
    """An array of web connector URLs associated with this Knowledge Graph."""
