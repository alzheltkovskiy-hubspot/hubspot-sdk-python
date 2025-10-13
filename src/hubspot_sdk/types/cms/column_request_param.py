# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..option_param import OptionParam

__all__ = ["ColumnRequestParam"]


class ColumnRequestParam(TypedDict, total=False):
    id: Required[int]

    label: Required[str]

    name: Required[str]

    options: Required[Iterable[OptionParam]]

    type: Required[
        Literal[
            "NULL",
            "TEXT",
            "NUMBER",
            "URL",
            "IMAGE",
            "SELECT",
            "MULTISELECT",
            "BOOLEAN",
            "LOCATION",
            "DATE",
            "DATETIME",
            "CURRENCY",
            "RICHTEXT",
            "FOREIGN_ID",
            "VIDEO",
            "CTA",
            "FILE",
            "JSON",
            "COMPOSITE",
            "CODE",
            "HUBSPOT_VIDEO",
            "EMBED",
        ]
    ]

    foreign_column_id: Annotated[int, PropertyInfo(alias="foreignColumnId")]

    foreign_table_id: Annotated[int, PropertyInfo(alias="foreignTableId")]

    max_number_of_characters: Annotated[int, PropertyInfo(alias="maxNumberOfCharacters")]

    max_number_of_options: Annotated[int, PropertyInfo(alias="maxNumberOfOptions")]
