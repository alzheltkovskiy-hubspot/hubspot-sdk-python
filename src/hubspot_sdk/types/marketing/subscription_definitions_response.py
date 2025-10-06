# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .subscription_definition import SubscriptionDefinition

__all__ = ["SubscriptionDefinitionsResponse"]


class SubscriptionDefinitionsResponse(BaseModel):
    subscription_definitions: List[SubscriptionDefinition] = FieldInfo(alias="subscriptionDefinitions")
