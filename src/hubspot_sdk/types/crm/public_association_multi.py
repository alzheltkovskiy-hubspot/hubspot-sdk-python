# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..associated_id import AssociatedID
from ..shared.public_object_id import PublicObjectID
from ..marketing.marketing_emails_paging import MarketingEmailsPaging

__all__ = ["PublicAssociationMulti"]


class PublicAssociationMulti(BaseModel):
    from_: PublicObjectID = FieldInfo(alias="from")

    to: List[AssociatedID]

    paging: Optional[MarketingEmailsPaging] = None
