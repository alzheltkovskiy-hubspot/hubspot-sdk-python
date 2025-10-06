# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailStatisticsData"]


class EmailStatisticsData(BaseModel):
    counters: Dict[str, int]

    device_breakdown: Dict[str, Dict[str, int]] = FieldInfo(alias="deviceBreakdown")

    qualifier_stats: Dict[str, Dict[str, int]] = FieldInfo(alias="qualifierStats")

    ratios: Dict[str, float]
