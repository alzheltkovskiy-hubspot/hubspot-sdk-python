# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .folder import Folder
from .._models import BaseModel
from .marketing.marketing_emails_paging import MarketingEmailsPaging

__all__ = ["CollectionResponseFolder"]


class CollectionResponseFolder(BaseModel):
    results: List[Folder]

    paging: Optional[MarketingEmailsPaging] = None
