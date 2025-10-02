# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .cms_blogs_tags_tag_param import CmsBlogsTagsTagParam

__all__ = ["TagCreateBatchParams"]


class TagCreateBatchParams(TypedDict, total=False):
    inputs: Required[Iterable[CmsBlogsTagsTagParam]]
