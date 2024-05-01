# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ModelListResponse", "Model"]


class Model(BaseModel):
    id: str

    name: str


class ModelListResponse(BaseModel):
    models: List[Model]
