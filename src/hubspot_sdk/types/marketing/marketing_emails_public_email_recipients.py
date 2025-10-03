# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MarketingEmailsPublicEmailRecipients"]


class MarketingEmailsPublicEmailRecipients(BaseModel):
    exclude: Optional[List[str]] = None

    include: Optional[List[str]] = None
