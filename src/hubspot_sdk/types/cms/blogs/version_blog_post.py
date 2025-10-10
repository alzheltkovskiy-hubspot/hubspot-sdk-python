# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...shared.version_user import VersionUser

__all__ = ["VersionBlogPost"]


class VersionBlogPost(BaseModel):
    id: str

    object: "BlogPost"

    updated_at: datetime = FieldInfo(alias="updatedAt")

    user: VersionUser


from .blog_post import BlogPost
