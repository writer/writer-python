# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .chat_completion import ChatCompletion

__all__ = ["ChatStreamingData"]


class ChatStreamingData(BaseModel):
    data: ChatCompletion
