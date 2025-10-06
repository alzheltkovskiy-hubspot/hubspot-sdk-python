# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Domain"]


class Domain(BaseModel):
    id: str

    domain: str

    is_resolving: bool = FieldInfo(alias="isResolving")

    is_used_for_blog_post: bool = FieldInfo(alias="isUsedForBlogPost")

    is_used_for_email: bool = FieldInfo(alias="isUsedForEmail")

    is_used_for_knowledge: bool = FieldInfo(alias="isUsedForKnowledge")

    is_used_for_landing_page: bool = FieldInfo(alias="isUsedForLandingPage")

    is_used_for_site_page: bool = FieldInfo(alias="isUsedForSitePage")

    correct_cname: Optional[str] = FieldInfo(alias="correctCname", default=None)

    created: Optional[datetime] = None

    is_ssl_enabled: Optional[bool] = FieldInfo(alias="isSslEnabled", default=None)

    is_ssl_only: Optional[bool] = FieldInfo(alias="isSslOnly", default=None)

    manually_marked_as_resolving: Optional[bool] = FieldInfo(alias="manuallyMarkedAsResolving", default=None)

    primary_blog_post: Optional[bool] = FieldInfo(alias="primaryBlogPost", default=None)

    primary_email: Optional[bool] = FieldInfo(alias="primaryEmail", default=None)

    primary_knowledge: Optional[bool] = FieldInfo(alias="primaryKnowledge", default=None)

    primary_landing_page: Optional[bool] = FieldInfo(alias="primaryLandingPage", default=None)

    primary_site_page: Optional[bool] = FieldInfo(alias="primarySitePage", default=None)

    secondary_to_domain: Optional[str] = FieldInfo(alias="secondaryToDomain", default=None)

    updated: Optional[datetime] = None
