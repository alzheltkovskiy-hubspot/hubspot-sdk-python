# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AssociationSpecWithLabel1"]


class AssociationSpecWithLabel1(BaseModel):
    category: Literal["HUBSPOT_DEFINED", "USER_DEFINED", "INTEGRATOR_DEFINED"]
    """The category of this association type (either HUBSPOT_DEFINED or USER_DEFINED)"""

    type_id: int = FieldInfo(alias="typeId")
    """The ID of this association type, unique within an association category"""

    label: Optional[str] = None
    """The label for this association type"""
