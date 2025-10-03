# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["EmailReadParams"]


class EmailReadParams(TypedDict, total=False):
    archived: bool

    included_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="includedProperties")]

    include_stats: Annotated[bool, PropertyInfo(alias="includeStats")]

    marketing_campaign_names: Annotated[bool, PropertyInfo(alias="marketingCampaignNames")]

    workflow_names: Annotated[bool, PropertyInfo(alias="workflowNames")]
