# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

import httpx

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["CursorURLPagePaging", "CursorURLPageNext", "SyncCursorURLPage", "AsyncCursorURLPage"]

_T = TypeVar("_T")


class CursorURLPageNext(BaseModel):
    link: Optional[str] = None


class CursorURLPagePaging(BaseModel):
    next: Optional[CursorURLPageNext] = None


class SyncCursorURLPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    paging: Optional[CursorURLPagePaging] = None

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        url = None
        if self.paging is not None:
            if self.paging.next is not None:
                if self.paging.next.link is not None:
                    url = self.paging.next.link
        if url is None:
            return None

        return PageInfo(url=httpx.URL(url))


class AsyncCursorURLPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    paging: Optional[CursorURLPagePaging] = None

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        url = None
        if self.paging is not None:
            if self.paging.next is not None:
                if self.paging.next.link is not None:
                    url = self.paging.next.link
        if url is None:
            return None

        return PageInfo(url=httpx.URL(url))
