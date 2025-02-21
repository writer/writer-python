# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Generic, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable

from pydantic import Field as FieldInfo

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncCursorPage",
    "AsyncCursorPage",
    "ApplicationJobsOffsetPagination",
    "SyncApplicationJobsOffset",
    "AsyncApplicationJobsOffset",
]

_T = TypeVar("_T")


@runtime_checkable
class CursorPageItem(Protocol):
    id: Optional[str]


class SyncCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    has_more: bool

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        return has_more and super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("before", False)

        data = self.data
        if not data:
            return None

        if is_forwards:
            item = cast(Any, data[-1])
            if not isinstance(item, CursorPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"after": item.id})
        else:
            item = cast(Any, self.data[0])
            if not isinstance(item, CursorPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"before": item.id})


class AsyncCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    has_more: bool

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        has_more = self.has_more
        return has_more and super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("before", False)

        data = self.data
        if not data:
            return None

        if is_forwards:
            item = cast(Any, data[-1])
            if not isinstance(item, CursorPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"after": item.id})
        else:
            item = cast(Any, self.data[0])
            if not isinstance(item, CursorPageItem) or item.id is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"before": item.id})


class ApplicationJobsOffsetPagination(BaseModel):
    limit: Optional[int] = None

    offset: Optional[int] = None


class SyncApplicationJobsOffset(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    result: List[_T]
    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)
    pagination: Optional[ApplicationJobsOffsetPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        result = self.result
        if not result:
            return []
        return result

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = None
        if self.pagination is not None:
            if self.pagination.offset is not None:
                offset = self.pagination.offset
        if offset is None:
            return None

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncApplicationJobsOffset(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    result: List[_T]
    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)
    pagination: Optional[ApplicationJobsOffsetPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        result = self.result
        if not result:
            return []
        return result

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = None
        if self.pagination is not None:
            if self.pagination.offset is not None:
                offset = self.pagination.offset
        if offset is None:
            return None

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None
