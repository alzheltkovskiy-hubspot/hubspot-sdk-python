# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .files_file import FilesFile
from .files_folder import FilesFolder

__all__ = ["FilesFileStat"]


class FilesFileStat(BaseModel):
    file: Optional[FilesFile] = None

    folder: Optional[FilesFolder] = None
