# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ComprehendMedicalParams"]


class ComprehendMedicalParams(TypedDict, total=False):
    content: Required[str]
    """The text to be analyzed."""

    response_type: Required[Literal["Entities", "RxNorm", "ICD-10-CM", "SNOMED CT"]]
    """The structure of the response to be returned.

    `Entities` returns medical entities, `RxNorm` returns medication information,
    `ICD-10-CM` returns diagnosis codes, and `SNOMED CT` returns medical concepts.
    """
