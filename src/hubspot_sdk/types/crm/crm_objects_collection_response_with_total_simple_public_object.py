# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .crm_objects_simple_public_object import CRMObjectsSimplePublicObject
from ..marketing.marketing_emails_paging import MarketingEmailsPaging

__all__ = ["CRMObjectsCollectionResponseWithTotalSimplePublicObject"]


class CRMObjectsCollectionResponseWithTotalSimplePublicObject(BaseModel):
    results: List[CRMObjectsSimplePublicObject]

    total: int

    paging: Optional[MarketingEmailsPaging] = None
