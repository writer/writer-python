# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ApplicationGenerateContentChunk", "Delta", "DeltaStage"]


class DeltaStage(BaseModel):
    id: str
    """The unique identifier for the stage."""

    content: str
    """The text content of the stage."""

    sources: Optional[List[str]] = None
    """A list of sources (URLs) that that stage used to process that particular step."""


class Delta(BaseModel):
    content: Optional[str] = None
    """The main text output."""

    stages: Optional[List[DeltaStage]] = None
    """A list of stages that show the 'thinking process'."""

    title: Optional[str] = None
    """The name of the output."""


class ApplicationGenerateContentChunk(BaseModel):
    delta: Delta
