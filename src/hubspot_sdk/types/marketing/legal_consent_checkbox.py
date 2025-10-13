# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LegalConsentCheckbox"]


class LegalConsentCheckbox(BaseModel):
    label: str
    """The main label for the form field."""

    required: bool
    """Whether this checkbox is required when submitting the form."""

    subscription_type_id: int = FieldInfo(alias="subscriptionTypeId")
