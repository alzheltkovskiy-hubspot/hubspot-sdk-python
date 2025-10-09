# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["PagePaging", "PageNext", "SyncPage", "AsyncPage"]

_T = TypeVar("_T")


class PageNext(BaseModel):
    after: Optional[str] = None


class PagePaging(BaseModel):
    next: Optional[PageNext] = None


class SyncPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    paging: Optional[PagePaging] = None

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        after = None
        if self.paging is not None:
            if self.paging.next is not None:
                if self.paging.next.after is not None:
                    after = self.paging.next.after
        if not after:
            return None

        return PageInfo(params={"after": after})


class AsyncPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    paging: Optional[PagePaging] = None

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        after = None
        if self.paging is not None:
            if self.paging.next is not None:
                if self.paging.next.after is not None:
                    after = self.paging.next.after
        if not after:
            return None

        return PageInfo(params={"after": after})
