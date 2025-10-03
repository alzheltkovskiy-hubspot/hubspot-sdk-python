# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .files_folder import FilesFolder
from .marketing.marketing_emails_paging import MarketingEmailsPaging

__all__ = ["FilesCollectionResponseFolder"]


class FilesCollectionResponseFolder(BaseModel):
    results: List[FilesFolder]

    paging: Optional[MarketingEmailsPaging] = None
