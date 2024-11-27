# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .logprobs_token import LogprobsToken

__all__ = ["Logprobs"]


class Logprobs(BaseModel):
    content: Optional[List[LogprobsToken]] = None

    refusal: Optional[List[LogprobsToken]] = None
