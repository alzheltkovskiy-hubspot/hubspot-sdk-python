# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CRMObjectsSimplePublicObjectBatchInputParam"]


class CRMObjectsSimplePublicObjectBatchInputParam(TypedDict, total=False):
    id: Required[str]

    properties: Required[Dict[str, str]]

    id_property: Annotated[str, PropertyInfo(alias="idProperty")]

    object_write_trace_id: Annotated[str, PropertyInfo(alias="objectWriteTraceId")]
