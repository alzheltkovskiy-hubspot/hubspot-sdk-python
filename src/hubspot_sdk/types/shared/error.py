# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .error_detail import ErrorDetail

__all__ = ["Error"]


class Error(BaseModel):
    category: str

    correlation_id: str = FieldInfo(alias="correlationId")

    message: str

    context: Optional[Dict[str, List[str]]] = None

    errors: Optional[List[ErrorDetail]] = None

    links: Optional[Dict[str, str]] = None

    sub_category: Optional[str] = FieldInfo(alias="subCategory", default=None)
