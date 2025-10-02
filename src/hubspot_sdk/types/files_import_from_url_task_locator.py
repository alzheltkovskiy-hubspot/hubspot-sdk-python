# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["FilesImportFromURLTaskLocator"]


class FilesImportFromURLTaskLocator(BaseModel):
    id: str

    links: Dict[str, str]
