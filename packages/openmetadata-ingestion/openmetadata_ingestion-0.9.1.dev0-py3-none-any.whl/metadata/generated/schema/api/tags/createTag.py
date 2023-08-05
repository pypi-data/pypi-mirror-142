# generated by datamodel-codegen:
#   filename:  schema/api/tags/createTag.json
#   timestamp: 2022-03-10T19:52:22+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...entity.tags import tagCategory


class CreateTagRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: tagCategory.TagName
    description: str = Field(..., description='Unique name of the tag category')
    associatedTags: Optional[List[str]] = Field(
        None, description='Fully qualified names of tags associated with this tag'
    )
