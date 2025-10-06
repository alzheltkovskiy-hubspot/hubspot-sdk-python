# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .public_action_definition import PublicActionDefinition

__all__ = ["PublicActionRevision"]


class PublicActionRevision(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    definition: PublicActionDefinition

    revision_id: str = FieldInfo(alias="revisionId")
