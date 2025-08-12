# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.tool_call import ToolCall
from .shared.graph_data import GraphData

__all__ = ["ChatCompletionMessage", "LlmData", "TranslationData", "WebSearchData", "WebSearchDataSource"]


class LlmData(BaseModel):
    model: str
    """The model used by the tool."""

    prompt: str
    """The prompt processed by the model."""


class TranslationData(BaseModel):
    source_language_code: str
    """The language code of the source text."""

    source_text: str
    """The text the tool translated."""

    target_language_code: str
    """The language code of the target text."""


class WebSearchDataSource(BaseModel):
    raw_content: Optional[str] = None

    url: Optional[str] = None


class WebSearchData(BaseModel):
    sources: List[WebSearchDataSource]


class ChatCompletionMessage(BaseModel):
    content: str
    """The text content produced by the model.

    This field contains the actual output generated, reflecting the model's response
    to the input query or command.
    """

    refusal: Optional[str] = None

    role: Literal["assistant"]
    """Specifies the role associated with the content."""

    graph_data: Optional[GraphData] = None

    llm_data: Optional[LlmData] = None

    tool_calls: Optional[List[ToolCall]] = None

    translation_data: Optional[TranslationData] = None

    web_search_data: Optional[WebSearchData] = None
