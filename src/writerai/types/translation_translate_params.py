# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TranslationTranslateParams"]


class TranslationTranslateParams(TypedDict, total=False):
    formality: Required[bool]
    """Whether to use formal or informal language in the translation.

    See the
    [list of languages that support formality](https://dev.writer.com/api-reference/translation-api/language-support#formality).
    If the language does not support formality, this parameter is ignored.
    """

    length_control: Required[bool]
    """Whether to control the length of the translated text.

    See the
    [list of languages that support length control](https://dev.writer.com/api-reference/translation-api/language-support#length-control).
    If the language does not support length control, this parameter is ignored.
    """

    mask_profanity: Required[bool]
    """Whether to mask profane words in the translated text.

    See the
    [list of languages that do not support profanity masking](https://dev.writer.com/api-reference/translation-api/language-support#profanity-masking).
    If the language does not support profanity masking, this parameter is ignored.
    """

    model: Required[Literal["palmyra-translate"]]
    """The model to use for translation."""

    source_language_code: Required[str]
    """
    The [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
    language code of the original text to translate. For example, `en` for English,
    `zh` for Chinese, `fr` for French, `es` for Spanish. If the language has a
    variant, the code appends the two-digit
    [ISO-3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
    For example, Mexican Spanish is `es-MX`. See the
    [list of supported languages and language codes](https://dev.writer.com/api-reference/translation-api/language-support).
    """

    target_language_code: Required[str]
    """
    The [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
    language code of the target language for the translation. For example, `en` for
    English, `zh` for Chinese, `fr` for French, `es` for Spanish. If the language
    has a variant, the code appends the two-digit
    [ISO-3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
    For example, Mexican Spanish is `es-MX`. See the
    [list of supported languages and language codes](https://dev.writer.com/api-reference/translation-api/language-support).
    """

    text: Required[str]
    """The text to translate. Maximum of 100,000 words."""
