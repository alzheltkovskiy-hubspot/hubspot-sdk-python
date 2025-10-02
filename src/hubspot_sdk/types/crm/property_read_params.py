# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .crm_properties_property_name_param import CRMPropertiesPropertyNameParam

__all__ = ["PropertyReadParams"]


class PropertyReadParams(TypedDict, total=False):
    archived: Required[bool]

    inputs: Required[Iterable[CRMPropertiesPropertyNameParam]]

    data_sensitivity: Annotated[
        Literal["non_sensitive", "sensitive", "highly_sensitive"], PropertyInfo(alias="dataSensitivity")
    ]
