# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..option_input_param import OptionInputParam

__all__ = ["ObjectTypePropertyCreateParam"]


class ObjectTypePropertyCreateParam(TypedDict, total=False):
    field_type: Required[Annotated[str, PropertyInfo(alias="fieldType")]]

    label: Required[str]

    name: Required[str]

    type: Required[Literal["string", "number", "date", "datetime", "enumeration", "bool"]]

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]

    form_field: Annotated[bool, PropertyInfo(alias="formField")]

    group_name: Annotated[str, PropertyInfo(alias="groupName")]

    has_unique_value: Annotated[bool, PropertyInfo(alias="hasUniqueValue")]

    hidden: bool

    number_display_hint: Annotated[
        Literal["unformatted", "formatted", "currency", "percentage", "duration", "probability"],
        PropertyInfo(alias="numberDisplayHint"),
    ]

    options: Iterable[OptionInputParam]

    option_sort_strategy: Annotated[Literal["DISPLAY_ORDER", "ALPHABETICAL"], PropertyInfo(alias="optionSortStrategy")]

    referenced_object_type: Annotated[str, PropertyInfo(alias="referencedObjectType")]

    searchable_in_global_search: Annotated[bool, PropertyInfo(alias="searchableInGlobalSearch")]

    show_currency_symbol: Annotated[bool, PropertyInfo(alias="showCurrencySymbol")]

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
