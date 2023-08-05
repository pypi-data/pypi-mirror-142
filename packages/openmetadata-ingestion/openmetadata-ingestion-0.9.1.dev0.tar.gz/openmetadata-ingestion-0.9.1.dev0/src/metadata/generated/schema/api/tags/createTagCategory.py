# generated by datamodel-codegen:
#   filename:  schema/api/tags/createTagCategory.json
#   timestamp: 2022-03-10T19:52:22+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field

from ...entity.tags import tagCategory


class CreateTagCategoryRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: tagCategory.TagName
    description: str = Field(..., description='Description of the tag category')
    categoryType: tagCategory.TagCategoryType
