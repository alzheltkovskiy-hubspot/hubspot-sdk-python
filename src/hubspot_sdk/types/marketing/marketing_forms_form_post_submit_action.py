# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MarketingFormsFormPostSubmitAction"]


class MarketingFormsFormPostSubmitAction(BaseModel):
    type: Literal["thank_you", "redirect_url"]

    value: str
