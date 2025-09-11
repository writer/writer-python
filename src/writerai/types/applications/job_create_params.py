# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["JobCreateParams", "Input"]


class JobCreateParams(TypedDict, total=False):
    inputs: Required[Iterable[Input]]
    """A list of input objects to generate content for."""


class Input(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the input field from the application.

    All input types from the No-code application are supported (i.e. Text input,
    Dropdown, File upload, Image input). The identifier should be the name of the
    input type.
    """

    value: Required[SequenceNotStr[str]]
    """The value for the input field.

    If the input type is "File upload", you must pass the `file_id` of an uploaded
    file. You cannot pass a file object directly. See the
    [file upload endpoint](https://dev.writer.com/api-reference/file-api/upload-files)
    for instructions on uploading files or the
    [list files endpoint](https://dev.writer.com/api-reference/file-api/get-all-files)
    for how to see a list of uploaded files and their IDs.
    """
