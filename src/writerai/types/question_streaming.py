# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .question import Question

__all__ = ["QuestionStreaming"]


class QuestionStreaming(BaseModel):
    data: Question
