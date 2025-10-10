# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .version_public_email import VersionPublicEmail
from .marketing_emails_paging import MarketingEmailsPaging

__all__ = ["CollectionResponseWithTotalVersionPublicEmail"]


class CollectionResponseWithTotalVersionPublicEmail(BaseModel):
    results: List[VersionPublicEmail]

    total: int

    paging: Optional[MarketingEmailsPaging] = None
