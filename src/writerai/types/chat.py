# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Chat", "Choice", "ChoiceMessage"]


class ChoiceMessage(BaseModel):
    content: str

    role: Literal["user", "assistant", "system"]


class Choice(BaseModel):
    finish_reason: Literal["stop", "length", "content_filter"]

    message: ChoiceMessage


class Chat(BaseModel):
    id: str

    choices: List[Choice]

    created: int

    model: str
