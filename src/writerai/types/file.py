# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    id: str

    created_at: datetime

    graph_ids: List[str]

    name: str
