# generated by datamodel-codegen:
#   filename:  schema/api/tests/createColumnTest.json
#   timestamp: 2022-03-10T18:46:10+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...tests import basic, columnTest
from ...type import basic as basic_1
from ...type import entityReference


class CreateColumnTestRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    description: Optional[str] = Field(None, description='Description of the testcase.')
    columnName: str = Field(..., description='Name of the column in a table.')
    testCase: columnTest.ColumnTestCase
    executionFrequency: Optional[basic.TestCaseExecutionFrequency] = None
    result: Optional[basic.TestCaseResult] = None
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this Pipeline.'
    )
    updatedAt: Optional[basic_1.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
