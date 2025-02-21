# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from writerai import Writer, AsyncWriter
from tests.utils import assert_matches_type
from writerai.pagination import SyncApplicationJobsOffset, AsyncApplicationJobsOffset
from writerai.types.applications import (
    JobRetryResponse,
    JobCreateResponse,
    ApplicationGenerateAsyncResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Writer) -> None:
        job = client.applications.jobs.create(
            application_id="application_id",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Writer) -> None:
        response = client.applications.jobs.with_raw_response.create(
            application_id="application_id",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Writer) -> None:
        with client.applications.jobs.with_streaming_response.create(
            application_id="application_id",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.jobs.with_raw_response.create(
                application_id="",
                inputs=[
                    {
                        "id": "id",
                        "value": ["string"],
                    }
                ],
            )

    @parametrize
    def test_method_retrieve(self, client: Writer) -> None:
        job = client.applications.jobs.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ApplicationGenerateAsyncResponse, job, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Writer) -> None:
        response = client.applications.jobs.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(ApplicationGenerateAsyncResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Writer) -> None:
        with client.applications.jobs.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(ApplicationGenerateAsyncResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.applications.jobs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Writer) -> None:
        job = client.applications.jobs.list(
            application_id="application_id",
        )
        assert_matches_type(SyncApplicationJobsOffset[ApplicationGenerateAsyncResponse], job, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Writer) -> None:
        job = client.applications.jobs.list(
            application_id="application_id",
            limit=0,
            offset=0,
            status="in_progress",
        )
        assert_matches_type(SyncApplicationJobsOffset[ApplicationGenerateAsyncResponse], job, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Writer) -> None:
        response = client.applications.jobs.with_raw_response.list(
            application_id="application_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(SyncApplicationJobsOffset[ApplicationGenerateAsyncResponse], job, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Writer) -> None:
        with client.applications.jobs.with_streaming_response.list(
            application_id="application_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(SyncApplicationJobsOffset[ApplicationGenerateAsyncResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.applications.jobs.with_raw_response.list(
                application_id="",
            )

    @parametrize
    def test_method_retry(self, client: Writer) -> None:
        job = client.applications.jobs.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobRetryResponse, job, path=["response"])

    @parametrize
    def test_raw_response_retry(self, client: Writer) -> None:
        response = client.applications.jobs.with_raw_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobRetryResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_retry(self, client: Writer) -> None:
        with client.applications.jobs.with_streaming_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(JobRetryResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retry(self, client: Writer) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.applications.jobs.with_raw_response.retry(
                "",
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncWriter) -> None:
        job = await async_client.applications.jobs.create(
            application_id="application_id",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
        )
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncWriter) -> None:
        response = await async_client.applications.jobs.with_raw_response.create(
            application_id="application_id",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobCreateResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncWriter) -> None:
        async with async_client.applications.jobs.with_streaming_response.create(
            application_id="application_id",
            inputs=[
                {
                    "id": "id",
                    "value": ["string"],
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobCreateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.jobs.with_raw_response.create(
                application_id="",
                inputs=[
                    {
                        "id": "id",
                        "value": ["string"],
                    }
                ],
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncWriter) -> None:
        job = await async_client.applications.jobs.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ApplicationGenerateAsyncResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncWriter) -> None:
        response = await async_client.applications.jobs.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(ApplicationGenerateAsyncResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncWriter) -> None:
        async with async_client.applications.jobs.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(ApplicationGenerateAsyncResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.applications.jobs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncWriter) -> None:
        job = await async_client.applications.jobs.list(
            application_id="application_id",
        )
        assert_matches_type(AsyncApplicationJobsOffset[ApplicationGenerateAsyncResponse], job, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncWriter) -> None:
        job = await async_client.applications.jobs.list(
            application_id="application_id",
            limit=0,
            offset=0,
            status="in_progress",
        )
        assert_matches_type(AsyncApplicationJobsOffset[ApplicationGenerateAsyncResponse], job, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncWriter) -> None:
        response = await async_client.applications.jobs.with_raw_response.list(
            application_id="application_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(AsyncApplicationJobsOffset[ApplicationGenerateAsyncResponse], job, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncWriter) -> None:
        async with async_client.applications.jobs.with_streaming_response.list(
            application_id="application_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(AsyncApplicationJobsOffset[ApplicationGenerateAsyncResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.applications.jobs.with_raw_response.list(
                application_id="",
            )

    @parametrize
    async def test_method_retry(self, async_client: AsyncWriter) -> None:
        job = await async_client.applications.jobs.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobRetryResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncWriter) -> None:
        response = await async_client.applications.jobs.with_raw_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobRetryResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncWriter) -> None:
        async with async_client.applications.jobs.with_streaming_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(JobRetryResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retry(self, async_client: AsyncWriter) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.applications.jobs.with_raw_response.retry(
                "",
            )
