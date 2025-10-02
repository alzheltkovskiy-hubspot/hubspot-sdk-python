# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .crm_public_object_id import CRMPublicObjectID
from .crm.associations.crm_associations_v4_association_spec_1 import CRMAssociationsV4AssociationSpec1

__all__ = ["CRMPublicDefaultAssociation"]


class CRMPublicDefaultAssociation(BaseModel):
    association_spec: CRMAssociationsV4AssociationSpec1 = FieldInfo(alias="associationSpec")

    from_: CRMPublicObjectID = FieldInfo(alias="from")

    to: CRMPublicObjectID
