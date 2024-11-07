# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["ToolParsePdfResponse"]


class ToolParsePdfResponse(BaseModel):
    content: str
    """The extracted content from the PDF file, converted to the specified format."""
