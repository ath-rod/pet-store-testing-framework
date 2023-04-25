from datetime import datetime, timezone
from re import sub


def error_name(error) -> str:
    """
        Returns the name of the caught error for logging purposes:
        i.e. ConnectionError is returned from "HTTPConnectionPool [...] [Errno 11001] getaddrinfo failed"

            Parameters:
                error: caught exception
    """
    name_start = str(type(error)).rfind('.') + 1
    name = str(type(error))[name_start:-2]
    return name


def parsed_date(date=None):
    """
        Returns the given date in the API format, if none is given returns from now().
        i.e. From 2023-02-20T23:22:47.233129+00:00 returns 2023-02-20T23:22:47.233+0000

            Parameters:
                date: date in isoformat with utc timezone i.e. 2023-02-20T23:22:47.233129+00:00
    """
    if date is None:
        date = datetime.now(timezone.utc).isoformat()
    date = str(date)[::-1].replace(":", "", 1)[::-1]
    date = date[:date.rfind("+") - 3] + date[date.rfind("+"):]
    return date


def get_number_from_price_string(price_to_convert):
    number = sub("[^\d\.]", "", price_to_convert)
    return float(number)
