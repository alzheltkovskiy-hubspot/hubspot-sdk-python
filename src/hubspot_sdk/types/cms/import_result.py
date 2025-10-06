# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.error import Error

__all__ = ["ImportResult"]


class ImportResult(BaseModel):
    duplicate_rows: int = FieldInfo(alias="duplicateRows")

    errors: List[Error]

    row_limit_exceeded: bool = FieldInfo(alias="rowLimitExceeded")

    rows_imported: int = FieldInfo(alias="rowsImported")
