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
    """Whether to add a reset link to the form.

    This removes any pre-populated content on the form and creates a new contact on
    submission.
    """

    archivable: bool
    """Whether the form can be archived."""

    cloneable: bool
    """Whether the form can be cloned."""

    create_new_contact_for_new_email: bool = FieldInfo(alias="createNewContactForNewEmail")
    """
    Whether to create a new contact when a form is submitted with an email address
    that doesn’t match any in your existing contacts records.
    """

    editable: bool
    """Whether the form can be edited."""

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
    """The language of the form."""

    notify_contact_owner: bool = FieldInfo(alias="notifyContactOwner")
    """
    Whether to send a notification email to the contact owner when a submission is
    received.
    """

    notify_recipients: List[str] = FieldInfo(alias="notifyRecipients")
    """
    The list of user IDs to receive a notification email when a submission is
    received.
    """

    post_submit_action: FormPostSubmitAction = FieldInfo(alias="postSubmitAction")
    """What should happen after the customer submits the form."""

    pre_populate_known_values: bool = FieldInfo(alias="prePopulateKnownValues")
    """
    Whether contact fields should pre-populate with known information when a contact
    returns to your site.
    """

    recaptcha_enabled: bool = FieldInfo(alias="recaptchaEnabled")
    """Whether CAPTCHA (spam prevention) is enabled."""

    lifecycle_stages: Optional[List[LifecycleStage]] = FieldInfo(alias="lifecycleStages", default=None)
