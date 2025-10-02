# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .marketing_forms_enumerated_field_option_param import MarketingFormsEnumeratedFieldOptionParam

__all__ = ["MarketingFormsPaymentLinkRadioFieldParam"]


class MarketingFormsPaymentLinkRadioFieldParam(TypedDict, total=False):
    default_values: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="defaultValues")]]

    dependent_fields: Required[
        Annotated[Iterable["MarketingFormsDependentFieldParam"], PropertyInfo(alias="dependentFields")]
    ]

    field_type: Required[Annotated[Literal["payment_link_radio"], PropertyInfo(alias="fieldType")]]

    hidden: Required[bool]

    label: Required[str]

    name: Required[str]

    object_type_id: Required[Annotated[str, PropertyInfo(alias="objectTypeId")]]

    options: Required[Iterable[MarketingFormsEnumeratedFieldOptionParam]]

    required: Required[bool]


from .marketing_forms_dependent_field_param import MarketingFormsDependentFieldParam
