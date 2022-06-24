"""
Generic helpers for the project, might be useful all over who knows...
"""


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
    e : The exception to reraise.
    args : Extra args to add to the exception.
    """
    e.args = args + e.args

    raise e.with_traceback(e.__traceback__)