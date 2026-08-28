# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["GraphCreateParams"]


class GraphCreateParams(TypedDict, total=False):
    description: str
    """A description of the Knowledge Graph (max 255 characters).

    Omitting this field leaves the description unchanged.
    """

    name: str
    """The name of the Knowledge Graph (max 255 characters).

    Omitting this field leaves the name unchanged.
    """

    team_ids: Iterable[int]
    """Optional list of team IDs to deploy the Knowledge Graph to.

    Omit the field or pass an empty array to create an org-wide Knowledge Graph
    (accessible to every team in the organization), which is the default. Provide
    one or more team IDs to scope the Knowledge Graph to those teams. Only applies
    when using an org-scoped API key; requests made with a team-scoped API key
    ignore this field and always assign the graph to that key's team.
    """
