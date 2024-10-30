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
from ...types.tools import medical_create_params
from ..._base_client import make_request_options
from ...types.tools.medical_create_response import MedicalCreateResponse

__all__ = ["MedicalResource", "AsyncMedicalResource"]


class MedicalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MedicalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return MedicalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MedicalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return MedicalResourceWithStreamingResponse(self)

    def create(
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
    ) -> MedicalCreateResponse:
        """
        Create a completion using Palmyra medical model.

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
                medical_create_params.MedicalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MedicalCreateResponse,
        )


class AsyncMedicalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMedicalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMedicalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMedicalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return AsyncMedicalResourceWithStreamingResponse(self)

    async def create(
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
    ) -> MedicalCreateResponse:
        """
        Create a completion using Palmyra medical model.

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
                medical_create_params.MedicalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MedicalCreateResponse,
        )


class MedicalResourceWithRawResponse:
    def __init__(self, medical: MedicalResource) -> None:
        self._medical = medical

        self.create = to_raw_response_wrapper(
            medical.create,
        )


class AsyncMedicalResourceWithRawResponse:
    def __init__(self, medical: AsyncMedicalResource) -> None:
        self._medical = medical

        self.create = async_to_raw_response_wrapper(
            medical.create,
        )


class MedicalResourceWithStreamingResponse:
    def __init__(self, medical: MedicalResource) -> None:
        self._medical = medical

        self.create = to_streamed_response_wrapper(
            medical.create,
        )


class AsyncMedicalResourceWithStreamingResponse:
    def __init__(self, medical: AsyncMedicalResource) -> None:
        self._medical = medical

        self.create = async_to_streamed_response_wrapper(
            medical.create,
        )
