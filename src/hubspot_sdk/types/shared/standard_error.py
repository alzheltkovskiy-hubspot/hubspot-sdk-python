# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .error_detail import ErrorDetail

__all__ = ["StandardError"]


class StandardError(BaseModel):
    category: str

    context: Dict[str, List[str]]

    errors: List[ErrorDetail]

    links: Dict[str, str]

    message: str

    status: str

    id: Optional[str] = None

    sub_category: Optional[object] = FieldInfo(alias="subCategory", default=None)
