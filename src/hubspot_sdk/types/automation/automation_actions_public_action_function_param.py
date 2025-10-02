# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AutomationActionsPublicActionFunctionParam"]


class AutomationActionsPublicActionFunctionParam(TypedDict, total=False):
    function_source: Required[Annotated[str, PropertyInfo(alias="functionSource")]]

    function_type: Required[
        Annotated[
            Literal["PRE_ACTION_EXECUTION", "PRE_FETCH_OPTIONS", "POST_FETCH_OPTIONS", "POST_ACTION_EXECUTION"],
            PropertyInfo(alias="functionType"),
        ]
    ]

    id: str
