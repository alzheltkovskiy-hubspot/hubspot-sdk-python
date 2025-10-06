# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging

__all__ = ["CollectionResponseFormDefinitionBaseForwardPaging"]


class CollectionResponseFormDefinitionBaseForwardPaging(BaseModel):
    results: List["HubSpotFormDefinition"]

    paging: Optional[ForwardPaging] = None


from .hub_spot_form_definition import HubSpotFormDefinition
