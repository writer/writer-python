# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["LogprobsToken", "TopLogprob"]


class TopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class LogprobsToken(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[TopLogprob]

    bytes: Optional[List[int]] = None
