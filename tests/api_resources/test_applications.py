# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.types import ApplicationGenerateContentResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApplications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_generate_content_overload_1(self, client: Writer) -> None:
        application = client.applications.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
        )
        assert_matches_type(ApplicationGenerateContentResponse, application, path=["response"])

    @parametrize
    def test_method_generate_content_with_all_params_overload_1(self, client: Writer) -> None:
        application = client.applications.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
            stream=False,
        )
        assert_matches_type(ApplicationGenerateContentResponse, application, path=["response"])

    @parametrize
    def test_raw_response_generate_content_overload_1(self, client: Writer) -> None:
        response = client.applications.with_raw_response.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(ApplicationGenerateContentResponse, application, path=["response"])

    @parametrize
    def test_streaming_response_generate_content_overload_1(self, client: Writer) -> None:
        with client.applications.with_streaming_response.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(ApplicationGenerateContentResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_generate_content_overload_1(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.with_raw_response.generate_content(
                application_id="",
                inputs=[
                    {
                        "id": "id",
                        "value": ["string"],
                    }
                ],
            )

    @parametrize
    def test_method_generate_content_overload_2(self, client: Writer) -> None:
        application_stream = client.applications.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
            stream=True,
        )
        application_stream.response.close()

    @parametrize
    def test_raw_response_generate_content_overload_2(self, client: Writer) -> None:
        response = client.applications.with_raw_response.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_generate_content_overload_2(self, client: Writer) -> None:
        with client.applications.with_streaming_response.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_generate_content_overload_2(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.with_raw_response.generate_content(
                application_id="",
                inputs=[
                    {
                        "id": "id",
                        "value": ["string"],
                    }
                ],
                stream=True,
            )


class TestAsyncApplications:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_generate_content_overload_1(self, async_client: AsyncWriter) -> None:
        application = await async_client.applications.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
        )
        assert_matches_type(ApplicationGenerateContentResponse, application, path=["response"])

    @parametrize
    async def test_method_generate_content_with_all_params_overload_1(self, async_client: AsyncWriter) -> None:
        application = await async_client.applications.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
            stream=False,
        )
        assert_matches_type(ApplicationGenerateContentResponse, application, path=["response"])

    @parametrize
    async def test_raw_response_generate_content_overload_1(self, async_client: AsyncWriter) -> None:
        response = await async_client.applications.with_raw_response.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(ApplicationGenerateContentResponse, application, path=["response"])

    @parametrize
    async def test_streaming_response_generate_content_overload_1(self, async_client: AsyncWriter) -> None:
        async with async_client.applications.with_streaming_response.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(ApplicationGenerateContentResponse, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_generate_content_overload_1(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.with_raw_response.generate_content(
                application_id="",
                inputs=[
                    {
                        "id": "id",
                        "value": ["string"],
                    }
                ],
            )

    @parametrize
    async def test_method_generate_content_overload_2(self, async_client: AsyncWriter) -> None:
        application_stream = await async_client.applications.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
            stream=True,
        )
        await application_stream.response.aclose()

    @parametrize
    async def test_raw_response_generate_content_overload_2(self, async_client: AsyncWriter) -> None:
        response = await async_client.applications.with_raw_response.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_generate_content_overload_2(self, async_client: AsyncWriter) -> None:
        async with async_client.applications.with_streaming_response.generate_content(
            application_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_generate_content_overload_2(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.with_raw_response.generate_content(
                application_id="",
                inputs=[
                    {
                        "id": "id",
                        "value": ["string"],
                    }
                ],
                stream=True,
            )
