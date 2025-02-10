# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ApplicationListResponse",
    "Input",
    "InputOptions",
    "InputOptionsApplicationInputDropdownOptions",
    "InputOptionsApplicationInputFileOptions",
    "InputOptionsApplicationInputMediaOptions",
    "InputOptionsApplicationInputTextOptions",
]


class InputOptionsApplicationInputDropdownOptions(BaseModel):
    list: List[str]
    """List of available options in the dropdown menu."""


class InputOptionsApplicationInputFileOptions(BaseModel):
    file_types: List[str]
    """List of allowed file extensions."""

    max_file_size_mb: int
    """Maximum file size allowed in megabytes."""

    max_files: int
    """Maximum number of files that can be uploaded."""

    max_word_count: int
    """Maximum number of words allowed in text files."""


class InputOptionsApplicationInputMediaOptions(BaseModel):
    file_types: List[str]
    """List of allowed media file types."""

    max_image_size_mb: int
    """Maximum media file size allowed in megabytes."""


class InputOptionsApplicationInputTextOptions(BaseModel):
    max_fields: int
    """Maximum number of text fields allowed."""

    min_fields: int
    """Minimum number of text fields required."""


InputOptions: TypeAlias = Union[
    InputOptionsApplicationInputDropdownOptions,
    InputOptionsApplicationInputFileOptions,
    InputOptionsApplicationInputMediaOptions,
    InputOptionsApplicationInputTextOptions,
]


class Input(BaseModel):
    input_type: Literal["text", "dropdown", "file", "media"]
    """Type of input field determining its behavior and validation rules."""

    name: str
    """Identifier for the input field."""

    required: bool
    """Indicates if this input field is mandatory."""

    description: Optional[str] = None
    """Human-readable description of the input field's purpose."""

    options: Optional[InputOptions] = None
    """Type-specific configuration options for input fields."""


class ApplicationListResponse(BaseModel):
    id: str
    """Unique identifier for the application."""

    created_at: datetime
    """Timestamp when the application was created."""

    inputs: List[Input]
    """List of input configurations for the application."""

    name: str
    """Display name of the application."""

    status: Literal["deployed", "draft"]
    """Current deployment status of the application.

    Note: currently only `deployed` applications are returned.
    """

    type: Literal["generation"]
    """The type of no-code application."""

    updated_at: datetime
    """Timestamp when the application was last updated."""

    last_deployed_at: Optional[datetime] = None
    """Timestamp when the application was last deployed."""
