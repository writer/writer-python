# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ChatCompletionUsage", "CompletionTokensDetails", "PromptTokenDetails"]


class CompletionTokensDetails(BaseModel):
    reasoning_tokens: int


class PromptTokenDetails(BaseModel):
    cached_tokens: int


class ChatCompletionUsage(BaseModel):
    completion_tokens: int

    prompt_tokens: int

    total_tokens: int

    completion_tokens_details: Optional[CompletionTokensDetails] = None

    prompt_token_details: Optional[PromptTokenDetails] = None
