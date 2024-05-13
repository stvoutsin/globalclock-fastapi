"""Models for global_clock."""

from pydantic import BaseModel, Field
from safir.metadata import Metadata as SafirMetadata

__all__ = ["Index", "TimeData"]


class Index(BaseModel):
    """Metadata returned by the external root URL of the application.

    Notes
    -----
    As written, this is not very useful. Add additional metadata that will be
    helpful for a user exploring the application, or replace this model with
    some other model that makes more sense to return from the application API
    root.
    """

    metadata: SafirMetadata = Field(..., title="Package metadata")


class TimeData(BaseModel):
    """Metadata returned by the external root URL of the application.

    Notes
    -----
    As written, this is not very useful. Add additional metadata that will be
    helpful for a user exploring the application, or replace this model with
    some other model that makes more sense to return from the application API
    root.
    """

    country: str = Field(..., title="Timezone")
    hour: int = Field(..., title="Hours")
    minute: int = Field(..., title="Minutes")
    second: int = Field(..., title="Seconds")
    day: int = Field(..., title="Day")
    month: int = Field(..., title="Month")
    year: int = Field(..., title="Year")
