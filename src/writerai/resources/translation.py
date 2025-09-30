# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing_extensions import Literal

import httpx

from ..types import translation_translate_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.translation_response import TranslationResponse

__all__ = ["TranslationResource", "AsyncTranslationResource"]


class TranslationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TranslationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return TranslationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranslationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return TranslationResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "Will be removed in a future release. Migrate to `chat.chat` with the translate tool for translation capabilities. See documentation at dev.writer.com for more information."
    )
    def translate(
        self,
        *,
        formality: bool,
        length_control: bool,
        mask_profanity: bool,
        model: Literal["palmyra-translate"],
        source_language_code: str,
        target_language_code: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranslationResponse:
        """
        Translate text from one language to another.

        Args:
          formality: Whether to use formal or informal language in the translation. See the
              [list of languages that support formality](https://dev.writer.com/api-reference/translation-api/language-support#formality).
              If the language does not support formality, this parameter is ignored.

          length_control: Whether to control the length of the translated text. See the
              [list of languages that support length control](https://dev.writer.com/api-reference/translation-api/language-support#length-control).
              If the language does not support length control, this parameter is ignored.

          mask_profanity: Whether to mask profane words in the translated text. See the
              [list of languages that do not support profanity masking](https://dev.writer.com/api-reference/translation-api/language-support#profanity-masking).
              If the language does not support profanity masking, this parameter is ignored.

          model: The model to use for translation.

          source_language_code: The [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
              language code of the original text to translate. For example, `en` for English,
              `zh` for Chinese, `fr` for French, `es` for Spanish. If the language has a
              variant, the code appends the two-digit
              [ISO-3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
              For example, Mexican Spanish is `es-MX`. See the
              [list of supported languages and language codes](https://dev.writer.com/api-reference/translation-api/language-support).

          target_language_code: The [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
              language code of the target language for the translation. For example, `en` for
              English, `zh` for Chinese, `fr` for French, `es` for Spanish. If the language
              has a variant, the code appends the two-digit
              [ISO-3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
              For example, Mexican Spanish is `es-MX`. See the
              [list of supported languages and language codes](https://dev.writer.com/api-reference/translation-api/language-support).

          text: The text to translate. Maximum of 100,000 words.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/translation",
            body=maybe_transform(
                {
                    "formality": formality,
                    "length_control": length_control,
                    "mask_profanity": mask_profanity,
                    "model": model,
                    "source_language_code": source_language_code,
                    "target_language_code": target_language_code,
                    "text": text,
                },
                translation_translate_params.TranslationTranslateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TranslationResponse,
        )


class AsyncTranslationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTranslationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTranslationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranslationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return AsyncTranslationResourceWithStreamingResponse(self)

    @typing_extensions.deprecated(
        "Will be removed in a future release. Migrate to `chat.chat` with the translate tool for translation capabilities. See documentation at dev.writer.com for more information."
    )
    async def translate(
        self,
        *,
        formality: bool,
        length_control: bool,
        mask_profanity: bool,
        model: Literal["palmyra-translate"],
        source_language_code: str,
        target_language_code: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TranslationResponse:
        """
        Translate text from one language to another.

        Args:
          formality: Whether to use formal or informal language in the translation. See the
              [list of languages that support formality](https://dev.writer.com/api-reference/translation-api/language-support#formality).
              If the language does not support formality, this parameter is ignored.

          length_control: Whether to control the length of the translated text. See the
              [list of languages that support length control](https://dev.writer.com/api-reference/translation-api/language-support#length-control).
              If the language does not support length control, this parameter is ignored.

          mask_profanity: Whether to mask profane words in the translated text. See the
              [list of languages that do not support profanity masking](https://dev.writer.com/api-reference/translation-api/language-support#profanity-masking).
              If the language does not support profanity masking, this parameter is ignored.

          model: The model to use for translation.

          source_language_code: The [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
              language code of the original text to translate. For example, `en` for English,
              `zh` for Chinese, `fr` for French, `es` for Spanish. If the language has a
              variant, the code appends the two-digit
              [ISO-3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
              For example, Mexican Spanish is `es-MX`. See the
              [list of supported languages and language codes](https://dev.writer.com/api-reference/translation-api/language-support).

          target_language_code: The [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
              language code of the target language for the translation. For example, `en` for
              English, `zh` for Chinese, `fr` for French, `es` for Spanish. If the language
              has a variant, the code appends the two-digit
              [ISO-3166 country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).
              For example, Mexican Spanish is `es-MX`. See the
              [list of supported languages and language codes](https://dev.writer.com/api-reference/translation-api/language-support).

          text: The text to translate. Maximum of 100,000 words.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/translation",
            body=await async_maybe_transform(
                {
                    "formality": formality,
                    "length_control": length_control,
                    "mask_profanity": mask_profanity,
                    "model": model,
                    "source_language_code": source_language_code,
                    "target_language_code": target_language_code,
                    "text": text,
                },
                translation_translate_params.TranslationTranslateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TranslationResponse,
        )


class TranslationResourceWithRawResponse:
    def __init__(self, translation: TranslationResource) -> None:
        self._translation = translation

        self.translate = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                translation.translate,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncTranslationResourceWithRawResponse:
    def __init__(self, translation: AsyncTranslationResource) -> None:
        self._translation = translation

        self.translate = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                translation.translate,  # pyright: ignore[reportDeprecated],
            )
        )


class TranslationResourceWithStreamingResponse:
    def __init__(self, translation: TranslationResource) -> None:
        self._translation = translation

        self.translate = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                translation.translate,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncTranslationResourceWithStreamingResponse:
    def __init__(self, translation: AsyncTranslationResource) -> None:
        self._translation = translation

        self.translate = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                translation.translate,  # pyright: ignore[reportDeprecated],
            )
        )
