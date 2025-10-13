# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["NextPage"]


class NextPage(BaseModel):
    after: str
    """A paging cursor token for retrieving subsequent pages."""

    link: Optional[str] = None
    """A URL that can be used to retrieve the next page results."""
