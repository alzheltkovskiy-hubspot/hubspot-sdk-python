# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CallingRegisterURLFormatParams"]


class CallingRegisterURLFormatParams(TypedDict, total=False):
    url_to_retrieve_authed_recording: Required[Annotated[str, PropertyInfo(alias="urlToRetrieveAuthedRecording")]]
