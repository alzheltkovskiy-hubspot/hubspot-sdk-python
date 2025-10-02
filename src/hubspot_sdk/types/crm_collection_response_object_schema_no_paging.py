# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .crm_object_schema import CRMObjectSchema

__all__ = ["CRMCollectionResponseObjectSchemaNoPaging"]


class CRMCollectionResponseObjectSchemaNoPaging(BaseModel):
    results: List[CRMObjectSchema]
