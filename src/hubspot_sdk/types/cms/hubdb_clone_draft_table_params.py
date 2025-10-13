# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HubdbCloneDraftTableParams"]


class HubdbCloneDraftTableParams(TypedDict, total=False):
    copy_rows: Required[Annotated[bool, PropertyInfo(alias="copyRows")]]

    is_hubspot_defined: Required[Annotated[bool, PropertyInfo(alias="isHubspotDefined")]]

    new_label: Annotated[str, PropertyInfo(alias="newLabel")]

    new_name: Annotated[str, PropertyInfo(alias="newName")]
