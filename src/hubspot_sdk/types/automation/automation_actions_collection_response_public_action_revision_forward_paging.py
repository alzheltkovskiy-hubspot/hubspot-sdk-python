# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.forward_paging import ForwardPaging
from .automation_actions_public_action_revision import AutomationActionsPublicActionRevision

__all__ = ["AutomationActionsCollectionResponsePublicActionRevisionForwardPaging"]


class AutomationActionsCollectionResponsePublicActionRevisionForwardPaging(BaseModel):
    results: List[AutomationActionsPublicActionRevision]

    paging: Optional[ForwardPaging] = None
