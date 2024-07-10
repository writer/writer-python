# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ModelListResponse", "Model"]


class Model(BaseModel):
    id: str
    """The ID of the particular LLM that you want to use"""

    name: str
    """The name of the particular LLM that you want to use."""


class ModelListResponse(BaseModel):
    models: List[Model]
    """The identifier of the model to be used for processing the request."""
