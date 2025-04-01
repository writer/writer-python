# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["VisionAnalyzeParams", "Variable"]


class VisionAnalyzeParams(TypedDict, total=False):
    model: Required[str]
    """The model to be used for image analysis.

    Currently only supports `palmyra-vision`.
    """

    prompt: Required[str]
    """The prompt to use for the image analysis.

    The prompt must include the name of each image variable, surrounded by double
    curly braces (`{{}}`). For example,
    `Describe the difference between the image {{image_1}} and the image {{image_2}}`.
    """

    variables: Required[Iterable[Variable]]


class Variable(TypedDict, total=False):
    file_id: Required[str]
    """The File ID of the image to be analyzed.

    The file must be uploaded to the Writer platform before it can be used in a
    vision request.
    """

    name: Required[str]
    """The name of the file variable.

    You must reference this name in the prompt with double curly braces (`{{}}`).
    For example,
    `Describe the difference between the image {{image_1}} and the image {{image_2}}`.
    """
