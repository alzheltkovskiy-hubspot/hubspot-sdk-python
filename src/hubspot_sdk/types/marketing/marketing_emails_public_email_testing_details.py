# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketingEmailsPublicEmailTestingDetails"]


class MarketingEmailsPublicEmailTestingDetails(BaseModel):
    ab_sample_size_default: Optional[
        Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ]
    ] = FieldInfo(alias="abSampleSizeDefault", default=None)

    ab_sampling_default: Optional[
        Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ]
    ] = FieldInfo(alias="abSamplingDefault", default=None)

    ab_status: Optional[
        Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ]
    ] = FieldInfo(alias="abStatus", default=None)

    ab_success_metric: Optional[Literal["CLICKS_BY_OPENS", "CLICKS_BY_DELIVERED", "OPENS_BY_DELIVERED"]] = FieldInfo(
        alias="abSuccessMetric", default=None
    )

    ab_test_percentage: Optional[int] = FieldInfo(alias="abTestPercentage", default=None)

    hours_to_wait: Optional[int] = FieldInfo(alias="hoursToWait", default=None)

    test_id: Optional[str] = FieldInfo(alias="testId", default=None)
