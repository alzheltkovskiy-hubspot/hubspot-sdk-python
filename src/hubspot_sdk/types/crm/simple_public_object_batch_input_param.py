# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SimplePublicObjectBatchInputParam"]


class SimplePublicObjectBatchInputParam(TypedDict, total=False):
    id: Required[str]
    """The ID to be updated.

    This can be the object ID, or the unique property value of the `idProperty`
    property.
    """

    properties: Required[Dict[str, str]]
    """The company property values to set."""

    id_property: Annotated[str, PropertyInfo(alias="idProperty")]
    """The name of a property whose values are unique for this object"""

    object_write_trace_id: Annotated[str, PropertyInfo(alias="objectWriteTraceId")]
    """
    In each input object, set this field to a unique ID value to enable more
    granular debugging for error responses. Learn more about
    [multi-status errors](https://developers.hubspot.com/docs/reference/api/other-resources/error-handling#multi-status-errors).
    """
