# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from ..public_associations_for_object_param import PublicAssociationsForObjectParam

__all__ = ["DealCreateParams"]


class DealCreateParams(TypedDict, total=False):
    properties: Required[Dict[str, str]]
    """The company property values to set."""

    associations: Iterable[PublicAssociationsForObjectParam]
