# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from ..crm_objects_public_associations_for_object_param import CRMObjectsPublicAssociationsForObjectParam

__all__ = ["CompanyCreateParams"]


class CompanyCreateParams(TypedDict, total=False):
    properties: Required[Dict[str, str]]

    associations: Iterable[CRMObjectsPublicAssociationsForObjectParam]
