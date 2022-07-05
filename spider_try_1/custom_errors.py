"""
All custom exceptions and associated code.
"""


class InvalidURLError(Exception):
    """Custom error for Pydantic to raise in case where URL inputs are of wrong structure."""
    def __init__(
        self,
        url: str,
        scrape_id: str,
    ):
        message = f"URL '{url}' does not match expected structure for scrape ID '{scrape_id}'"
        super().__init__(message)


class InvalidPriceError(Exception):
    """Custom error for Pydantic to raise in case where price inputs are not able to be transformed to float."""
    def __init__(
        self,
        price_str: str,
    ):
        message = f"price '{price_str}' does not contain a float."
        super().__init__(message)


def reraise(
    e: Exception,
    *args,
) -> None:
    """Re-raise an exception with extra arguments, without moving the exceptions original line.

    Notes
    -----
    pilfered wholesale from this helpful stackoverflow gent named shrewmouse by here:

    https://stackoverflow.com/questions/9157210/how-do-i-raise-the-same-exception-with-a-custom-message-in-python

    I chose his answer as it was succinct and preserved the full trace, including location of the original error. I
    hope this will make it easier to debug, but we'll see

    Parameters
    ----------
    e : The exception to re-raise.
    args : Extra args to add to the exception.
    """
    e.args = args + e.args

    raise e.with_traceback(e.__traceback__)
