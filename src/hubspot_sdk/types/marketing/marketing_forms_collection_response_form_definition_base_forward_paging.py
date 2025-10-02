# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging

__all__ = ["MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging"]


class MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging(BaseModel):
    results: List["MarketingFormsHubSpotFormDefinition"]

    paging: Optional[ForwardPaging] = None


from .marketing_forms_hub_spot_form_definition import MarketingFormsHubSpotFormDefinition
