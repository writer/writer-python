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

    If the input type is "File upload", you must pass the `file_id` of an uploaded
    file. You cannot pass a file object directly. See the
    [file upload endpoint](/api-guides/api-reference/file-api/upload-files) for
    instructions on uploading files or the
    [list files endpoint](/api-guides/api-reference/file-api/get-all-files) for how
    to see a list of uploaded files and their IDs.
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
