"""
Validation for the expected arguments to be passed into the project via command line. used to be sexier getter and
setters, but I've been forced to resort to this sorry state of affairs due to my desires for more pleasant composition.
"""
import string
from typing import List, Optional
from distutils.util import strtobool
from spiders.custom_errors import reraise


class InputTransformer:
    """Validates inputs users will give to the project."""
    @staticmethod
    def transform_name(desired_name: str) -> str:
        """Make sure the name is compatible with the desired structure.

        Parameters
        ----------
        desired_name : Ideal name you'd like for the spider, but if it's not up to snuff we'll be changing it!

        Notes
        -----
        Slight risk of being overly sweaty here, but the 'translate' method is orders of magnitude faster to run than
        alternatives according to benchmarks. Hopefully I don't forget what its doing!!!

        Returns
        -------
        str
            The desired name for the object.
        """
        trans_table = str.maketrans(' ', '_', string.punctuation)
        return desired_name.lower().translate(trans_table)

    @staticmethod
    def transform_input_urls_list(urls_lst: str) -> Optional[List[str]]:
        """Validate that the provided urls lists are what they say they are - they'll probs be passed in at command
        line I'd have thought.

        Parameters
        ----------
        urls_lst : The object (ideally a list of urls) which we want to validate as a list of URLs.

        Notes
        -----
        So far as I can tell, there's no real rules to what makes a URL 100% valid, so I've forgone any validation on
        the provided lists contents beyond it all needing to be of type string.

        Returns
        -------
        Optional[List[str]]
            A list of strings, or raises TypeError if this is not possible.
        """
        try:
            return urls_lst.split(',')
        except AttributeError:  # this might never raise if urls_lst always comes via cmd since that'll always be str?
            raise TypeError("Stop using something that's not a comma separated string as a list of urls please!")

    @staticmethod
    def transform_manual_run(manual_run: str):
        """Validate the manual run flag passed to the object.

        Parameters
        ----------
        manual_run : Ideally a boolean value indicating if the scrape was triggered manually or via schedule.

        Returns
        -------
        bool
            The desired flag, come rain come shine.
        """
        try:
            return bool(strtobool(manual_run))
        except ValueError as e:
            reraise(e, "The boolean representation of your provided value for manual_run is ambiguous :(")
