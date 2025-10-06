# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FileFieldParam"]


class FileFieldParam(TypedDict, total=False):
    allow_multiple_files: Required[Annotated[bool, PropertyInfo(alias="allowMultipleFiles")]]

    dependent_fields: Required[Annotated[Iterable["DependentFieldParam"], PropertyInfo(alias="dependentFields")]]

    field_type: Required[Annotated[Literal["file"], PropertyInfo(alias="fieldType")]]

    hidden: Required[bool]

    label: Required[str]

    name: Required[str]

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    required: Required[bool]

    default_value: Annotated[str, PropertyInfo(alias="defaultValue")]

    placeholder: str


from .dependent_field_param import DependentFieldParam
