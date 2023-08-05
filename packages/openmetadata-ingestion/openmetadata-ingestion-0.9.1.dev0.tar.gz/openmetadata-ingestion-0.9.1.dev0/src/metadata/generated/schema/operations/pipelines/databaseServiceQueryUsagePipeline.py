# generated by datamodel-codegen:
#   filename:  schema/operations/pipelines/databaseServiceQueryUsagePipeline.json
#   timestamp: 2022-03-10T19:52:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class DatabaseServiceQueryUsagePipeline(BaseModel):
    class Config:
        extra = Extra.forbid

    queryLogDuration: Optional[int] = Field(
        '1',
        description='Configuration to tune how far we want to look back in query logs to process usage data.',
    )
    stageFileLocation: Optional[str] = Field(
        '/tmp/query_log',
        description='Temporary file name to store the query logs before processing. Absolute file path required.',
    )
