# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ErrorDetail"]


class ErrorDetail(BaseModel):
    message: str

    code: Optional[str] = None

    context: Optional[Dict[str, List[str]]] = None

    in_: Optional[str] = FieldInfo(alias="in", default=None)

    sub_category: Optional[str] = FieldInfo(alias="subCategory", default=None)
