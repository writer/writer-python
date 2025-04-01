# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import vision_analyze_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.vision_response import VisionResponse

__all__ = ["VisionResource", "AsyncVisionResource"]


class VisionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VisionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return VisionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VisionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return VisionResourceWithStreamingResponse(self)

    def analyze(
        self,
        *,
        model: str,
        prompt: str,
        variables: Iterable[vision_analyze_params.Variable],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VisionResponse:
        """
        Submit images and a prompt to generate an analysis of the images.

        Args:
          model: The model to be used for image analysis. Currently only supports
              `palmyra-vision`.

          prompt: The prompt to use for the image analysis. The prompt must include the name of
              each image variable, surrounded by double curly braces (`{{}}`). For example,
              `Describe the difference between the image {{image_1}} and the image {{image_2}}`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/vision",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "variables": variables,
                },
                vision_analyze_params.VisionAnalyzeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VisionResponse,
        )


class AsyncVisionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVisionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/writer/writer-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVisionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVisionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/writer/writer-python#with_streaming_response
        """
        return AsyncVisionResourceWithStreamingResponse(self)

    async def analyze(
        self,
        *,
        model: str,
        prompt: str,
        variables: Iterable[vision_analyze_params.Variable],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VisionResponse:
        """
        Submit images and a prompt to generate an analysis of the images.

        Args:
          model: The model to be used for image analysis. Currently only supports
              `palmyra-vision`.

          prompt: The prompt to use for the image analysis. The prompt must include the name of
              each image variable, surrounded by double curly braces (`{{}}`). For example,
              `Describe the difference between the image {{image_1}} and the image {{image_2}}`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/vision",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "variables": variables,
                },
                vision_analyze_params.VisionAnalyzeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VisionResponse,
        )


class VisionResourceWithRawResponse:
    def __init__(self, vision: VisionResource) -> None:
        self._vision = vision

        self.analyze = to_raw_response_wrapper(
            vision.analyze,
        )


class AsyncVisionResourceWithRawResponse:
    def __init__(self, vision: AsyncVisionResource) -> None:
        self._vision = vision

        self.analyze = async_to_raw_response_wrapper(
            vision.analyze,
        )


class VisionResourceWithStreamingResponse:
    def __init__(self, vision: VisionResource) -> None:
        self._vision = vision

        self.analyze = to_streamed_response_wrapper(
            vision.analyze,
        )


class AsyncVisionResourceWithStreamingResponse:
    def __init__(self, vision: AsyncVisionResource) -> None:
        self._vision = vision

        self.analyze = async_to_streamed_response_wrapper(
            vision.analyze,
        )
