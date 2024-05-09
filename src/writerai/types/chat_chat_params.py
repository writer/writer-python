# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatChatParamsBase", "Message", "ChatChatParamsNonStreaming", "ChatChatParamsStreaming"]


class ChatChatParamsBase(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    model: Required[str]

    max_tokens: int

    n: int

    stop: Union[List[str], str]

    temperature: float

    top_p: float


class Message(TypedDict, total=False):
    content: Required[str]

    role: Required[Literal["user", "assistant", "system"]]

    name: str


class ChatChatParamsNonStreaming(ChatChatParamsBase):
    stream: Literal[False]


class ChatChatParamsStreaming(ChatChatParamsBase):
    stream: Required[Literal[True]]


ChatChatParams = Union[ChatChatParamsNonStreaming, ChatChatParamsStreaming]
