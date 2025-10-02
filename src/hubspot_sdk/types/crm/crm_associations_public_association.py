# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..crm_public_object_id import CRMPublicObjectID

__all__ = ["CRMAssociationsPublicAssociation"]


class CRMAssociationsPublicAssociation(BaseModel):
    from_: CRMPublicObjectID = FieldInfo(alias="from")

    to: CRMPublicObjectID

    type: str
