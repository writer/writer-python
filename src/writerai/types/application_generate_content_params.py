# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "ApplicationGenerateContentParamsBase",
    "Input",
    "ApplicationGenerateContentParamsNonStreaming",
    "ApplicationGenerateContentParamsStreaming",
]


class ApplicationGenerateContentParamsBase(TypedDict, total=False):
    inputs: Required[Iterable[Input]]


class Input(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the input field from the application.

    All input types from the No-code application are supported (i.e. Text input,
    Dropdown, File upload, Image input). The identifier should be the name of the
    input type.
    """

    value: Required[List[str]]
    """The value for the input field.

    If file is required you will need to pass a `file_id`. See
    [here](https://dev.writer.com/api-guides/api-reference/file-api/upload-files)
    for the Files API.
    """


class ApplicationGenerateContentParamsNonStreaming(ApplicationGenerateContentParamsBase, total=False):
    stream: Literal[False]
    """Indicates whether the response should be streamed.

    Currently only supported for research assistant applications.
    """


class ApplicationGenerateContentParamsStreaming(ApplicationGenerateContentParamsBase):
    stream: Required[Literal[True]]
    """Indicates whether the response should be streamed.

    Currently only supported for research assistant applications.
    """


ApplicationGenerateContentParams = Union[
    ApplicationGenerateContentParamsNonStreaming, ApplicationGenerateContentParamsStreaming
]
