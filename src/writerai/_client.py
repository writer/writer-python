# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from writerai import _exceptions

from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import chat, files, graphs, models, vision, completions
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import WriterError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.tools import tools
from .resources.applications import applications

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Writer", "AsyncWriter", "Client", "AsyncClient"]


class Writer(SyncAPIClient):
    applications: applications.ApplicationsResource
    chat: chat.ChatResource
    completions: completions.CompletionsResource
    models: models.ModelsResource
    graphs: graphs.GraphsResource
    files: files.FilesResource
    tools: tools.ToolsResource
    vision: vision.VisionResource
    with_raw_response: WriterWithRawResponse
    with_streaming_response: WriterWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Writer client instance.

        This automatically infers the `api_key` argument from the `WRITER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("WRITER_API_KEY")
        if api_key is None:
            raise WriterError(
                "The api_key client option must be set either by passing api_key to the client or by setting the WRITER_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("WRITER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.writer.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = Stream

        self.applications = applications.ApplicationsResource(self)
        self.chat = chat.ChatResource(self)
        self.completions = completions.CompletionsResource(self)
        self.models = models.ModelsResource(self)
        self.graphs = graphs.GraphsResource(self)
        self.files = files.FilesResource(self)
        self.tools = tools.ToolsResource(self)
        self.vision = vision.VisionResource(self)
        self.with_raw_response = WriterWithRawResponse(self)
        self.with_streaming_response = WriterWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncWriter(AsyncAPIClient):
    applications: applications.AsyncApplicationsResource
    chat: chat.AsyncChatResource
    completions: completions.AsyncCompletionsResource
    models: models.AsyncModelsResource
    graphs: graphs.AsyncGraphsResource
    files: files.AsyncFilesResource
    tools: tools.AsyncToolsResource
    vision: vision.AsyncVisionResource
    with_raw_response: AsyncWriterWithRawResponse
    with_streaming_response: AsyncWriterWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncWriter client instance.

        This automatically infers the `api_key` argument from the `WRITER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("WRITER_API_KEY")
        if api_key is None:
            raise WriterError(
                "The api_key client option must be set either by passing api_key to the client or by setting the WRITER_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("WRITER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.writer.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = AsyncStream

        self.applications = applications.AsyncApplicationsResource(self)
        self.chat = chat.AsyncChatResource(self)
        self.completions = completions.AsyncCompletionsResource(self)
        self.models = models.AsyncModelsResource(self)
        self.graphs = graphs.AsyncGraphsResource(self)
        self.files = files.AsyncFilesResource(self)
        self.tools = tools.AsyncToolsResource(self)
        self.vision = vision.AsyncVisionResource(self)
        self.with_raw_response = AsyncWriterWithRawResponse(self)
        self.with_streaming_response = AsyncWriterWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class WriterWithRawResponse:
    def __init__(self, client: Writer) -> None:
        self.applications = applications.ApplicationsResourceWithRawResponse(client.applications)
        self.chat = chat.ChatResourceWithRawResponse(client.chat)
        self.completions = completions.CompletionsResourceWithRawResponse(client.completions)
        self.models = models.ModelsResourceWithRawResponse(client.models)
        self.graphs = graphs.GraphsResourceWithRawResponse(client.graphs)
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.tools = tools.ToolsResourceWithRawResponse(client.tools)
        self.vision = vision.VisionResourceWithRawResponse(client.vision)


class AsyncWriterWithRawResponse:
    def __init__(self, client: AsyncWriter) -> None:
        self.applications = applications.AsyncApplicationsResourceWithRawResponse(client.applications)
        self.chat = chat.AsyncChatResourceWithRawResponse(client.chat)
        self.completions = completions.AsyncCompletionsResourceWithRawResponse(client.completions)
        self.models = models.AsyncModelsResourceWithRawResponse(client.models)
        self.graphs = graphs.AsyncGraphsResourceWithRawResponse(client.graphs)
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.tools = tools.AsyncToolsResourceWithRawResponse(client.tools)
        self.vision = vision.AsyncVisionResourceWithRawResponse(client.vision)


class WriterWithStreamedResponse:
    def __init__(self, client: Writer) -> None:
        self.applications = applications.ApplicationsResourceWithStreamingResponse(client.applications)
        self.chat = chat.ChatResourceWithStreamingResponse(client.chat)
        self.completions = completions.CompletionsResourceWithStreamingResponse(client.completions)
        self.models = models.ModelsResourceWithStreamingResponse(client.models)
        self.graphs = graphs.GraphsResourceWithStreamingResponse(client.graphs)
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.tools = tools.ToolsResourceWithStreamingResponse(client.tools)
        self.vision = vision.VisionResourceWithStreamingResponse(client.vision)


class AsyncWriterWithStreamedResponse:
    def __init__(self, client: AsyncWriter) -> None:
        self.applications = applications.AsyncApplicationsResourceWithStreamingResponse(client.applications)
        self.chat = chat.AsyncChatResourceWithStreamingResponse(client.chat)
        self.completions = completions.AsyncCompletionsResourceWithStreamingResponse(client.completions)
        self.models = models.AsyncModelsResourceWithStreamingResponse(client.models)
        self.graphs = graphs.AsyncGraphsResourceWithStreamingResponse(client.graphs)
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.tools = tools.AsyncToolsResourceWithStreamingResponse(client.tools)
        self.vision = vision.AsyncVisionResourceWithStreamingResponse(client.vision)


Client = Writer

AsyncClient = AsyncWriter
