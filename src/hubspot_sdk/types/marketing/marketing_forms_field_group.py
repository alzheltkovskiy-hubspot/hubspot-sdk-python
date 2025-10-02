# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MarketingFormsFieldGroup", "Field"]

Field: TypeAlias = Union[
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


class MarketingFormsFieldGroup(BaseModel):
    fields: List[Field]

    group_type: Literal["default_group", "progressive", "queued"] = FieldInfo(alias="groupType")

    rich_text_type: Literal["text", "image"] = FieldInfo(alias="richTextType")

    rich_text: Optional[str] = FieldInfo(alias="richText", default=None)


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
