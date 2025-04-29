# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .function_definition import FunctionDefinition

__all__ = [
    "ToolParam",
    "FunctionTool",
    "GraphTool",
    "GraphToolFunction",
    "LlmTool",
    "LlmToolFunction",
    "TranslationTool",
    "TranslationToolFunction",
    "VisionTool",
    "VisionToolFunction",
    "VisionToolFunctionVariable",
]


class FunctionTool(TypedDict, total=False):
    function: Required[FunctionDefinition]
    """A tool that uses a custom function."""

    type: Required[Literal["function"]]
    """The type of tool."""


class GraphToolFunction(TypedDict, total=False):
    graph_ids: Required[List[str]]
    """An array of graph IDs to use in the tool."""

    subqueries: Required[bool]
    """Boolean to indicate whether to include subqueries in the response."""

    description: str
    """A description of the graph content."""


class GraphTool(TypedDict, total=False):
    function: Required[GraphToolFunction]
    """A tool that uses Knowledge Graphs as context for responses."""

    type: Required[Literal["graph"]]
    """The type of tool."""


class LlmToolFunction(TypedDict, total=False):
    description: Required[str]
    """A description of the model to use."""

    model: Required[str]
    """The model to use."""


class LlmTool(TypedDict, total=False):
    function: Required[LlmToolFunction]
    """A tool that uses another Writer model to generate a response."""

    type: Required[Literal["llm"]]
    """The type of tool."""


class TranslationToolFunction(TypedDict, total=False):
    formality: Required[bool]
    """Whether to use formal or informal language in the translation.

    See the
    [list of languages that support formality](https://dev.writer.com/api-guides/api-reference/translation-api/language-support#formality).
    If the language does not support formality, this parameter is ignored.
    """

    length_control: Required[bool]
    """Whether to control the length of the translated text.

    See the
    [list of languages that support length control](https://dev.writer.com/api-guides/api-reference/translation-api/language-support#length-control).
    If the language does not support length control, this parameter is ignored.
    """

    mask_profanity: Required[bool]
    """Whether to mask profane words in the translated text.

    See the
    [list of languages that do not support profanity masking](https://dev.writer.com/api-guides/api-reference/translation-api/language-support#profanity-masking).
    If the language does not support profanity masking, this parameter is ignored.
    """

    model: Required[Literal["palmyra-translate"]]
    """The model to use for translation."""

    source_language_code: str
    """Optional.

    The [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
    language code of the original text to translate. For example, `en` for English,
    `zh` for Chinese, `fr` for French, `es` for Spanish. If the language has a
    variant, the code appends the two-digit
    [ISO-3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
    If you do not provide a language code, the LLM detects the language of the text.
    """

    target_language_code: str
    """Optional.

    The [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
    language code of the target language for the translation. For example, `en` for
    English, `zh` for Chinese, `fr` for French, `es` for Spanish. If the language
    has a variant, the code appends the two-digit
    [ISO-3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
    If you do not provide a language code, the LLM uses the content of the chat
    message to determine the target language.
    """


class TranslationTool(TypedDict, total=False):
    function: Required[TranslationToolFunction]
    """A tool that uses Palmyra Translate to translate text."""

    type: Required[Literal["translation"]]
    """The type of tool."""


class VisionToolFunctionVariable(TypedDict, total=False):
    file_id: Required[str]
    """The File ID of the image to analyze.

    The file must be uploaded to the Writer platform before you use it with the
    Vision tool.
    """

    name: Required[str]
    """The name of the file variable.

    You must reference this name in the `message.content` field of the request to
    the chat completions endpoint. Use double curly braces (`{{}}`) to reference the
    file. For example,
    `Describe the difference between the image {{image_1}} and the image {{image_2}}`.
    """


class VisionToolFunction(TypedDict, total=False):
    model: Required[Literal["palmyra-vision"]]
    """The model to use for image analysis."""

    variables: Required[Iterable[VisionToolFunctionVariable]]


class VisionTool(TypedDict, total=False):
    function: Required[VisionToolFunction]
    """A tool that uses Palmyra Vision to analyze images."""

    type: Required[Literal["vision"]]
    """The type of tool."""


ToolParam: TypeAlias = Union[FunctionTool, GraphTool, LlmTool, TranslationTool, VisionTool]
