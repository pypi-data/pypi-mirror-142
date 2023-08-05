# generated by datamodel-codegen:
#   filename:  schema/api/services/createDashboardService.json
#   timestamp: 2022-03-10T19:52:22+00:00

from __future__ import annotations

from typing import Optional

from pydantic import AnyUrl, BaseModel, Extra, Field, constr

from ...entity.services import dashboardService
from ...type import entityReference, schedule


class CreateDashboardServiceRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    name: constr(regex=r'^[^.]*$', min_length=1, max_length=128) = Field(
        ..., description='Name that identifies the this entity instance uniquely'
    )
    description: Optional[str] = Field(
        None, description='Description of dashboard service entity.'
    )
    serviceType: dashboardService.DashboardServiceType
    dashboardUrl: AnyUrl = Field(..., description='Dashboard Service URL')
    username: Optional[str] = Field(
        None, description='Username to log-into Dashboard Service'
    )
    password: Optional[str] = Field(
        None, description='Password to log-into Dashboard Service'
    )
    ingestionSchedule: Optional[schedule.Schedule] = Field(
        None, description='Schedule for running metadata ingestion jobs'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this dashboard service.'
    )
