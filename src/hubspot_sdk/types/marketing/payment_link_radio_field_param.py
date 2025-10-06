# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .enumerated_field_option_param import EnumeratedFieldOptionParam

__all__ = ["PaymentLinkRadioFieldParam"]


class PaymentLinkRadioFieldParam(TypedDict, total=False):
    default_values: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="defaultValues")]]

    dependent_fields: Required[Annotated[Iterable["DependentFieldParam"], PropertyInfo(alias="dependentFields")]]

    field_type: Required[Annotated[Literal["payment_link_radio"], PropertyInfo(alias="fieldType")]]

    hidden: Required[bool]

    label: Required[str]

    name: Required[str]

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    options: Required[Iterable[EnumeratedFieldOptionParam]]

    required: Required[bool]


from .dependent_field_param import DependentFieldParam
