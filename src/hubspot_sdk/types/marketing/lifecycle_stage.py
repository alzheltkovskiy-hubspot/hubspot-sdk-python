# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LifecycleStage"]


class LifecycleStage(BaseModel):
    object_type_id: str = FieldInfo(alias="objectTypeId")
    """The objectTypeId for both contact and company"""

    value: str
    """The internal name of the contact's lifecycle stage set when submitting a form"""
