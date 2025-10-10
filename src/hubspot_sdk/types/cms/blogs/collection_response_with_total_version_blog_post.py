# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ...._models import BaseModel
from ...marketing.marketing_emails_paging import MarketingEmailsPaging

__all__ = ["CollectionResponseWithTotalVersionBlogPost"]


class CollectionResponseWithTotalVersionBlogPost(BaseModel):
    results: List["VersionBlogPost"]

    total: int

    paging: Optional[MarketingEmailsPaging] = None


from .version_blog_post import VersionBlogPost
