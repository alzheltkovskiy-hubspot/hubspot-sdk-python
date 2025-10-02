# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .marketing_forms_lifecycle_stage_param import MarketingFormsLifecycleStageParam
from .marketing_forms_form_post_submit_action_param import MarketingFormsFormPostSubmitActionParam

__all__ = ["MarketingFormsHubSpotFormConfigurationParam"]


class MarketingFormsHubSpotFormConfigurationParam(TypedDict, total=False):
    allow_link_to_reset_known_values: Required[Annotated[bool, PropertyInfo(alias="allowLinkToResetKnownValues")]]

    archivable: Required[bool]

    cloneable: Required[bool]

    create_new_contact_for_new_email: Required[Annotated[bool, PropertyInfo(alias="createNewContactForNewEmail")]]

    editable: Required[bool]

    language: Required[
        Literal[
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
    ]

    notify_contact_owner: Required[Annotated[bool, PropertyInfo(alias="notifyContactOwner")]]

    notify_recipients: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="notifyRecipients")]]

    post_submit_action: Required[
        Annotated[MarketingFormsFormPostSubmitActionParam, PropertyInfo(alias="postSubmitAction")]
    ]

    pre_populate_known_values: Required[Annotated[bool, PropertyInfo(alias="prePopulateKnownValues")]]

    recaptcha_enabled: Required[Annotated[bool, PropertyInfo(alias="recaptchaEnabled")]]

    lifecycle_stages: Annotated[Iterable[MarketingFormsLifecycleStageParam], PropertyInfo(alias="lifecycleStages")]
