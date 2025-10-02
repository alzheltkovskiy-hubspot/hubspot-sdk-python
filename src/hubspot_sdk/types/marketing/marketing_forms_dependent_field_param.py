# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict, TypeAliasType

from ..._utils import PropertyInfo
from ..._compat import PYDANTIC_V1
from .marketing_forms_dependent_field_filter_param import MarketingFormsDependentFieldFilterParam

__all__ = ["MarketingFormsDependentFieldParam", "DependentField"]

if TYPE_CHECKING or not PYDANTIC_V1:
    DependentField = TypeAliasType(
        "DependentField",
        Union[
            "MarketingFormsEmailFieldParam",
            "MarketingFormsPhoneFieldParam",
            "MarketingFormsMobilePhoneFieldParam",
            "MarketingFormsSingleLineTextFieldParam",
            "MarketingFormsMultiLineTextFieldParam",
            "MarketingFormsNumberFieldParam",
            "MarketingFormsSingleCheckboxFieldParam",
            "MarketingFormsMultipleCheckboxesFieldParam",
            "MarketingFormsDropdownFieldParam",
            "MarketingFormsRadioFieldParam",
            "MarketingFormsDatepickerFieldParam",
            "MarketingFormsFileFieldParam",
            "MarketingFormsPaymentLinkRadioFieldParam",
        ],
    )
else:
    DependentField: TypeAlias = Union[
        "MarketingFormsEmailFieldParam",
        "MarketingFormsPhoneFieldParam",
        "MarketingFormsMobilePhoneFieldParam",
        "MarketingFormsSingleLineTextFieldParam",
        "MarketingFormsMultiLineTextFieldParam",
        "MarketingFormsNumberFieldParam",
        "MarketingFormsSingleCheckboxFieldParam",
        "MarketingFormsMultipleCheckboxesFieldParam",
        "MarketingFormsDropdownFieldParam",
        "MarketingFormsRadioFieldParam",
        "MarketingFormsDatepickerFieldParam",
        "MarketingFormsFileFieldParam",
        "MarketingFormsPaymentLinkRadioFieldParam",
    ]


class MarketingFormsDependentFieldParam(TypedDict, total=False):
    dependent_condition: Required[
        Annotated[MarketingFormsDependentFieldFilterParam, PropertyInfo(alias="dependentCondition")]
    ]

    dependent_field: Required[Annotated[DependentField, PropertyInfo(alias="dependentField")]]


from .marketing_forms_file_field_param import MarketingFormsFileFieldParam
from .marketing_forms_email_field_param import MarketingFormsEmailFieldParam
from .marketing_forms_phone_field_param import MarketingFormsPhoneFieldParam
from .marketing_forms_radio_field_param import MarketingFormsRadioFieldParam
from .marketing_forms_number_field_param import MarketingFormsNumberFieldParam
from .marketing_forms_dropdown_field_param import MarketingFormsDropdownFieldParam
from .marketing_forms_datepicker_field_param import MarketingFormsDatepickerFieldParam
from .marketing_forms_mobile_phone_field_param import MarketingFormsMobilePhoneFieldParam
from .marketing_forms_multi_line_text_field_param import MarketingFormsMultiLineTextFieldParam
from .marketing_forms_single_checkbox_field_param import MarketingFormsSingleCheckboxFieldParam
from .marketing_forms_single_line_text_field_param import MarketingFormsSingleLineTextFieldParam
from .marketing_forms_payment_link_radio_field_param import MarketingFormsPaymentLinkRadioFieldParam
from .marketing_forms_multiple_checkboxes_field_param import MarketingFormsMultipleCheckboxesFieldParam
