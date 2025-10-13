# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .form_definition_create_request_base_param import FormDefinitionCreateRequestBaseParam

__all__ = ["FormCreateParams"]


class FormCreateParams(TypedDict, total=False):
    form_definition_create_request_base: Required[
        Annotated[FormDefinitionCreateRequestBaseParam, PropertyInfo(alias="FormDefinitionCreateRequestBase")]
    ]
