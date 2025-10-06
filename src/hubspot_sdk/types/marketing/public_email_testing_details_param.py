# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PublicEmailTestingDetailsParam"]


class PublicEmailTestingDetailsParam(TypedDict, total=False):
    ab_sample_size_default: Annotated[
        Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ],
        PropertyInfo(alias="abSampleSizeDefault"),
    ]

    ab_sampling_default: Annotated[
        Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ],
        PropertyInfo(alias="abSamplingDefault"),
    ]

    ab_status: Annotated[
        Literal[
            "master",
            "variant",
            "loser_variant",
            "mab_master",
            "mab_variant",
            "automated_master",
            "automated_variant",
            "automated_loser_variant",
        ],
        PropertyInfo(alias="abStatus"),
    ]

    ab_success_metric: Annotated[
        Literal["CLICKS_BY_OPENS", "CLICKS_BY_DELIVERED", "OPENS_BY_DELIVERED"], PropertyInfo(alias="abSuccessMetric")
    ]

    ab_test_percentage: Annotated[int, PropertyInfo(alias="abTestPercentage")]

    hours_to_wait: Annotated[int, PropertyInfo(alias="hoursToWait")]

    test_id: Annotated[str, PropertyInfo(alias="testId")]
