# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CRMLabelsBetweenObjectPair"]


class CRMLabelsBetweenObjectPair(BaseModel):
    from_object_id: str = FieldInfo(alias="fromObjectId")

    from_object_type_id: str = FieldInfo(alias="fromObjectTypeId")

    labels: List[str]

    to_object_id: str = FieldInfo(alias="toObjectId")

    to_object_type_id: str = FieldInfo(alias="toObjectTypeId")
