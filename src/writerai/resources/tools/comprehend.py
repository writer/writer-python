# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.tools import comprehend_medical_params
from ..._base_client import make_request_options
from ...types.tools.comprehend_medical_response import ComprehendMedicalResponse

__all__ = ["ComprehendResource", "AsyncComprehendResource"]


class ComprehendResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ComprehendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return ComprehendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComprehendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return ComprehendResourceWithStreamingResponse(self)

    def medical(
        self,
        *,
        content: str,
        response_type: Literal["Entities", "RxNorm", "ICD-10-CM", "SNOMED CT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ComprehendMedicalResponse:
        """
        Analyze unstructured medical text to extract entities labeled with standardized
        medical codes and confidence scores.

        Args:
          content: The text to be analyzed.

          response_type: The structure of the response to be returned. `Entities` returns medical
              entities, `RxNorm` returns medication information, `ICD-10-CM` returns diagnosis
              codes, and `SNOMED CT` returns medical concepts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools/comprehend/medical",
            body=maybe_transform(
                {
                    "content": content,
                    "response_type": response_type,
                },
                comprehend_medical_params.ComprehendMedicalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComprehendMedicalResponse,
        )


class AsyncComprehendResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncComprehendResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncComprehendResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComprehendResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return AsyncComprehendResourceWithStreamingResponse(self)

    async def medical(
        self,
        *,
        content: str,
        response_type: Literal["Entities", "RxNorm", "ICD-10-CM", "SNOMED CT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ComprehendMedicalResponse:
        """
        Analyze unstructured medical text to extract entities labeled with standardized
        medical codes and confidence scores.

        Args:
          content: The text to be analyzed.

          response_type: The structure of the response to be returned. `Entities` returns medical
              entities, `RxNorm` returns medication information, `ICD-10-CM` returns diagnosis
              codes, and `SNOMED CT` returns medical concepts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools/comprehend/medical",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "response_type": response_type,
                },
                comprehend_medical_params.ComprehendMedicalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ComprehendMedicalResponse,
        )


class ComprehendResourceWithRawResponse:
    def __init__(self, comprehend: ComprehendResource) -> None:
        self._comprehend = comprehend

        self.medical = to_raw_response_wrapper(
            comprehend.medical,
        )


class AsyncComprehendResourceWithRawResponse:
    def __init__(self, comprehend: AsyncComprehendResource) -> None:
        self._comprehend = comprehend

        self.medical = async_to_raw_response_wrapper(
            comprehend.medical,
        )


class ComprehendResourceWithStreamingResponse:
    def __init__(self, comprehend: ComprehendResource) -> None:
        self._comprehend = comprehend

        self.medical = to_streamed_response_wrapper(
            comprehend.medical,
        )


class AsyncComprehendResourceWithStreamingResponse:
    def __init__(self, comprehend: AsyncComprehendResource) -> None:
        self._comprehend = comprehend

        self.medical = async_to_streamed_response_wrapper(
            comprehend.medical,
        )
