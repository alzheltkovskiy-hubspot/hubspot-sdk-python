# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..column_request_param import ColumnRequestParam

__all__ = ["TableUpdateDraftParams"]


class TableUpdateDraftParams(TypedDict, total=False):
    label: Required[str]

    name: Required[str]

    archived: bool

    include_foreign_ids: Annotated[bool, PropertyInfo(alias="includeForeignIds")]

    is_get_localized_schema: Annotated[bool, PropertyInfo(alias="isGetLocalizedSchema")]

    allow_child_tables: Annotated[bool, PropertyInfo(alias="allowChildTables")]

    allow_public_api_access: Annotated[bool, PropertyInfo(alias="allowPublicApiAccess")]

    columns: Iterable[ColumnRequestParam]

    dynamic_meta_tags: Annotated[Dict[str, int], PropertyInfo(alias="dynamicMetaTags")]

    enable_child_table_pages: Annotated[bool, PropertyInfo(alias="enableChildTablePages")]

    use_for_pages: Annotated[bool, PropertyInfo(alias="useForPages")]
