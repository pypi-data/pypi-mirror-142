# generated by datamodel-codegen:
#   filename:  schema/api/data/createGlossaryTerm.json
#   timestamp: 2022-03-10T18:46:10+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ...entity.data import glossaryTerm
from ...type import entityReference, tagLabel


class CreateGlossaryTermRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    glossary: entityReference.EntityReference = Field(
        ..., description='Reference to the glossary that this term is part of.'
    )
    parent: Optional[entityReference.EntityReference] = Field(
        None,
        description='Reference to the parent glossary term. When null, the term is at the root of the glossary.',
    )
    name: glossaryTerm.Name = Field(
        ..., description='Preferred name for the glossary term.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this glossary.'
    )
    description: Optional[str] = Field(
        None, description='Description of the glossary term.'
    )
    synonyms: Optional[List[glossaryTerm.Name]] = Field(
        None,
        description='Alternate names that are synonyms or near-synonyms for the glossary term.',
    )
    relatedTerms: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Other glossary terms that are related to this glossary term.'
    )
    references: Optional[List[glossaryTerm.TermReference]] = Field(
        None, description='Link to a reference from an external glossary.'
    )
    reviewers: Optional[entityReference.EntityReferenceList] = Field(
        None, description='User names of the reviewers for this glossary.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this glossary term.'
    )
