# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from ..._models import BaseModel
from .error_message import ErrorMessage

__all__ = ["ErrorObject"]


class ErrorObject(BaseModel):
    errors: List[ErrorMessage]

    extras: Dict[str, object]

    tpe: str
