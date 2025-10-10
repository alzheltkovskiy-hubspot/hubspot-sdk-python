# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .file import File
from .._models import BaseModel
from .marketing.marketing_emails_paging import MarketingEmailsPaging

__all__ = ["CollectionResponseFile"]


class CollectionResponseFile(BaseModel):
    results: List[File]

    paging: Optional[MarketingEmailsPaging] = None
