# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..crm_objects_simple_public_object_batch_input_param import CRMObjectsSimplePublicObjectBatchInputParam

__all__ = ["ContactUpdateParams"]


class ContactUpdateParams(TypedDict, total=False):
    inputs: Required[Iterable[CRMObjectsSimplePublicObjectBatchInputParam]]
