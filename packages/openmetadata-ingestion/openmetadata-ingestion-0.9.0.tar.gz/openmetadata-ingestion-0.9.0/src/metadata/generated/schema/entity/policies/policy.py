# generated by datamodel-codegen:
#   filename:  schema/entity/policies/policy.json
#   timestamp: 2022-03-10T18:46:10+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, Extra, Field, constr

from ...type import basic, entityHistory, entityReference
from .accessControl import rule
from .lifecycle import rule as rule_1


class PolicyName(BaseModel):
    __root__: constr(min_length=1, max_length=128) = Field(
        ..., description='Name that identifies this Policy.'
    )


class PolicyType(Enum):
    AccessControl = 'AccessControl'
    Lifecycle = 'Lifecycle'


class Rules(BaseModel):
    __root__: List[Union[rule.AccessControlRule, rule_1.LifecycleRule]] = Field(
        ..., description='A set of rules associated with the Policy.'
    )


class Policy(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies this Policy.'
    )
    name: PolicyName = Field(
        ..., description='Name that uniquely identifies this Policy.'
    )
    fullyQualifiedName: Optional[PolicyName] = Field(
        None, description='Name that uniquely identifies a Policy.'
    )
    displayName: Optional[str] = Field(None, description='Title for this Policy.')
    description: Optional[str] = Field(
        None,
        description='A short description of the Policy, comprehensible to regular users.',
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this Policy.'
    )
    policyUrl: Optional[AnyUrl] = Field(
        None, description='Link to a well documented definition of this Policy.'
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    policyType: PolicyType
    enabled: Optional[bool] = Field(True, description='Is the policy enabled.')
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the Policy.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the Policy in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that led to this version of the Policy.'
    )
    rules: Optional[Rules] = None
    location: Optional[entityReference.EntityReference] = None
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
