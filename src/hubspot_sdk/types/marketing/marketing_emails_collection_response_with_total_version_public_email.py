# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .marketing_emails_paging import MarketingEmailsPaging
from .marketing_emails_version_public_email import MarketingEmailsVersionPublicEmail

__all__ = ["MarketingEmailsCollectionResponseWithTotalVersionPublicEmail"]


class MarketingEmailsCollectionResponseWithTotalVersionPublicEmail(BaseModel):
    results: List[MarketingEmailsVersionPublicEmail]

    total: int

    paging: Optional[MarketingEmailsPaging] = None
