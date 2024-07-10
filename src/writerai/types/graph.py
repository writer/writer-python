# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Graph", "FileStatus"]


class FileStatus(BaseModel):
    completed: int

    failed: int

    in_progress: int

    total: int


class Graph(BaseModel):
    id: str

    created_at: datetime

    file_status: FileStatus

    name: str

    description: Optional[str] = None
