"""
Fourth pass at input transforming lololol
I think my main concern is that the .transform method between the children outputs different types which isn't ideal.
Might prefer the previous setters based implementation for that reason?
"""
import string

from abc import ABC, abstractmethod
from typing import Any, Optional, List
from distutils.util import strtobool


class StrTransformer:
    """Validates inputs users will give to the project."""
    @staticmethod
    def clean_str(input_str: str) -> str:
        """Clean str in standard way.

        Parameters
        ----------
        input_str : String, but if it's not up to snuff we'll be changing it!

        Notes
        -----
        Slight risk of being overly sweaty here, but the 'translate' method is orders of magnitude faster to run than
        alternatives according to benchmarks. Hopefully I don't forget what its doing!!!

        Returns
        -------
        str
            The desired string but clean.
        """
        trans_table = str.maketrans(' ', '_', string.punctuation)
        res = (
            input_str
            .lower()
            .translate(trans_table)
            .strip('_')
        )
        return res

    @staticmethod
    def str_to_list(input_str: str) -> List[str]:
        """Split a string into a list of strings.

        Parameters
        ----------
        input_str : A string of ideally comma separated values.

        Returns
        -------
        Optional[List[str]]
            A list of strings, or raises TypeError if this is not possible.
        """
        try:
            return [vl.replace(' ', '') for vl in input_str.split(',')]
        except AttributeError:  # this might never raise if urls_lst always comes via cmd since that'll always be str?
            raise

    @staticmethod
    def str_to_boolean(input_str: str) -> bool:
        """Convert input str to boolean if possible.

        Parameters
        ----------
        input_str : Ideally a boolean transformable string.

        Returns
        -------
        bool
            The desired flag, come rain come shine.
        """
        try:
            return bool(strtobool(input_str))
        except ValueError:
            raise
