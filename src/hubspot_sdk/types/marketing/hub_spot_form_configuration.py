# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .lifecycle_stage import LifecycleStage
from .form_post_submit_action import FormPostSubmitAction

__all__ = ["HubSpotFormConfiguration"]


class HubSpotFormConfiguration(BaseModel):
    allow_link_to_reset_known_values: bool = FieldInfo(alias="allowLinkToResetKnownValues")

    archivable: bool

    cloneable: bool

    create_new_contact_for_new_email: bool = FieldInfo(alias="createNewContactForNewEmail")

    editable: bool

    language: Literal[
        "af",
        "ar-eg",
        "bg",
        "bn",
        "ca-es",
        "cs",
        "da",
        "de",
        "el",
        "en",
        "es",
        "es-mx",
        "fi",
        "fr",
        "fr-ca",
        "he-il",
        "hr",
        "hu",
        "id",
        "it",
        "ja",
        "ko",
        "lt",
        "ms",
        "nl",
        "no-no",
        "pl",
        "pt",
        "pt-br",
        "ro",
        "ru",
        "sk",
        "sl",
        "sv",
        "th",
        "tl",
        "tr",
        "uk",
        "vi",
        "zh-cn",
        "zh-hk",
        "zh-tw",
    ]

    notify_contact_owner: bool = FieldInfo(alias="notifyContactOwner")

    notify_recipients: List[str] = FieldInfo(alias="notifyRecipients")

    post_submit_action: FormPostSubmitAction = FieldInfo(alias="postSubmitAction")

    pre_populate_known_values: bool = FieldInfo(alias="prePopulateKnownValues")

    recaptcha_enabled: bool = FieldInfo(alias="recaptchaEnabled")

    lifecycle_stages: Optional[List[LifecycleStage]] = FieldInfo(alias="lifecycleStages", default=None)
