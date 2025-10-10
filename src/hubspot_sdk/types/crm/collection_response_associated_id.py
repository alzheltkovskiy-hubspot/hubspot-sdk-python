# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..associated_id import AssociatedID
from ..marketing.marketing_emails_paging import MarketingEmailsPaging

__all__ = ["CollectionResponseAssociatedID"]


class CollectionResponseAssociatedID(BaseModel):
    results: List[AssociatedID]

    paging: Optional[MarketingEmailsPaging] = None
