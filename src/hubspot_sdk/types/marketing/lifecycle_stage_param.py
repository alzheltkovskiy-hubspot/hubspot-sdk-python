# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["LifecycleStageParam"]


class LifecycleStageParam(TypedDict, total=False):
    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    value: Required[str]
