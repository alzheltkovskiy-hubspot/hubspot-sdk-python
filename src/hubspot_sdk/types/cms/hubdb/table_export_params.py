# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TableExportParams"]


class TableExportParams(TypedDict, total=False):
    format: str
    """The file format to export. Possible values include `CSV`, `XLSX`, and `XLS`."""
