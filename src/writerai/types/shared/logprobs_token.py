# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["LogprobsToken", "TopLogprob"]


class TopLogprob(BaseModel):
    """
    An array of mappings for each token to its top log probabilities, showing detailed prediction probabilities.
    """

    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class LogprobsToken(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[TopLogprob]

    bytes: Optional[List[int]] = None
