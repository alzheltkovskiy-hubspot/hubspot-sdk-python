# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CmsHubdbSimpleUser"]


class CmsHubdbSimpleUser(BaseModel):
    id: str

    email: str

    first_name: str = FieldInfo(alias="firstName")

    last_name: str = FieldInfo(alias="lastName")
