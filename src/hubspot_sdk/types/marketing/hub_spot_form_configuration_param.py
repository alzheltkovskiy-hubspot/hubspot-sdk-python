# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .lifecycle_stage_param import LifecycleStageParam
from .form_post_submit_action_param import FormPostSubmitActionParam

__all__ = ["HubSpotFormConfigurationParam"]


class HubSpotFormConfigurationParam(TypedDict, total=False):
    allow_link_to_reset_known_values: Required[Annotated[bool, PropertyInfo(alias="allowLinkToResetKnownValues")]]
    """Whether to add a reset link to the form.

    This removes any pre-populated content on the form and creates a new contact on
    submission.
    """

    archivable: Required[bool]
    """Whether the form can be archived."""

    cloneable: Required[bool]
    """Whether the form can be cloned."""

    create_new_contact_for_new_email: Required[Annotated[bool, PropertyInfo(alias="createNewContactForNewEmail")]]
    """
    Whether to create a new contact when a form is submitted with an email address
    that doesn’t match any in your existing contacts records.
    """

    editable: Required[bool]
    """Whether the form can be edited."""

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
    """The language of the form."""

    notify_contact_owner: Required[Annotated[bool, PropertyInfo(alias="notifyContactOwner")]]
    """
    Whether to send a notification email to the contact owner when a submission is
    received.
    """

    notify_recipients: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="notifyRecipients")]]
    """
    The list of user IDs to receive a notification email when a submission is
    received.
    """

    post_submit_action: Required[Annotated[FormPostSubmitActionParam, PropertyInfo(alias="postSubmitAction")]]
    """What should happen after the customer submits the form."""

    pre_populate_known_values: Required[Annotated[bool, PropertyInfo(alias="prePopulateKnownValues")]]
    """
    Whether contact fields should pre-populate with known information when a contact
    returns to your site.
    """

    recaptcha_enabled: Required[Annotated[bool, PropertyInfo(alias="recaptchaEnabled")]]
    """Whether CAPTCHA (spam prevention) is enabled."""

    lifecycle_stages: Annotated[Iterable[LifecycleStageParam], PropertyInfo(alias="lifecycleStages")]
