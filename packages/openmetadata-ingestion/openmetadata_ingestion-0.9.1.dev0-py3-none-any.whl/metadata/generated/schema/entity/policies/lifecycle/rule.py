# generated by datamodel-codegen:
#   filename:  schema/entity/policies/lifecycle/rule.json
#   timestamp: 2022-03-10T19:52:22+00:00

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import BaseModel, Extra, Field

from .. import filters
from . import deleteAction, moveAction


class LifecycleRule(BaseModel):
    class Config:
        extra = Extra.forbid

    name: Optional[str] = Field(None, description='Name that identifies this Rule.')
    prefixFilter: Optional[filters.Prefix] = None
    regexFilter: Optional[filters.Regex] = None
    tagsFilter: Optional[filters.Tags] = None
    actions: List[
        Union[deleteAction.LifecycleDeleteAction, moveAction.LifecycleMoveAction]
    ] = Field(..., description='A set of actions to take on the entities.', min_items=1)
    enabled: Optional[bool] = Field(True, description='Is the rule enabled.')
