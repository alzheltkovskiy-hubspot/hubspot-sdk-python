# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .simple_public_object import SimplePublicObject
from ..marketing.marketing_emails_paging import MarketingEmailsPaging

__all__ = ["CollectionResponseWithTotalSimplePublicObject"]


class CollectionResponseWithTotalSimplePublicObject(BaseModel):
    results: List[SimplePublicObject]

    total: int

    paging: Optional[MarketingEmailsPaging] = None
