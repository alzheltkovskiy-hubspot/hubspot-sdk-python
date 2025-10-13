# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..option_input_param import OptionInputParam

__all__ = ["ObjectTypePropertyCreateParam"]


class ObjectTypePropertyCreateParam(TypedDict, total=False):
    field_type: Required[Annotated[str, PropertyInfo(alias="fieldType")]]
    """Controls how the property appears in HubSpot."""

    label: Required[str]
    """A human-readable property label that will be shown in HubSpot."""

    name: Required[str]
    """
    The internal property name, which must be used when referencing the property
    from the API.
    """

    type: Required[Literal["string", "number", "date", "datetime", "enumeration", "bool"]]
    """The data type of the property."""

    description: str
    """A description of the property that will be shown as help text in HubSpot."""

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]
    """
    The order that this property should be displayed in the HubSpot UI relative to
    other properties for this object type. Properties are displayed in order
    starting with the lowest positive integer value. A value of -1 will cause the
    property to be displayed **after** any positive values.
    """

    form_field: Annotated[bool, PropertyInfo(alias="formField")]
    """Whether the property can be used in a HubSpot form."""

    group_name: Annotated[str, PropertyInfo(alias="groupName")]
    """The name of the group this property belongs to."""

    has_unique_value: Annotated[bool, PropertyInfo(alias="hasUniqueValue")]
    """Whether or not the property's value must be unique.

    Once set, this can't be changed.
    """

    hidden: bool

    number_display_hint: Annotated[
        Literal["unformatted", "formatted", "currency", "percentage", "duration", "probability"],
        PropertyInfo(alias="numberDisplayHint"),
    ]
    """Controls how numeric properties are formatted in the HubSpot UI"""

    options: Iterable[OptionInputParam]
    """A list of available options for the property.

    This field is only required for enumerated properties.
    """

    option_sort_strategy: Annotated[Literal["DISPLAY_ORDER", "ALPHABETICAL"], PropertyInfo(alias="optionSortStrategy")]
    """Controls how the property options will be sorted in the HubSpot UI."""

    referenced_object_type: Annotated[str, PropertyInfo(alias="referencedObjectType")]
    """Defines the options this property will return, e.g.

    OWNER would return name of users on the portal.
    """

    searchable_in_global_search: Annotated[bool, PropertyInfo(alias="searchableInGlobalSearch")]
    """
    Allow users to search for information entered to this field (limited to 3
    properties)
    """

    show_currency_symbol: Annotated[bool, PropertyInfo(alias="showCurrencySymbol")]
    """Whether the property will display the currency symbol in the HubSpot UI."""

    text_display_hint: Annotated[
        Literal[
            "unformatted_single_line",
            "multi_line",
            "email",
            "phone_number",
            "domain_name",
            "ip_address",
            "physical_address",
            "postal_code",
        ],
        PropertyInfo(alias="textDisplayHint"),
    ]
    """Controls how text properties are formatted in the HubSpot UI"""
