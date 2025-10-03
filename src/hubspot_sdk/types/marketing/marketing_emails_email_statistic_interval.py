# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .marketing_emails_interval import MarketingEmailsInterval
from .marketing_emails_email_statistics_data import MarketingEmailsEmailStatisticsData

__all__ = ["MarketingEmailsEmailStatisticInterval"]


class MarketingEmailsEmailStatisticInterval(BaseModel):
    aggregations: Optional[MarketingEmailsEmailStatisticsData] = None

    interval: Optional[MarketingEmailsInterval] = None
