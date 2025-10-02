# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .files_file import FilesFile
from .shared.paging import Paging

__all__ = ["FilesCollectionResponseFile"]


class FilesCollectionResponseFile(BaseModel):
    results: List[FilesFile]

    paging: Optional[Paging] = None
