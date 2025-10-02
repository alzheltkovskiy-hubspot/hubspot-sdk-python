# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.paging import Paging
from ..crm_associated_id import CRMAssociatedID
from ..crm_public_object_id import CRMPublicObjectID

__all__ = ["CRMAssociationsPublicAssociationMulti"]


class CRMAssociationsPublicAssociationMulti(BaseModel):
    from_: CRMPublicObjectID = FieldInfo(alias="from")

    to: List[CRMAssociatedID]

    paging: Optional[Paging] = None
