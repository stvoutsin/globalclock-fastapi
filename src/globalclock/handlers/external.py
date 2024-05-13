"""Handlers for the app's external root, ``/global_clock/``."""

import json
from datetime import datetime
from typing import Annotated, Any

import pytz
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from safir.dependencies.logger import logger_dependency
from safir.metadata import get_metadata
from structlog.stdlib import Bound  Logger

from ..config import config
from ..models import Index, TimeData
from ..services.timeservice import TimeService

__all__ = ["get_index", "get_time", "external_router"]

external_router = APIRouter()
"""FastAPI router for all external handlers."""


@external_router.get(
    "/",
    description=(
        "Document the top-level API here. By default it only returns metadata"
        " about the application."
    ),
    response_model=Index,
    response_model_exclude_none=True,
    summary="Application metadata",
)
async def get_index(
    logger: Annotated[BoundLogger, Depends(logger_dependency)],
) -> Index:
    """GET ``/global_clock/`` (the app's external root).

    Customize this handler to return whatever the top-level resource of your
    application should return. For example, consider listing key API URLs.
    When doing so, also change or customize the response model in
    `globalclock.models.Index`.

    By convention, the root of the external API includes a field called
    ``metadata`` that provides the same Safir-generated metadata as the
    internal root endpoint.
    """
    # There is no need to log simple requests since uvicorn will do this
    # automatically, but this is included as an example of how to use the
    # logger for more complex logging.
    logger.info("Request for application metadata")
    metadata = get_metadata(
        package_name="global_clock",
        application_name=config.name,
    )
    return Index(metadata=metadata)


class FormattedJSONResponse(JSONResponse):
    """The same as ``fastapi.JSONResponse`` except formatted for humans."""

    def render(self, content: Any) -> bytes:
        """Render a data structure into JSON formatted for humans."""
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            sort_keys=True,
        ).encode()



@external_router.get(
    "/time/{country}",
    response_model=TimeData,
    response_model_exclude_none=True,
    response_model_exclude_unset=True,
    summary="Time in the requested timezone",
)
async def get_time(
    country: str,
) -> TimeData:

    now = TimeService.get_current_time(country)
    time_data = {
        "country" : country,
        "hour" : now.hour,
        "minute": now.minute,
        "second": now.second,
        "day" : now.day,
        "month" : now.month,
        "year": now.year,
    }

    return TimeData(**time_data)
