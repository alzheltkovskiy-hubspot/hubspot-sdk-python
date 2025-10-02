# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AutomationActionsPublicActionFunctionIdentifier"]


class AutomationActionsPublicActionFunctionIdentifier(BaseModel):
    function_type: Literal[
        "PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"
    ] = FieldInfo(alias="functionType")

    id: Optional[str] = None
