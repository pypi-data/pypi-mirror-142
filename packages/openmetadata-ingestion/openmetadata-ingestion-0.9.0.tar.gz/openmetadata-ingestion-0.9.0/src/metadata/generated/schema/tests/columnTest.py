# generated by datamodel-codegen:
#   filename:  schema/tests/columnTest.json
#   timestamp: 2022-03-10T18:46:10+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Extra, Field, constr

from ..type import basic, entityReference
from . import basic as basic_1
from .column import (
    columnValuesLengthsToBeBetween,
    columnValuesMissingCountToBeEqual,
    columnValuesToBeBetween,
    columnValuesToBeNotInSet,
    columnValuesToBeNotNull,
    columnValuesToBeUnique,
    columnValuesToMatchRegex,
)


class ColumnTestType(Enum):
    columnValuesToBeUnique = 'columnValuesToBeUnique'
    columnValuesToBeNotNull = 'columnValuesToBeNotNull'
    columnValuesToMatchRegex = 'columnValuesToMatchRegex'
    columnValuesToBeNotInSet = 'columnValuesToBeNotInSet'
    columnValuesToBeBetween = 'columnValuesToBeBetween'
    columnValuesMissingCountToBeEqual = 'columnValuesMissingCountToBeEqual'
    columnValueLengthsToBeBetween = 'columnValueLengthsToBeBetween'


class ColumnTestCase(BaseModel):
    class Config:
        extra = Extra.forbid

    config: Optional[
        Union[
            columnValuesToBeUnique.ColumnValuesToBeUnique,
            columnValuesToBeNotNull.ColumnValuesToBeNotNull,
            columnValuesToMatchRegex.ColumnValuesToMatchRegex,
            columnValuesToBeNotInSet.ColumnValuesToBeNotInSet,
            columnValuesToBeBetween.ColumnValuesToBeBetween,
            columnValuesMissingCountToBeEqual.ColumnValuesMissingCount,
            columnValuesLengthsToBeBetween.ColumnValueLengthsToBeBetween,
        ]
    ] = None
    columnTestType: Optional[ColumnTestType] = None


class ColumnTest(BaseModel):
    class Config:
        extra = Extra.forbid

    id: Optional[basic.Uuid] = Field(
        None, description='Unique identifier of this table instance.'
    )
    name: constr(min_length=1, max_length=128) = Field(
        ...,
        description='Name that identifies this test case. Name passed by client will be  overridden by  auto generating based on table/column name and test name',
    )
    description: Optional[str] = Field(None, description='Description of the testcase.')
    columnName: Optional[str] = Field(
        None, description='Name of the column in a table.'
    )
    testCase: ColumnTestCase
    executionFrequency: Optional[basic_1.TestCaseExecutionFrequency] = None
    results: Optional[List[basic_1.TestCaseResult]] = Field(
        None, description='List of results of the test case.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this Pipeline.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
