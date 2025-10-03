# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..crm_associated_id import CRMAssociatedID
from ..marketing.marketing_emails_paging import MarketingEmailsPaging

__all__ = ["CRMObjectsCollectionResponseAssociatedID"]


class CRMObjectsCollectionResponseAssociatedID(BaseModel):
    results: List[CRMAssociatedID]

    paging: Optional[MarketingEmailsPaging] = None
