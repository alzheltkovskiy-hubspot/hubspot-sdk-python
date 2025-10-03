# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .marketing_emails_email_statistic_interval import MarketingEmailsEmailStatisticInterval

__all__ = ["MarketingEmailsCollectionResponseWithTotalEmailStatisticIntervalNoPaging"]


class MarketingEmailsCollectionResponseWithTotalEmailStatisticIntervalNoPaging(BaseModel):
    results: List[MarketingEmailsEmailStatisticInterval]

    total: int
