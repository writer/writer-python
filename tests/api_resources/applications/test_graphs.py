# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types.applications import ApplicationGraphsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGraphs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Writer) -> None:
        graph = client.applications.graphs.update(
            application_id="application_id",
            graph_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(ApplicationGraphsResponse, graph, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Writer) -> None:
        response = client.applications.graphs.with_raw_response.update(
            application_id="application_id",
            graph_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(ApplicationGraphsResponse, graph, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Writer) -> None:
        with client.applications.graphs.with_streaming_response.update(
            application_id="application_id",
            graph_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(ApplicationGraphsResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.graphs.with_raw_response.update(
                application_id="",
                graph_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    def test_method_list(self, client: Writer) -> None:
        graph = client.applications.graphs.list(
            "application_id",
        )
        assert_matches_type(ApplicationGraphsResponse, graph, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Writer) -> None:
        response = client.applications.graphs.with_raw_response.list(
            "application_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(ApplicationGraphsResponse, graph, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Writer) -> None:
        with client.applications.graphs.with_streaming_response.list(
            "application_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(ApplicationGraphsResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.graphs.with_raw_response.list(
                "",
            )


class TestAsyncGraphs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncWriter) -> None:
        graph = await async_client.applications.graphs.update(
            application_id="application_id",
            graph_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(ApplicationGraphsResponse, graph, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWriter) -> None:
        response = await async_client.applications.graphs.with_raw_response.update(
            application_id="application_id",
            graph_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(ApplicationGraphsResponse, graph, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWriter) -> None:
        async with async_client.applications.graphs.with_streaming_response.update(
            application_id="application_id",
            graph_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(ApplicationGraphsResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.graphs.with_raw_response.update(
                application_id="",
                graph_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncWriter) -> None:
        graph = await async_client.applications.graphs.list(
            "application_id",
        )
        assert_matches_type(ApplicationGraphsResponse, graph, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWriter) -> None:
        response = await async_client.applications.graphs.with_raw_response.list(
            "application_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(ApplicationGraphsResponse, graph, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWriter) -> None:
        async with async_client.applications.graphs.with_streaming_response.list(
            "application_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(ApplicationGraphsResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.graphs.with_raw_response.list(
                "",
            )
