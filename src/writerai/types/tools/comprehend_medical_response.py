# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "ComprehendMedicalResponse",
    "Entity",
    "EntityAttribute",
    "EntityAttributeConcept",
    "EntityAttributeTrait",
    "EntityConcept",
    "EntityTrait",
]


class EntityAttributeConcept(BaseModel):
    code: str

    description: str

    score: float


class EntityAttributeTrait(BaseModel):
    name: str

    score: float


class EntityAttribute(BaseModel):
    begin_offset: int

    concepts: List[EntityAttributeConcept]

    end_offset: int

    relationship_score: float

    score: float

    text: str

    traits: List[EntityAttributeTrait]

    type: str

    category: Optional[str] = None

    relationship_type: Optional[str] = None


class EntityConcept(BaseModel):
    code: str

    description: str

    score: float


class EntityTrait(BaseModel):
    name: str

    score: float


class Entity(BaseModel):
    attributes: List[EntityAttribute]

    begin_offset: int

    category: str

    concepts: List[EntityConcept]

    end_offset: int

    score: float

    text: str

    traits: List[EntityTrait]

    type: str


class ComprehendMedicalResponse(BaseModel):
    entities: List[Entity]
    """An array of medical entities extracted from the input text."""
