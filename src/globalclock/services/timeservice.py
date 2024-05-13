"""
...
"""
from _datetime import datetime
import pytz

__all__ = ["TimeService"]


class TimeService:
    """
    ...
    """

    def __init__(self):
        ...

    @staticmethod
    def get_current_time(ccode: str) -> datetime:
        try:
            # Get timezone based on country code
            timezone = pytz.country_timezones[ccode.upper()][0]
            # Get current time in the specified timezone
            current_time = datetime.now(pytz.timezone(timezone))
            return current_time
        except KeyError:
            return None
