# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .cms_domains_domain import CmsDomainsDomain
from ..shared.forward_paging import ForwardPaging

__all__ = ["CmsDomainsCollectionResponseWithTotalDomainForwardPaging"]


class CmsDomainsCollectionResponseWithTotalDomainForwardPaging(BaseModel):
    results: List[CmsDomainsDomain]

    total: int

    paging: Optional[ForwardPaging] = None
