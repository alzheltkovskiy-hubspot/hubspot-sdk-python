# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .crm.associations.crm_associations_v4_association_spec_with_label_1 import (
    CRMAssociationsV4AssociationSpecWithLabel1,
)

__all__ = ["CRMMultiAssociatedObjectWithLabel"]


class CRMMultiAssociatedObjectWithLabel(BaseModel):
    association_types: List[CRMAssociationsV4AssociationSpecWithLabel1] = FieldInfo(alias="associationTypes")

    to_object_id: str = FieldInfo(alias="toObjectId")
