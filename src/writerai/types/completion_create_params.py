# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CompletionCreateParamsBase", "CompletionCreateParamsNonStreaming", "CompletionCreateParamsStreaming"]


class CompletionCreateParamsBase(TypedDict, total=False):
    model: Required[str]
    """The identifier of the model to be used for processing the request."""

    prompt: Required[str]
    """The input text that the model will process to generate a response."""

    best_of: int
    """Specifies the number of completions to generate and return the best one.

    Useful for generating multiple outputs and choosing the best based on some
    criteria.
    """

    max_tokens: int
    """The maximum number of tokens that the model can generate in the response."""

    random_seed: int
    """
    A seed used to initialize the random number generator for the model, ensuring
    reproducibility of the output when the same inputs are provided.
    """

    stop: Union[List[str], str]
    """Specifies stopping conditions for the model's output generation.

    This can be an array of strings or a single string that the model will look for
    as a signal to stop generating further tokens.
    """

    temperature: float
    """Controls the randomness of the model's outputs.

    Higher values lead to more random outputs, while lower values make the model
    more deterministic.
    """

    top_p: float
    """
    Used to control the nucleus sampling, where only the most probable tokens with a
    cumulative probability of top_p are considered for sampling, providing a way to
    fine-tune the randomness of predictions.
    """


class CompletionCreateParamsNonStreaming(CompletionCreateParamsBase, total=False):
    stream: Literal[False]
    """Determines whether the model's output should be streamed.

    If true, the output is generated and sent incrementally, which can be useful for
    real-time applications.
    """


class CompletionCreateParamsStreaming(CompletionCreateParamsBase):
    stream: Required[Literal[True]]
    """Determines whether the model's output should be streamed.

    If true, the output is generated and sent incrementally, which can be useful for
    real-time applications.
    """


CompletionCreateParams = Union[CompletionCreateParamsNonStreaming, CompletionCreateParamsStreaming]
