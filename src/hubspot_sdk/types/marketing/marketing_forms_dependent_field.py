# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import TypeAlias, TypeAliasType

from pydantic import Field as FieldInfo

from ..._compat import PYDANTIC_V1
from ..._models import BaseModel
from .marketing_forms_dependent_field_filter import MarketingFormsDependentFieldFilter

__all__ = ["MarketingFormsDependentField", "DependentField"]

if TYPE_CHECKING or not PYDANTIC_V1:
    DependentField = TypeAliasType(
        "DependentField",
        Union[
            "MarketingFormsEmailField",
            "MarketingFormsPhoneField",
            "MarketingFormsMobilePhoneField",
            "MarketingFormsSingleLineTextField",
            "MarketingFormsMultiLineTextField",
            "MarketingFormsNumberField",
            "MarketingFormsSingleCheckboxField",
            "MarketingFormsMultipleCheckboxesField",
            "MarketingFormsDropdownField",
            "MarketingFormsRadioField",
            "MarketingFormsDatepickerField",
            "MarketingFormsFileField",
            "MarketingFormsPaymentLinkRadioField",
        ],
    )
else:
    DependentField: TypeAlias = Union[
        "MarketingFormsEmailField",
        "MarketingFormsPhoneField",
        "MarketingFormsMobilePhoneField",
        "MarketingFormsSingleLineTextField",
        "MarketingFormsMultiLineTextField",
        "MarketingFormsNumberField",
        "MarketingFormsSingleCheckboxField",
        "MarketingFormsMultipleCheckboxesField",
        "MarketingFormsDropdownField",
        "MarketingFormsRadioField",
        "MarketingFormsDatepickerField",
        "MarketingFormsFileField",
        "MarketingFormsPaymentLinkRadioField",
    ]


class MarketingFormsDependentField(BaseModel):
    dependent_condition: MarketingFormsDependentFieldFilter = FieldInfo(alias="dependentCondition")

    dependent_field: DependentField = FieldInfo(alias="dependentField")


from .marketing_forms_file_field import MarketingFormsFileField
from .marketing_forms_email_field import MarketingFormsEmailField
from .marketing_forms_phone_field import MarketingFormsPhoneField
from .marketing_forms_radio_field import MarketingFormsRadioField
from .marketing_forms_number_field import MarketingFormsNumberField
from .marketing_forms_dropdown_field import MarketingFormsDropdownField
from .marketing_forms_datepicker_field import MarketingFormsDatepickerField
from .marketing_forms_mobile_phone_field import MarketingFormsMobilePhoneField
from .marketing_forms_multi_line_text_field import MarketingFormsMultiLineTextField
from .marketing_forms_single_checkbox_field import MarketingFormsSingleCheckboxField
from .marketing_forms_single_line_text_field import MarketingFormsSingleLineTextField
from .marketing_forms_payment_link_radio_field import MarketingFormsPaymentLinkRadioField
from .marketing_forms_multiple_checkboxes_field import MarketingFormsMultipleCheckboxesField
