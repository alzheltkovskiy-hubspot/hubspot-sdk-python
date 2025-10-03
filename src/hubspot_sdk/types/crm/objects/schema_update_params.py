# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ...crm_object_type_definition_labels_param import CRMObjectTypeDefinitionLabelsParam

__all__ = ["SchemaUpdateParams"]


class SchemaUpdateParams(TypedDict, total=False):
    clear_description: Annotated[bool, PropertyInfo(alias="clearDescription")]

    labels: CRMObjectTypeDefinitionLabelsParam

    primary_display_property: Annotated[str, PropertyInfo(alias="primaryDisplayProperty")]

    required_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="requiredProperties")]

    restorable: bool

    searchable_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="searchableProperties")]

    secondary_display_properties: Annotated[SequenceNotStr[str], PropertyInfo(alias="secondaryDisplayProperties")]
