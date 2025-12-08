# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VisionAnalyzeParams", "Variable"]


class VisionAnalyzeParams(TypedDict, total=False):
    model: Required[Literal["palmyra-vision"]]
    """The model to use for image analysis."""

    prompt: Required[str]
    """The prompt to use for the image analysis.

    The prompt must include the name of each image variable, surrounded by double
    curly braces (`{{}}`). For example,
    `Describe the difference between the image {{image_1}} and the image {{image_2}}`.
    """

    variables: Required[Iterable[Variable]]


class Variable(TypedDict, total=False):
    """An array of file variables required for the analysis.

    The files must be uploaded to the Writer platform before they can be used in a vision request. Learn how to upload files using the [Files API](https://dev.writer.com/api-reference/file-api/upload-files).

    Supported file types: JPG, PNG, PDF, TXT. The maximum allowed file size for each file is 7MB.
    """

    file_id: Required[str]
    """The File ID of the file to analyze.

    The file must be uploaded to the Writer platform before it can be used in a
    vision request. Supported file types: JPG, PNG, PDF, TXT (max 7MB each).
    """

    name: Required[str]
    """The name of the file variable.

    You must reference this name in the prompt with double curly braces (`{{}}`).
    For example,
    `Describe the difference between the image {{image_1}} and the image {{image_2}}`.
    """
