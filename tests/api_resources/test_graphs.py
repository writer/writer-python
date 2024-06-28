# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types import (
    File,
    Graph,
    GraphCreateResponse,
    GraphDeleteResponse,
    GraphUpdateResponse,
    GraphRemoveFileFromGraphResponse,
)
from writerai.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGraphs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Writer) -> None:
        graph = client.graphs.create(
            name="string",
        )
        assert_matches_type(GraphCreateResponse, graph, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Writer) -> None:
        graph = client.graphs.create(
            name="string",
            description="string",
        )
        assert_matches_type(GraphCreateResponse, graph, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Writer) -> None:
        response = client.graphs.with_raw_response.create(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(GraphCreateResponse, graph, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Writer) -> None:
        with client.graphs.with_streaming_response.create(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(GraphCreateResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Writer) -> None:
        graph = client.graphs.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Graph, graph, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Writer) -> None:
        response = client.graphs.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(Graph, graph, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Writer) -> None:
        with client.graphs.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(Graph, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `graph_id` but received ''"):
            client.graphs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Writer) -> None:
        graph = client.graphs.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )
        assert_matches_type(GraphUpdateResponse, graph, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Writer) -> None:
        graph = client.graphs.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            description="string",
        )
        assert_matches_type(GraphUpdateResponse, graph, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Writer) -> None:
        response = client.graphs.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(GraphUpdateResponse, graph, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Writer) -> None:
        with client.graphs.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(GraphUpdateResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `graph_id` but received ''"):
            client.graphs.with_raw_response.update(
                "",
                name="string",
            )

    @parametrize
    def test_method_list(self, client: Writer) -> None:
        graph = client.graphs.list()
        assert_matches_type(SyncCursorPage[Graph], graph, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Writer) -> None:
        graph = client.graphs.list(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            order="asc",
        )
        assert_matches_type(SyncCursorPage[Graph], graph, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Writer) -> None:
        response = client.graphs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(SyncCursorPage[Graph], graph, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Writer) -> None:
        with client.graphs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(SyncCursorPage[Graph], graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Writer) -> None:
        graph = client.graphs.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GraphDeleteResponse, graph, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Writer) -> None:
        response = client.graphs.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(GraphDeleteResponse, graph, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Writer) -> None:
        with client.graphs.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(GraphDeleteResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `graph_id` but received ''"):
            client.graphs.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_add_file_to_graph(self, client: Writer) -> None:
        graph = client.graphs.add_file_to_graph(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="string",
        )
        assert_matches_type(File, graph, path=["response"])

    @parametrize
    def test_raw_response_add_file_to_graph(self, client: Writer) -> None:
        response = client.graphs.with_raw_response.add_file_to_graph(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(File, graph, path=["response"])

    @parametrize
    def test_streaming_response_add_file_to_graph(self, client: Writer) -> None:
        with client.graphs.with_streaming_response.add_file_to_graph(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(File, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_file_to_graph(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `graph_id` but received ''"):
            client.graphs.with_raw_response.add_file_to_graph(
                "",
                file_id="string",
            )

    @parametrize
    def test_method_remove_file_from_graph(self, client: Writer) -> None:
        graph = client.graphs.remove_file_from_graph(
            "string",
            graph_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GraphRemoveFileFromGraphResponse, graph, path=["response"])

    @parametrize
    def test_raw_response_remove_file_from_graph(self, client: Writer) -> None:
        response = client.graphs.with_raw_response.remove_file_from_graph(
            "string",
            graph_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = response.parse()
        assert_matches_type(GraphRemoveFileFromGraphResponse, graph, path=["response"])

    @parametrize
    def test_streaming_response_remove_file_from_graph(self, client: Writer) -> None:
        with client.graphs.with_streaming_response.remove_file_from_graph(
            "string",
            graph_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = response.parse()
            assert_matches_type(GraphRemoveFileFromGraphResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_remove_file_from_graph(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `graph_id` but received ''"):
            client.graphs.with_raw_response.remove_file_from_graph(
                "string",
                graph_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.graphs.with_raw_response.remove_file_from_graph(
                "",
                graph_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncGraphs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncWriter) -> None:
        graph = await async_client.graphs.create(
            name="string",
        )
        assert_matches_type(GraphCreateResponse, graph, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncWriter) -> None:
        graph = await async_client.graphs.create(
            name="string",
            description="string",
        )
        assert_matches_type(GraphCreateResponse, graph, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWriter) -> None:
        response = await async_client.graphs.with_raw_response.create(
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(GraphCreateResponse, graph, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWriter) -> None:
        async with async_client.graphs.with_streaming_response.create(
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(GraphCreateResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWriter) -> None:
        graph = await async_client.graphs.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Graph, graph, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWriter) -> None:
        response = await async_client.graphs.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(Graph, graph, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWriter) -> None:
        async with async_client.graphs.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(Graph, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `graph_id` but received ''"):
            await async_client.graphs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncWriter) -> None:
        graph = await async_client.graphs.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )
        assert_matches_type(GraphUpdateResponse, graph, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncWriter) -> None:
        graph = await async_client.graphs.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
            description="string",
        )
        assert_matches_type(GraphUpdateResponse, graph, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncWriter) -> None:
        response = await async_client.graphs.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(GraphUpdateResponse, graph, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncWriter) -> None:
        async with async_client.graphs.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(GraphUpdateResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `graph_id` but received ''"):
            await async_client.graphs.with_raw_response.update(
                "",
                name="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncWriter) -> None:
        graph = await async_client.graphs.list()
        assert_matches_type(AsyncCursorPage[Graph], graph, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWriter) -> None:
        graph = await async_client.graphs.list(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            order="asc",
        )
        assert_matches_type(AsyncCursorPage[Graph], graph, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWriter) -> None:
        response = await async_client.graphs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(AsyncCursorPage[Graph], graph, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWriter) -> None:
        async with async_client.graphs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(AsyncCursorPage[Graph], graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncWriter) -> None:
        graph = await async_client.graphs.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GraphDeleteResponse, graph, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncWriter) -> None:
        response = await async_client.graphs.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(GraphDeleteResponse, graph, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncWriter) -> None:
        async with async_client.graphs.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(GraphDeleteResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `graph_id` but received ''"):
            await async_client.graphs.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_add_file_to_graph(self, async_client: AsyncWriter) -> None:
        graph = await async_client.graphs.add_file_to_graph(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="string",
        )
        assert_matches_type(File, graph, path=["response"])

    @parametrize
    async def test_raw_response_add_file_to_graph(self, async_client: AsyncWriter) -> None:
        response = await async_client.graphs.with_raw_response.add_file_to_graph(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(File, graph, path=["response"])

    @parametrize
    async def test_streaming_response_add_file_to_graph(self, async_client: AsyncWriter) -> None:
        async with async_client.graphs.with_streaming_response.add_file_to_graph(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(File, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_file_to_graph(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `graph_id` but received ''"):
            await async_client.graphs.with_raw_response.add_file_to_graph(
                "",
                file_id="string",
            )

    @parametrize
    async def test_method_remove_file_from_graph(self, async_client: AsyncWriter) -> None:
        graph = await async_client.graphs.remove_file_from_graph(
            "string",
            graph_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GraphRemoveFileFromGraphResponse, graph, path=["response"])

    @parametrize
    async def test_raw_response_remove_file_from_graph(self, async_client: AsyncWriter) -> None:
        response = await async_client.graphs.with_raw_response.remove_file_from_graph(
            "string",
            graph_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        graph = await response.parse()
        assert_matches_type(GraphRemoveFileFromGraphResponse, graph, path=["response"])

    @parametrize
    async def test_streaming_response_remove_file_from_graph(self, async_client: AsyncWriter) -> None:
        async with async_client.graphs.with_streaming_response.remove_file_from_graph(
            "string",
            graph_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            graph = await response.parse()
            assert_matches_type(GraphRemoveFileFromGraphResponse, graph, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_remove_file_from_graph(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `graph_id` but received ''"):
            await async_client.graphs.with_raw_response.remove_file_from_graph(
                "string",
                graph_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.graphs.with_raw_response.remove_file_from_graph(
                "",
                graph_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
