from typing import Union
from typing_extensions import TypeAlias

from .response_format_text import ResponseFormatText
from .response_format_json_object import ResponseFormatJSONObject
from .response_format_json_schema import ResponseFormatJSONSchema

__all__ = ["ResponseFormat"]

ResponseFormat: TypeAlias = Union[ResponseFormatText, ResponseFormatJSONObject, ResponseFormatJSONSchema]
