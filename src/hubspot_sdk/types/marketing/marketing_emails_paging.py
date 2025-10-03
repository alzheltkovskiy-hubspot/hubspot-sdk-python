# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..shared.next_page import NextPage
from ..shared.previous_page import PreviousPage

__all__ = ["MarketingEmailsPaging"]


class MarketingEmailsPaging(BaseModel):
    next: NextPage

    prev: Optional[PreviousPage] = None
