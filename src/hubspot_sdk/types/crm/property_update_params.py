# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .option_input_param import OptionInputParam

__all__ = ["PropertyUpdateParams"]


class PropertyUpdateParams(TypedDict, total=False):
    object_type: Required[Annotated[str, PropertyInfo(alias="objectType")]]

    calculation_formula: Annotated[str, PropertyInfo(alias="calculationFormula")]

    display_order: Annotated[int, PropertyInfo(alias="displayOrder")]

    field_type: Annotated[
        Literal[
            "booleancheckbox",
            "calculation_equation",
            "checkbox",
            "date",
            "file",
            "html",
            "number",
            "phonenumber",
            "radio",
            "select",
            "text",
            "textarea",
        ],
        PropertyInfo(alias="fieldType"),
    ]

    form_field: Annotated[bool, PropertyInfo(alias="formField")]

    group_name: Annotated[str, PropertyInfo(alias="groupName")]

    hidden: bool

    label: str

    options: Iterable[OptionInputParam]

    type: Literal["bool", "date", "datetime", "enumeration", "number", "phone_number", "string"]
