# generated by datamodel-codegen:
#   filename:  schema/entity/services/storageService.json
#   timestamp: 2022-03-10T18:46:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field, constr

from ...type import basic, entityHistory, entityReference, storage


class StorageService(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier of this storage service instance.'
    )
    name: constr(regex=r'^[^.]*$', min_length=1, max_length=128) = Field(
        ..., description='Name that identifies this storage service.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this storage service.'
    )
    serviceType: storage.StorageServiceType = Field(
        ..., description='Type of storage service such as S3, GCS, HDFS...'
    )
    description: Optional[str] = Field(
        None, description='Description of a storage service instance.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: basic.Href = Field(
        ..., description='Link to the resource corresponding to this storage service.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this storage service.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
