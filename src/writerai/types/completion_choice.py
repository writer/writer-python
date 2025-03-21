# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.logprobs import Logprobs

__all__ = ["CompletionChoice"]


class CompletionChoice(BaseModel):
    text: str
    """
    The generated text output from the model, which forms the main content of the
    response.
    """

    log_probs: Optional[Logprobs] = None
