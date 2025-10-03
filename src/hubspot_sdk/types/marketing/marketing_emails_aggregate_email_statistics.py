# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .marketing_emails_email_statistics_data import MarketingEmailsEmailStatisticsData

__all__ = ["MarketingEmailsAggregateEmailStatistics"]


class MarketingEmailsAggregateEmailStatistics(BaseModel):
    aggregate: Optional[MarketingEmailsEmailStatisticsData] = None

    campaign_aggregations: Optional[Dict[str, MarketingEmailsEmailStatisticsData]] = FieldInfo(
        alias="campaignAggregations", default=None
    )

    emails: Optional[List[int]] = None
