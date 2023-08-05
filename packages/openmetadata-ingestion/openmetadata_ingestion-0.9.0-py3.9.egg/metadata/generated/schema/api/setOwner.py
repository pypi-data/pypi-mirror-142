# generated by datamodel-codegen:
#   filename:  schema/api/setOwner.json
#   timestamp: 2022-03-10T18:46:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ..type import basic


class SetOwnershipRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    id: Optional[basic.Uuid] = Field(None, description='Id of the owner of the entity')
    type: Optional[str] = Field(
        None, description="Entity type of the owner typically either 'user' or 'team'"
    )
