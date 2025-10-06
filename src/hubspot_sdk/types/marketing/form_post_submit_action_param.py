# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FormPostSubmitActionParam"]


class FormPostSubmitActionParam(TypedDict, total=False):
    type: Required[Literal["thank_you", "redirect_url"]]

    value: Required[str]
