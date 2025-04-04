from __future__ import annotations

import os
from typing import Any, Generic, Callable, Iterator, overload
from typing_extensions import Literal, TypeVar

# import rich
import httpx
import pytest
from respx import MockRouter
from pydantic import BaseModel
from inline_snapshot import external, snapshot, outsource

import writerai
from writerai import Writer, AsyncWriter
from writerai._utils import assert_signatures_in_sync

# from writerai._compat import model_copy
from writerai.lib.streaming.chat import (
    ContentDoneEvent,
    ChatCompletionStream,
    ChatCompletionStreamEvent,
    ChatCompletionStreamManager,
    # ParsedChatCompletionSnapshot,
)
from writerai.lib._parsing._completions import ResponseFormatT

from ._utils import print_obj
from ...conftest import base_url

_T = TypeVar("_T")

# all the snapshots in this file are auto-generated from the live API
#
# you can update them with
#
# `WRITER_LIVE=1 pytest --inline-snapshot=fix`


@pytest.mark.respx(base_url=base_url)
def test_parse_nothing(client: Writer, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
    listener = _make_stream_snapshot_request(
        lambda c: c.chat.stream(
            model="palmyra-x-003-instruct",
            messages=[
                {
                    "role": "user",
                    "content": "What's the weather like in SF?",
                },
            ],
        ),
        content_snapshot=snapshot(external("e2aad469b71d*.writer")),
        openai_content_snapshot=snapshot(external("e2aad469b71d*.openai")),
        mock_client=client,
        respx_mock=respx_mock,
    )

    assert print_obj(listener.stream.get_final_completion().choices, monkeypatch) == snapshot(
        """\
[
    ParsedChatCompletionChoice[NoneType](
        finish_reason='stop',
        index=0,
        logprobs=None,
        message=ParsedChatCompletionMessage[NoneType](
            content="I'm unable to provide real-time weather updates. To get the current weather in San Francisco, I 
recommend checking a reliable weather website or a weather app.",
            graph_data=None,
            llm_data=None,
            parsed=None,
            refusal=None,
            role='assistant',
            tool_calls=[]
        )
    )
]
"""
    )
    assert print_obj(listener.get_event_by_type("content.done"), monkeypatch) == snapshot(
        """\
ContentDoneEvent[NoneType](
    content="I'm unable to provide real-time weather updates. To get the current weather in San Francisco, I recommend 
checking a reliable weather website or a weather app.",
    parsed=None,
    type='content.done'
)
"""
    )


# @pytest.mark.respx(base_url=base_url)
# def test_parse_pydantic_model(client: Writer, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
#     class Location(BaseModel):
#         city: str
#         temperature: float
#         units: Literal["c", "f"]

#     done_snapshots: list[ParsedChatCompletionSnapshot] = []

#     def on_event(stream: ChatCompletionStream[Location], event: ChatCompletionStreamEvent[Location]) -> None:
#         if event.type == "content.done":
#             done_snapshots.append(model_copy(stream.current_completion_snapshot, deep=True))

#     listener = _make_stream_snapshot_request(
#         lambda c: c.chat.stream(
#             model="palmyra-x-003-instruct",
#             messages=[
#                 {
#                     "role": "user",
#                     "content": "What's the weather like in SF?",
#                 },
#             ],
#             # response_format=Location,
#         ),
#         content_snapshot=snapshot(external("7e5ea4d12e7c*_bin")),
#         mock_client=client,
#         respx_mock=respx_mock,
#         on_event=on_event,
#     )

#     assert len(done_snapshots) == 1
#     assert isinstance(done_snapshots[0].choices[0].message.parsed, Location)

#     for event in reversed(listener.events):
#         if event.type == "content.delta":
#             data = cast(Any, event.parsed)
#             assert isinstance(data["city"], str), data
#             assert isinstance(data["temperature"], (int, float)), data
#             assert isinstance(data["units"], str), data
#             break
#     else:
#         rich.print(listener.events)
#         raise AssertionError("Did not find a `content.delta` event")

#     assert print_obj(listener.stream.get_final_completion(), monkeypatch) == snapshot(
#         """\
# ParsedChatCompletion[Location](
#     choices=[
#         ParsedChatCompletionChoice[Location](
#             finish_reason='stop',
#             index=0,
#             logprobs=None,
#             message=ParsedChatCompletionMessage[Location](
#                 content='{"city":"San Francisco","temperature":61,"units":"f"}',
#                 graph_data=None,
#                 parsed=Location(city='San Francisco', temperature=61.0, units='f'),
#                 refusal=None,
#                 role='assistant',
#                 tool_calls=[]
#             )
#         )
#     ],
#     created=1727346169,
#     id='chatcmpl-ABfw1e5abtU8OwGr15vOreYVb2MiF',
#     model='palmyra-x-003-instruct',
#     object='chat.completion',
#     service_tier=None,
#     system_fingerprint='fp_5050236cbd',
#     usage=CompletionUsage(
#         completion_tokens=14,
#         completion_tokens_details=CompletionTokensDetails(reasoning_tokens=0),
#         prompt_tokens=79,
#         total_tokens=93
#     )
# )
# """
#     )
#     assert print_obj(listener.get_event_by_type("content.done"), monkeypatch) == snapshot(
#         """\
# ContentDoneEvent[Location](
#     content='{"city":"San Francisco","temperature":61,"units":"f"}',
#     parsed=Location(city='San Francisco', temperature=61.0, units='f'),
#     type='content.done'
# )
# """
#     )


# @pytest.mark.respx(base_url=base_url)
# def test_parse_pydantic_model_multiple_choices(
#     client: Writer, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch
# ) -> None:
#     class Location(BaseModel):
#         city: str
#         temperature: float
#         units: Literal["c", "f"]

#     listener = _make_stream_snapshot_request(
#         lambda c: c.chat.stream(
#             model="palmyra-x-003-instruct",
#             messages=[
#                 {
#                     "role": "user",
#                     "content": "What's the weather like in SF?",
#                 },
#             ],
#             n=3,
#             response_format=Location,
#         ),
#         content_snapshot=snapshot(external("a491adda08c3*_bin")),
#         mock_client=client,
#         respx_mock=respx_mock,
#     )

#     assert [e.type for e in listener.events] == snapshot(
#         [
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.delta",
#             "chunk",
#             "content.done",
#             "chunk",
#             "content.done",
#             "chunk",
#             "content.done",
#             "chunk",
#         ]
#     )
#     assert print_obj(listener.stream.get_final_completion().choices, monkeypatch) == snapshot(
#         """\
# [
#     ParsedChatCompletionChoice[Location](
#         finish_reason='stop',
#         index=0,
#         logprobs=None,
#         message=ParsedChatCompletionMessage[Location](
#             content='{"city":"San Francisco","temperature":65,"units":"f"}',
#             graph_data=None,
#             parsed=Location(city='San Francisco', temperature=65.0, units='f'),
#             refusal=None,
#             role='assistant',
#             tool_calls=[]
#         )
#     ),
#     ParsedChatCompletionChoice[Location](
#         finish_reason='stop',
#         index=1,
#         logprobs=None,
#         message=ParsedChatCompletionMessage[Location](
#             content='{"city":"San Francisco","temperature":61,"units":"f"}',
#             graph_data=None,
#             parsed=Location(city='San Francisco', temperature=61.0, units='f'),
#             refusal=None,
#             role='assistant',
#             tool_calls=[]
#         )
#     ),
#     ParsedChatCompletionChoice[Location](
#         finish_reason='stop',
#         index=2,
#         logprobs=None,
#         message=ParsedChatCompletionMessage[Location](
#             content='{"city":"San Francisco","temperature":59,"units":"f"}',
#             graph_data=None,
#             parsed=Location(city='San Francisco', temperature=59.0, units='f'),
#             refusal=None,
#             role='assistant',
#             tool_calls=[]
#         )
#     )
# ]
# """
#     )


# @pytest.mark.respx(base_url=base_url)
# def test_parse_max_tokens_reached(client: Writer, respx_mock: MockRouter) -> None:
#     class Location(BaseModel):
#         city: str
#         temperature: float
#         units: Literal["c", "f"]
#
#     with pytest.raises(writerai.LengthFinishReasonError):
#         _make_stream_snapshot_request(
#             lambda c: c.chat.stream(
#                 model="palmyra-x-003-instruct",
#                 messages=[
#                     {
#                         "role": "user",
#                         "content": "What's the weather like in SF?",
#                     },
#                 ],
#                 max_tokens=1,
#                 response_format=Location,
#             ),
#             content_snapshot=snapshot(external("4cc50a6135d2*_bin")),
#             mock_client=client,
#             respx_mock=respx_mock,
#         )


# @pytest.mark.respx(base_url=base_url)
# def test_parse_pydantic_model_refusal(client: Writer, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
#     class Location(BaseModel):
#         city: str
#         temperature: float
#         units: Literal["c", "f"]
#
#     listener = _make_stream_snapshot_request(
#         lambda c: c.chat.stream(
#             model="palmyra-x-003-instruct",
#             messages=[
#                 {
#                     "role": "user",
#                     "content": "How do I make anthrax?",
#                 },
#             ],
#             response_format=Location,
#         ),
#         content_snapshot=snapshot(external("173417d55340*_bin")),
#         mock_client=client,
#         respx_mock=respx_mock,
#     )
#
#     assert print_obj(listener.get_event_by_type("refusal.done"), monkeypatch) == snapshot("""\
# RefusalDoneEvent(refusal="I'm sorry, I can't assist with that request.", type='refusal.done')
# """)
#
#     assert print_obj(listener.stream.get_final_completion().choices, monkeypatch) == snapshot(
#         """\
# [
#     ParsedChatCompletionChoice[Location](
#         finish_reason='stop',
#         index=0,
#         logprobs=None,
#         message=ParsedChatCompletionMessage[Location](
#             content=None,
#             graph_data=None,
#             parsed=None,
#             refusal="I'm sorry, I can't assist with that request.",
#             role='assistant',
#             tool_calls=[]
#         )
#     )
# ]
# """
#     )


@pytest.mark.respx(base_url=base_url)
def test_content_logprobs_events(client: Writer, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
    listener = _make_stream_snapshot_request(
        lambda c: c.chat.stream(
            model="palmyra-x-003-instruct",
            messages=[
                {
                    "role": "user",
                    "content": "Say foo",
                },
            ],
            logprobs=True,
        ),
        content_snapshot=snapshot(external("83b060bae42e*.writer")),
        openai_content_snapshot=snapshot(external("83b060bae42e*.openai")),
        mock_client=client,
        respx_mock=respx_mock,
    )

    assert print_obj([e for e in listener.events if e.type.startswith("logprobs")], monkeypatch) == snapshot("""\
[
    LogprobsContentDeltaEvent(
        content=[LogprobsToken(bytes=[70, 111, 111], logprob=-0.0025094282, token='Foo', top_logprobs=[])],
        snapshot=[LogprobsToken(bytes=[70, 111, 111], logprob=-0.0025094282, token='Foo', top_logprobs=[])],
        type='logprobs.content.delta'
    ),
    LogprobsContentDeltaEvent(
        content=[LogprobsToken(bytes=[33], logprob=-0.26638845, token='!', top_logprobs=[])],
        snapshot=[
            LogprobsToken(bytes=[70, 111, 111], logprob=-0.0025094282, token='Foo', top_logprobs=[]),
            LogprobsToken(bytes=[33], logprob=-0.26638845, token='!', top_logprobs=[])
        ],
        type='logprobs.content.delta'
    ),
    LogprobsContentDoneEvent(
        content=[
            LogprobsToken(bytes=[70, 111, 111], logprob=-0.0025094282, token='Foo', top_logprobs=[]),
            LogprobsToken(bytes=[33], logprob=-0.26638845, token='!', top_logprobs=[])
        ],
        type='logprobs.content.done'
    )
]
""")

    assert print_obj(listener.stream.get_final_completion().choices, monkeypatch) == snapshot("""\
[
    ParsedChatCompletionChoice[NoneType](
        finish_reason='stop',
        index=0,
        logprobs=Logprobs(
            content=[
                LogprobsToken(bytes=[70, 111, 111], logprob=-0.0025094282, token='Foo', top_logprobs=[]),
                LogprobsToken(bytes=[33], logprob=-0.26638845, token='!', top_logprobs=[])
            ],
            refusal=None
        ),
        message=ParsedChatCompletionMessage[NoneType](
            content='Foo!',
            graph_data=None,
            llm_data=None,
            parsed=None,
            refusal=None,
            role='assistant',
            tool_calls=[]
        )
    )
]
""")


@pytest.mark.respx(base_url=base_url)
def test_refusal_logprobs_events(client: Writer, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
    #     class Location(BaseModel):
    #         city: str
    #         temperature: float
    #         units: Literal["c", "f"]

    listener = _make_stream_snapshot_request(
        lambda c: c.chat.stream(
            model="palmyra-x-003-instruct",
            messages=[
                {
                    "role": "user",
                    "content": "How do I make anthrax?",
                },
            ],
            logprobs=True,
            # response_format=Location,
        ),
        content_snapshot=snapshot(external("569c877e6942*.writer")),
        openai_content_snapshot=snapshot(external("569c877e6942*.openai")),
        mock_client=client,
        respx_mock=respx_mock,
    )

    assert print_obj([e.type for e in listener.events if e.type.startswith("logprobs")], monkeypatch) == snapshot("""\
[
    'logprobs.refusal.delta',
    'logprobs.refusal.delta',
    'logprobs.refusal.delta',
    'logprobs.refusal.delta',
    'logprobs.refusal.delta',
    'logprobs.refusal.delta',
    'logprobs.refusal.delta',
    'logprobs.refusal.delta',
    'logprobs.refusal.delta',
    'logprobs.refusal.delta',
    'logprobs.refusal.delta',
    'logprobs.refusal.done'
]
""")

    assert print_obj(listener.stream.get_final_completion().choices, monkeypatch) == snapshot("""\
[
    ParsedChatCompletionChoice[NoneType](
        finish_reason='stop',
        index=0,
        logprobs=Logprobs(
            content=None,
            refusal=[
                LogprobsToken(bytes=[73, 39, 109], logprob=-0.0012038043, token="I'm", top_logprobs=[]),
                LogprobsToken(bytes=[32, 118, 101, 114, 121], logprob=-0.8438816, token=' very', top_logprobs=[]),
                LogprobsToken(
                    bytes=[32, 115, 111, 114, 114, 121],
                    logprob=-3.4121115e-06,
                    token=' sorry',
                    top_logprobs=[]
                ),
                LogprobsToken(bytes=[44], logprob=-3.3809047e-05, token=',', top_logprobs=[]),
                LogprobsToken(bytes=[32, 98, 117, 116], logprob=-0.038048144, token=' but', top_logprobs=[]),
                LogprobsToken(bytes=[32, 73], logprob=-0.0016109125, token=' I', top_logprobs=[]),
                LogprobsToken(
                    bytes=[32, 99, 97, 110, 39, 116],
                    logprob=-0.0073532974,
                    token=" can't",
                    top_logprobs=[]
                ),
                LogprobsToken(
                    bytes=[32, 97, 115, 115, 105, 115, 116],
                    logprob=-0.0020837625,
                    token=' assist',
                    top_logprobs=[]
                ),
                LogprobsToken(bytes=[32, 119, 105, 116, 104], logprob=-0.00318354, token=' with', top_logprobs=[]),
                LogprobsToken(bytes=[32, 116, 104, 97, 116], logprob=-0.0017186158, token=' that', top_logprobs=[]),
                LogprobsToken(bytes=[46], logprob=-0.57687104, token='.', top_logprobs=[])
            ]
        ),
        message=ParsedChatCompletionMessage[NoneType](
            content=None,
            graph_data=None,
            llm_data=None,
            parsed=None,
            refusal="I'm very sorry, but I can't assist with that.",
            role='assistant',
            tool_calls=[]
        )
    )
]
""")


@pytest.mark.respx(base_url=base_url)
def test_parse_pydantic_tool(client: Writer, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
    class GetWeatherArgs(BaseModel):
        city: str
        country: str
        units: Literal["c", "f"] = "c"

    listener = _make_stream_snapshot_request(
        lambda c: c.chat.stream(
            model="palmyra-x-003-instruct",
            messages=[
                {
                    "role": "user",
                    "content": "What's the weather like in Edinburgh?",
                },
            ],
            tools=[
                writerai.pydantic_function_tool(GetWeatherArgs),
            ],
        ),
        content_snapshot=snapshot(external("c6aa7e397b71*.writer")),
        openai_content_snapshot=snapshot(external("c6aa7e397b71*.openai")),
        mock_client=client,
        respx_mock=respx_mock,
    )

    assert print_obj(listener.stream.current_completion_snapshot.choices, monkeypatch) == snapshot(
        """\
[
    ParsedChatCompletionChoice[object](
        finish_reason='tool_calls',
        index=0,
        logprobs=None,
        message=ParsedChatCompletionMessage[object](
            content=None,
            graph_data=None,
            llm_data=None,
            parsed=None,
            refusal=None,
            role='assistant',
            tool_calls=[
                ParsedFunctionToolCall(
                    function=ParsedFunction(
                        arguments='{"city":"Edinburgh","country":"UK","units":"c"}',
                        name='GetWeatherArgs',
                        parsed_arguments=GetWeatherArgs(city='Edinburgh', country='UK', units='c')
                    ),
                    id='call_c91SqDXlYFuETYv8mUHzz6pp',
                    index=0,
                    type='function'
                )
            ]
        )
    )
]
"""
    )

    assert print_obj(listener.stream.get_final_completion().choices, monkeypatch) == snapshot(
        """\
[
    ParsedChatCompletionChoice[NoneType](
        finish_reason='tool_calls',
        index=0,
        logprobs=None,
        message=ParsedChatCompletionMessage[NoneType](
            content=None,
            graph_data=None,
            llm_data=None,
            parsed=None,
            refusal=None,
            role='assistant',
            tool_calls=[
                ParsedFunctionToolCall(
                    function=ParsedFunction(
                        arguments='{"city":"Edinburgh","country":"UK","units":"c"}',
                        name='GetWeatherArgs',
                        parsed_arguments=GetWeatherArgs(city='Edinburgh', country='UK', units='c')
                    ),
                    id='call_c91SqDXlYFuETYv8mUHzz6pp',
                    index=0,
                    type='function'
                )
            ]
        )
    )
]
"""
    )


@pytest.mark.respx(base_url=base_url)
def test_parse_multiple_pydantic_tools(client: Writer, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
    class GetWeatherArgs(BaseModel):
        """Get the temperature for the given country/city combo"""

        city: str
        country: str
        units: Literal["c", "f"] = "c"

    class GetStockPrice(BaseModel):
        ticker: str
        exchange: str

    listener = _make_stream_snapshot_request(
        lambda c: c.chat.stream(
            model="palmyra-x-003-instruct",
            messages=[
                {
                    "role": "user",
                    "content": "What's the weather like in Edinburgh?",
                },
                {
                    "role": "user",
                    "content": "What's the price of AAPL?",
                },
            ],
            tools=[
                writerai.pydantic_function_tool(GetWeatherArgs),
                writerai.pydantic_function_tool(
                    GetStockPrice, name="get_stock_price", description="Fetch the latest price for a given ticker"
                ),
            ],
        ),
        content_snapshot=snapshot(external("f82268f2fefd*.writer")),
        openai_content_snapshot=snapshot(external("f82268f2fefd*.openai")),
        mock_client=client,
        respx_mock=respx_mock,
    )

    assert print_obj(listener.stream.current_completion_snapshot.choices, monkeypatch) == snapshot(
        """\
[
    ParsedChatCompletionChoice[object](
        finish_reason='tool_calls',
        index=0,
        logprobs=None,
        message=ParsedChatCompletionMessage[object](
            content=None,
            graph_data=None,
            llm_data=None,
            parsed=None,
            refusal=None,
            role='assistant',
            tool_calls=[
                ParsedFunctionToolCall(
                    function=ParsedFunction(
                        arguments='{"city": "Edinburgh", "country": "GB", "units": "c"}',
                        name='GetWeatherArgs',
                        parsed_arguments=GetWeatherArgs(city='Edinburgh', country='GB', units='c')
                    ),
                    id='call_JMW1whyEaYG438VE1OIflxA2',
                    index=0,
                    type='function'
                ),
                ParsedFunctionToolCall(
                    function=ParsedFunction(
                        arguments='{"ticker": "AAPL", "exchange": "NASDAQ"}',
                        name='get_stock_price',
                        parsed_arguments=GetStockPrice(exchange='NASDAQ', ticker='AAPL')
                    ),
                    id='call_DNYTawLBoN8fj3KN6qU9N1Ou',
                    index=1,
                    type='function'
                )
            ]
        )
    )
]
"""
    )
    completion = listener.stream.get_final_completion()
    assert print_obj(completion.choices[0].message.tool_calls, monkeypatch) == snapshot(
        """\
[
    ParsedFunctionToolCall(
        function=ParsedFunction(
            arguments='{"city": "Edinburgh", "country": "GB", "units": "c"}',
            name='GetWeatherArgs',
            parsed_arguments=GetWeatherArgs(city='Edinburgh', country='GB', units='c')
        ),
        id='call_JMW1whyEaYG438VE1OIflxA2',
        index=0,
        type='function'
    ),
    ParsedFunctionToolCall(
        function=ParsedFunction(
            arguments='{"ticker": "AAPL", "exchange": "NASDAQ"}',
            name='get_stock_price',
            parsed_arguments=GetStockPrice(exchange='NASDAQ', ticker='AAPL')
        ),
        id='call_DNYTawLBoN8fj3KN6qU9N1Ou',
        index=1,
        type='function'
    )
]
"""
    )


# @pytest.mark.respx(base_url=base_url)
# def test_parse_strict_tools(client: Writer, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
#     listener = _make_stream_snapshot_request(
#         lambda c: c.chat.stream(
#             model="palmyra-x-003-instruct",
#             messages=[
#                 {
#                     "role": "user",
#                     "content": "What's the weather like in SF?",
#                 },
#             ],
#             tools=[
#                 {
#                     "type": "function",
#                     "function": {
#                         "name": "get_weather",
#                         "parameters": {
#                             "type": "object",
#                             "properties": {
#                                 "city": {"type": "string"},
#                                 "state": {"type": "string"},
#                             },
#                             "required": [
#                                 "city",
#                                 "state",
#                             ],
#                             "additionalProperties": False,
#                         },
#                         "strict": True,
#                     },
#                 }
#             ],
#         ),
#         content_snapshot=snapshot(external("a247c49c5fcd*_bin")),
#         mock_client=client,
#         respx_mock=respx_mock,
#     )

#     assert print_obj(listener.stream.current_completion_snapshot.choices, monkeypatch) == snapshot(
#         """\
# [
#     ParsedChatCompletionChoice[object](
#         finish_reason='tool_calls',
#         index=0,
#         logprobs=None,
#         message=ParsedChatCompletionMessage[object](
#             content=None,
#             graph_data=None,
#             parsed=None,
#             refusal=None,
#             role='assistant',
#             tool_calls=[
#                 ParsedFunctionToolCall(
#                     function=ParsedFunction(
#                         arguments='{"city":"San Francisco","state":"CA"}',
#                         name='get_weather',
#                         parsed_arguments={'city': 'San Francisco', 'state': 'CA'}
#                     ),
#                     id='call_CTf1nWJLqSeRgDqaCG27xZ74',
#                     index=0,
#                     type='function'
#                 )
#             ]
#         )
#     )
# ]
# """
#     )


@pytest.mark.respx(base_url=base_url)
def test_non_pydantic_response_format(client: Writer, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch) -> None:
    listener = _make_stream_snapshot_request(
        lambda c: c.chat.stream(
            model="palmyra-x-003-instruct",
            messages=[
                {
                    "role": "user",
                    "content": "What's the weather like in SF? Give me any JSON back",
                },
            ],
            # response_format={"type": "json_object"},
        ),
        content_snapshot=snapshot(external("d61558011839*.writer")),
        openai_content_snapshot=snapshot(external("d61558011839*.openai")),
        mock_client=client,
        respx_mock=respx_mock,
    )

    assert print_obj(listener.stream.get_final_completion().choices, monkeypatch) == snapshot(
        """\
[
    ParsedChatCompletionChoice[NoneType](
        finish_reason='stop',
        index=0,
        logprobs=None,
        message=ParsedChatCompletionMessage[NoneType](
            content='\\n  {\\n    "location": "San Francisco, CA",\\n    "weather": {\\n      "temperature": "18°C",\\n      
"condition": "Partly Cloudy",\\n      "humidity": "72%",\\n      "windSpeed": "15 km/h",\\n      "windDirection": "NW"\\n   
},\\n    "forecast": [\\n      {\\n        "day": "Monday",\\n        "high": "20°C",\\n        "low": "14°C",\\n        
"condition": "Sunny"\\n      },\\n      {\\n        "day": "Tuesday",\\n        "high": "19°C",\\n        "low": "15°C",\\n   
"condition": "Mostly Cloudy"\\n      },\\n      {\\n        "day": "Wednesday",\\n        "high": "18°C",\\n        "low": 
"14°C",\\n        "condition": "Cloudy"\\n      }\\n    ]\\n  }\\n',
            graph_data=None,
            llm_data=None,
            parsed=None,
            refusal=None,
            role='assistant',
            tool_calls=[]
        )
    )
]
"""
    )


@pytest.mark.respx(base_url=base_url)
def test_allows_non_strict_tools_but_no_parsing(
    client: Writer, respx_mock: MockRouter, monkeypatch: pytest.MonkeyPatch
) -> None:
    listener = _make_stream_snapshot_request(
        lambda c: c.chat.stream(
            model="palmyra-x-003-instruct",
            messages=[{"role": "user", "content": "what's the weather in NYC?"}],
            tools=[
                {
                    "type": "function",
                    "function": {
                        "name": "get_weather",
                        "parameters": {"type": "object", "properties": {"city": {"type": "string"}}},
                    },
                }
            ],
        ),
        content_snapshot=snapshot(external("2018feb66ae1*.writer")),
        openai_content_snapshot=snapshot(external("2018feb66ae1*.openai")),
        mock_client=client,
        respx_mock=respx_mock,
    )

    assert print_obj(listener.get_event_by_type("tool_calls.function.arguments.done"), monkeypatch) == snapshot("""\
FunctionToolCallArgumentsDoneEvent(
    arguments='{"city":"New York City"}',
    index=0,
    name='get_weather',
    parsed_arguments=None,
    tool_call_snapshot_id='call_4XzlGBLtUe9dy3GVNV4jhq7h',
    type='tool_calls.function.arguments.done'
)
""")

    assert print_obj(listener.stream.get_final_completion().choices, monkeypatch) == snapshot(
        """\
[
    ParsedChatCompletionChoice[NoneType](
        finish_reason='tool_calls',
        index=0,
        logprobs=None,
        message=ParsedChatCompletionMessage[NoneType](
            content=None,
            graph_data=None,
            llm_data=None,
            parsed=None,
            refusal=None,
            role='assistant',
            tool_calls=[
                ParsedFunctionToolCall(
                    function=ParsedFunction(
                        arguments='{"city":"New York City"}',
                        name='get_weather',
                        parsed_arguments=None
                    ),
                    id='call_4XzlGBLtUe9dy3GVNV4jhq7h',
                    index=0,
                    type='function'
                )
            ]
        )
    )
]
"""
    )


@pytest.mark.parametrize("sync", [True, False], ids=["sync", "async"])
def test_stream_method_in_sync(sync: bool, client: Writer, async_client: AsyncWriter) -> None:
    checking_client: Writer | AsyncWriter = client if sync else async_client

    assert_signatures_in_sync(
        checking_client.chat.chat,
        checking_client.chat.stream,
        exclude_params={"response_format", "stream"},
    )


class StreamListener(Generic[ResponseFormatT]):
    def __init__(self, stream: ChatCompletionStream[ResponseFormatT]) -> None:
        self.stream = stream
        self.events: list[ChatCompletionStreamEvent[ResponseFormatT]] = []

    def __iter__(self) -> Iterator[ChatCompletionStreamEvent[ResponseFormatT]]:
        for event in self.stream:
            self.events.append(event)
            yield event

    @overload
    def get_event_by_type(self, event_type: Literal["content.done"]) -> ContentDoneEvent[ResponseFormatT] | None: ...

    @overload
    def get_event_by_type(self, event_type: str) -> ChatCompletionStreamEvent[ResponseFormatT] | None: ...

    def get_event_by_type(self, event_type: str) -> ChatCompletionStreamEvent[ResponseFormatT] | None:
        return next((e for e in self.events if e.type == event_type), None)


def _make_stream_snapshot_request(
    func: Callable[[Writer], ChatCompletionStreamManager[ResponseFormatT]],
    *,
    content_snapshot: Any,
    openai_content_snapshot: Any,
    respx_mock: MockRouter,
    mock_client: Writer,
    on_event: Callable[[ChatCompletionStream[ResponseFormatT], ChatCompletionStreamEvent[ResponseFormatT]], Any]
    | None = None,
) -> StreamListener[ResponseFormatT]:
    def mock_response(snapshot: Any) -> Writer:
        respx_mock.post("/v1/chat").mock(
            return_value=httpx.Response(
                200,
                content=snapshot._old_value._load_value(),
                headers={"content-type": "text/event-stream"},
            )
        )
        return mock_client

    def consume_stream(client: Writer) -> StreamListener[ResponseFormatT]:
        with func(client) as stream:
            listener = StreamListener(stream)

            for event in listener:
                if on_event:
                    on_event(stream, event)
            return listener

    # Test against Writer's content snapshot
    live = os.environ.get("WRITER_LIVE") == "1"
    if live:

        def _on_response(response: httpx.Response) -> None:
            # update Writer's content snapshot
            assert outsource(response.read(), suffix=".writer") == content_snapshot

        respx_mock.stop()

        client = Writer(
            http_client=httpx.Client(
                event_hooks={
                    "response": [_on_response],
                }
            )
        )
    else:
        client = mock_response(content_snapshot)

    writer_listener = consume_stream(client)

    if live:
        client.close()

    # Ensure compatibility with OpenAI's content snapshot
    client = mock_response(openai_content_snapshot)
    consume_stream(client)

    return writer_listener
