# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Completion", "Choice", "ChoiceLogProbs", "ChoiceLogProbsTopLogProb"]


class ChoiceLogProbsTopLogProb(BaseModel):
    additional_properties: Optional[float] = None


class ChoiceLogProbs(BaseModel):
    text_offset: Optional[List[int]] = None

    token_log_probs: Optional[List[float]] = None

    tokens: Optional[List[str]] = None

    top_log_probs: Optional[List[ChoiceLogProbsTopLogProb]] = None


class Choice(BaseModel):
    text: str

    log_probs: Optional[ChoiceLogProbs] = None


class Completion(BaseModel):
    choices: List[Choice]

    model: Optional[str] = None
