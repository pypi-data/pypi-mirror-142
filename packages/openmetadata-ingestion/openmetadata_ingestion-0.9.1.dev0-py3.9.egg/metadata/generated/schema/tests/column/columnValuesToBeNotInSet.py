# generated by datamodel-codegen:
#   filename:  schema/tests/column/columnValuesToBeNotInSet.json
#   timestamp: 2022-03-10T19:52:22+00:00

from __future__ import annotations

from typing import List, Union

from pydantic import BaseModel, Extra, Field


class ColumnValuesToBeNotInSet(BaseModel):
    class Config:
        extra = Extra.forbid

    forbiddenValues: List[Union[str, float]] = Field(
        ..., description='An Array of values.'
    )
