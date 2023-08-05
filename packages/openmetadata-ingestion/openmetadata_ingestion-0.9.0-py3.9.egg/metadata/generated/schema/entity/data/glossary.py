# generated by datamodel-codegen:
#   filename:  schema/entity/data/glossary.json
#   timestamp: 2022-03-10T18:46:10+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field, constr

from ...type import basic, entityHistory, entityReference, tagLabel


class Name(BaseModel):
    __root__: constr(min_length=1, max_length=128) = Field(
        ..., description='Name that identifies a glossary term.'
    )


class Glossary(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(..., description='Unique identifier of a glossary instance.')
    name: Name = Field(..., description='Preferred name for the glossary term.')
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this glossary.'
    )
    description: Optional[str] = Field(None, description='Description of the glossary.')
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    reviewers: Optional[List[entityReference.EntityReference]] = Field(
        None, description='User references of the reviewers for this glossary.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this glossary.'
    )
    usageCount: Optional[int] = Field(
        None, description='Count of how many times terms from this glossary are used.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this glossary.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
