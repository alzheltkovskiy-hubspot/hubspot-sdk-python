# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ...crm_object_type_property_create_param import CRMObjectTypePropertyCreateParam
from ...crm_object_type_definition_labels_param import CRMObjectTypeDefinitionLabelsParam

__all__ = ["SchemaCreateParams"]


class SchemaCreateParams(TypedDict, total=False):
    associated_objects: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="associatedObjects")]]

    labels: Required[CRMObjectTypeDefinitionLabelsParam]

    name: Required[str]

    properties: Required[Iterable[CRMObjectTypePropertyCreateParam]]

    required_properties: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="requiredProperties")]]

    primary_display_property: Annotated[str, PropertyInfo(alias="primaryDisplayProperty")]

    searchable_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="searchableProperties")]

    secondary_display_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="secondaryDisplayProperties")]
