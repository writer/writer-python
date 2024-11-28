# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .chat import Chat

__all__ = ["ChatStreamingData"]


class ChatStreamingData(BaseModel):
    data: Chat
