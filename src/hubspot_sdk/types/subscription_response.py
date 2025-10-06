# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SubscriptionResponse"]


class SubscriptionResponse(BaseModel):
    id: str

    active: bool

    created_at: datetime = FieldInfo(alias="createdAt")

    event_type: Literal[
        "contact.propertyChange",
        "company.propertyChange",
        "deal.propertyChange",
        "ticket.propertyChange",
        "product.propertyChange",
        "line_item.propertyChange",
        "contact.creation",
        "contact.deletion",
        "contact.privacyDeletion",
        "company.creation",
        "company.deletion",
        "deal.creation",
        "deal.deletion",
        "ticket.creation",
        "ticket.deletion",
        "product.creation",
        "product.deletion",
        "line_item.creation",
        "line_item.deletion",
        "conversation.creation",
        "conversation.deletion",
        "conversation.newMessage",
        "conversation.privacyDeletion",
        "conversation.propertyChange",
        "contact.merge",
        "company.merge",
        "deal.merge",
        "ticket.merge",
        "product.merge",
        "line_item.merge",
        "contact.restore",
        "company.restore",
        "deal.restore",
        "ticket.restore",
        "product.restore",
        "line_item.restore",
        "contact.associationChange",
        "company.associationChange",
        "deal.associationChange",
        "ticket.associationChange",
        "line_item.associationChange",
        "object.propertyChange",
        "object.creation",
        "object.deletion",
        "object.merge",
        "object.restore",
        "object.associationChange",
    ] = FieldInfo(alias="eventType")

    object_type_id: Optional[str] = FieldInfo(alias="objectTypeId", default=None)

    property_name: Optional[str] = FieldInfo(alias="propertyName", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
