# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["FileUploadParams"]


class FileUploadParams(TypedDict, total=False):
    content: Required[FileTypes]

    content_disposition: Required[Annotated[str, PropertyInfo(alias="Content-Disposition")]]

    content_type: Required[Annotated[str, PropertyInfo(alias="Content-Type")]]
