# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .marketing_emails_public_email import MarketingEmailsPublicEmail

__all__ = ["MarketingEmailsCollectionResponseWithTotalPublicEmailForwardPaging"]


class MarketingEmailsCollectionResponseWithTotalPublicEmailForwardPaging(BaseModel):
    results: List[MarketingEmailsPublicEmail]

    total: int

    paging: Optional[ForwardPaging] = None
