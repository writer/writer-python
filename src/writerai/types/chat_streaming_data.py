# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .chat import Chat
from .._models import BaseModel

__all__ = ["ChatStreamingData"]


class ChatStreamingData(BaseModel):
    data: Chat
