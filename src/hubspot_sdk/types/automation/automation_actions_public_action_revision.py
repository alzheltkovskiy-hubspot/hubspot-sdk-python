# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .automation_actions_public_action_definition import AutomationActionsPublicActionDefinition

__all__ = ["AutomationActionsPublicActionRevision"]


class AutomationActionsPublicActionRevision(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    definition: AutomationActionsPublicActionDefinition

    revision_id: str = FieldInfo(alias="revisionId")
