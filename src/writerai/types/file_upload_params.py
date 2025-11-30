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

    graph_id: Annotated[str, PropertyInfo(alias="graphId")]
    """
    The unique identifier of the Knowledge Graph to associate the uploaded file
    with.

    Note: The response from the upload endpoint does not include the `graphId`
    field, but the association will be visible when you retrieve the file using the
    file retrieval endpoint.
    """
