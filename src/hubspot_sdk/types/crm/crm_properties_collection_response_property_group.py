# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .crm_properties_property_group import CRMPropertiesPropertyGroup
from ..marketing.marketing_emails_paging import MarketingEmailsPaging

__all__ = ["CRMPropertiesCollectionResponsePropertyGroup"]


class CRMPropertiesCollectionResponsePropertyGroup(BaseModel):
    results: List[CRMPropertiesPropertyGroup]

    paging: Optional[MarketingEmailsPaging] = None
