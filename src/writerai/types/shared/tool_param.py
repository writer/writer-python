# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .function_definition import FunctionDefinition

__all__ = [
    "ToolParam",
    "FunctionTool",
    "GraphTool",
    "GraphToolFunction",
    "GraphToolFunctionQueryConfig",
    "LlmTool",
    "LlmToolFunction",
    "TranslationTool",
    "TranslationToolFunction",
    "VisionTool",
    "VisionToolFunction",
    "VisionToolFunctionVariable",
    "WebSearchTool",
    "WebSearchToolFunction",
]


class FunctionTool(BaseModel):
    function: FunctionDefinition
    """A tool that uses a custom function."""

    type: Literal["function"]
    """The type of tool."""


class GraphToolFunctionQueryConfig(BaseModel):
    grounding_level: Optional[float] = None
    """
    Level of grounding required for responses, controlling how closely answers must
    be tied to source material. Set lower for grounded outputs, higher for
    creativity. Higher values (closer to 1.0) allow more creative interpretation,
    while lower values (closer to 0.0) stick more closely to source material. Range:
    0.0-1.0, Default: 0.0.
    """

    inline_citations: Optional[bool] = None
    """
    Whether to include inline citations in the response, showing which Knowledge
    Graph sources were used. Default: false.
    """

    keyword_threshold: Optional[float] = None
    """Threshold for keyword-based matching when searching Knowledge Graph content.

    Set higher for stricter relevance, lower for broader range. Higher values
    (closer to 1.0) require stronger keyword matches, while lower values (closer to
    0.0) allow more lenient matching. Range: 0.0-1.0, Default: 0.7.
    """

    max_snippets: Optional[int] = None
    """Maximum number of text snippets to retrieve from the Knowledge Graph for
    context.

    Works in concert with `search_weight` to control best matches vs broader
    coverage. While technically supports 1-60, values below 5 may return no results
    due to RAG implementation. Recommended range: 5-25. Due to RAG system behavior,
    you may see more snippets than requested. Range: 1-60, Default: 30.
    """

    max_subquestions: Optional[int] = None
    """Maximum number of subquestions to generate when processing complex queries.

    Set higher to improve detail, set lower to reduce response time. Range: 1-10,
    Default: 6.
    """

    max_tokens: Optional[int] = None
    """Maximum number of tokens the model can generate in the response.

    This controls the length of the AI's answer. Set higher for longer answers, set
    lower for shorter, faster answers. Range: 100-8000, Default: 4000.
    """

    search_weight: Optional[int] = None
    """Weight given to search results when ranking and selecting relevant information.

    Higher values (closer to 100) prioritize keyword-based matching, while lower
    values (closer to 0) prioritize semantic similarity matching. Use higher values
    for exact keyword searches, lower values for conceptual similarity searches.
    Range: 0-100, Default: 50.
    """

    semantic_threshold: Optional[float] = None
    """
    Threshold for semantic similarity matching when searching Knowledge Graph
    content. Set higher for stricter relevance, lower for broader range. Higher
    values (closer to 1.0) require stronger semantic similarity, while lower values
    (closer to 0.0) allow more lenient semantic matching. Range: 0.0-1.0, Default:
    0.7.
    """


class GraphToolFunction(BaseModel):
    graph_ids: List[str]
    """An array of graph IDs to use in the tool."""

    subqueries: bool
    """Boolean to indicate whether to include subqueries in the response."""

    description: Optional[str] = None
    """A description of the graph content."""

    query_config: Optional[GraphToolFunctionQueryConfig] = None
    """
    Configuration options for Knowledge Graph queries, including search parameters
    and citation settings.
    """


class GraphTool(BaseModel):
    function: GraphToolFunction
    """A tool that uses Knowledge Graphs as context for responses."""

    type: Literal["graph"]
    """The type of tool."""


class LlmToolFunction(BaseModel):
    description: str
    """A description of the model to use."""

    model: str
    """The model to use."""


class LlmTool(BaseModel):
    function: LlmToolFunction
    """A tool that uses another Writer model to generate a response."""

    type: Literal["llm"]
    """The type of tool."""


class TranslationToolFunction(BaseModel):
    formality: bool
    """Whether to use formal or informal language in the translation.

    See the
    [list of languages that support formality](https://dev.writer.com/api-reference/translation-api/language-support#formality).
    If the language does not support formality, this parameter is ignored.
    """

    length_control: bool
    """Whether to control the length of the translated text.

    See the
    [list of languages that support length control](https://dev.writer.com/api-reference/translation-api/language-support#length-control).
    If the language does not support length control, this parameter is ignored.
    """

    mask_profanity: bool
    """Whether to mask profane words in the translated text.

    See the
    [list of languages that do not support profanity masking](https://dev.writer.com/api-reference/translation-api/language-support#profanity-masking).
    If the language does not support profanity masking, this parameter is ignored.
    """

    model: Literal["palmyra-translate"]
    """The model to use for translation."""

    source_language_code: Optional[str] = None
    """Optional.

    The [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
    language code of the original text to translate. For example, `en` for English,
    `zh` for Chinese, `fr` for French, `es` for Spanish. If the language has a
    variant, the code appends the two-digit
    [ISO-3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
    If you do not provide a language code, the LLM detects the language of the text.
    """

    target_language_code: Optional[str] = None
    """Optional.

    The [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
    language code of the target language for the translation. For example, `en` for
    English, `zh` for Chinese, `fr` for French, `es` for Spanish. If the language
    has a variant, the code appends the two-digit
    [ISO-3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
    If you do not provide a language code, the LLM uses the content of the chat
    message to determine the target language.
    """


class TranslationTool(BaseModel):
    function: TranslationToolFunction
    """A tool that uses Palmyra Translate to translate text."""

    type: Literal["translation"]
    """The type of tool."""


class VisionToolFunctionVariable(BaseModel):
    file_id: str
    """The File ID of the image to analyze.

    The file must be uploaded to the Writer platform before you use it with the
    Vision tool. The maximum allowed file size is 7MB.
    """

    name: str
    """The name of the file variable.

    You must reference this name in the `message.content` field of the request to
    the chat completions endpoint. Use double curly braces (`{{}}`) to reference the
    file. For example,
    `Describe the difference between the image {{image_1}} and the image {{image_2}}`.
    """


class VisionToolFunction(BaseModel):
    model: Literal["palmyra-vision"]
    """The model to use for image analysis."""

    variables: List[VisionToolFunctionVariable]


class VisionTool(BaseModel):
    function: VisionToolFunction
    """A tool that uses Palmyra Vision to analyze images."""

    type: Literal["vision"]
    """The type of tool."""


class WebSearchToolFunction(BaseModel):
    exclude_domains: List[str]
    """An array of domains to exclude from the search results."""

    include_domains: List[str]
    """An array of domains to include in the search results."""


class WebSearchTool(BaseModel):
    function: WebSearchToolFunction
    """A tool that uses web search to find information."""

    type: Literal["web_search"]
    """The type of tool."""


ToolParam: TypeAlias = Annotated[
    Union[FunctionTool, GraphTool, LlmTool, TranslationTool, VisionTool, WebSearchTool],
    PropertyInfo(discriminator="type"),
]
