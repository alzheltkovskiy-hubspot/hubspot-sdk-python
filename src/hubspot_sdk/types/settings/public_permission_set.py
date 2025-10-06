# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PublicPermissionSet"]


class PublicPermissionSet(BaseModel):
    id: str

    name: str

    requires_billing_write: bool = FieldInfo(alias="requiresBillingWrite")
