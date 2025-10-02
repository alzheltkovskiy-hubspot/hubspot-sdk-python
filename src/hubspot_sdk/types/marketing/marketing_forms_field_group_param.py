# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MarketingFormsFieldGroupParam", "Field"]

Field: TypeAlias = Union[
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


class MarketingFormsFieldGroupParam(TypedDict, total=False):
    fields: Required[Iterable[Field]]

    group_type: Required[Annotated[Literal["default_group", "progressive", "queued"], PropertyInfo(alias="groupType")]]

    rich_text_type: Required[Annotated[Literal["text", "image"], PropertyInfo(alias="richTextType")]]

    rich_text: Annotated[str, PropertyInfo(alias="richText")]


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
