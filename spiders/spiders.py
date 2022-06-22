"""
here be crawly bastards

TODO: - add data schema as input
      - add Spider as input? So this is like the meta shit that sits on top? maybe? deffo feels like what i have atm is
      something I'd want to reuse is all - maybe i make a replacement parent spider to inherit off?
"""
import string
import uuid

from scrapy import Spider
from datetime import datetime
from typing import List


class BooksToScrapeSpider(Spider):
    """Maybe its like the generic parent spider or something I'm not sure, I haven't settled on it quite yet.
    """
    def __init__(
        self,
        name: str,
        start_urls: str,
        manual_run: bool = True,
    ) -> None:
        """Initialise the class.

        Parameters
        ----------
        name : Desired name for spider.
        start_urls : Comma separated string of urls to start at, e.g 'www.google.co.uk,www.eggs.org'.
        manual_run : Set to False if the run was scheduled rather than manually triggered.
        """
        self.start_urls = start_urls
        self.manual_run = manual_run
        self.run_time = datetime.now()
        self.run_id = uuid.uuid4()

        super(BooksToScrapeSpider, self).__init__(start_urls=start_urls, name=name)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, desired_name: str) -> None:
        """Make sure the name is compatible with the desired structure.

        Parameters
        ----------
        desired_name : Ideal name you'd like for the spider, but if it's not up to snuff we'll be changing it!

        Notes
        -----
        Slight risk of being overly sweaty here, but the 'translate' method is orders of magnitude faster to run than
        alternatives according to benchmarks. Hopefully I don't forget what its doing!!!
        """
        trans_table = str.maketrans(' ', '_', string.punctuation)
        self._name = desired_name.translate(trans_table)

    @property
    def start_urls(self) -> List[str]:
        return self._start_urls

    @start_urls.setter
    def start_urls(self, urls_lst: List[str]) -> None:
        """Validate that the provided start_urls are what they say they are - they'll probs be passed in at command
        line I'd have thought.

        Parameters
        ----------
        urls_lst : The object (ideally a list of urls) which we want to validate as a list of URLs.

        Notes
        -----
        So far as I can tell, there's no real rules to what makes a URL 100% valid, so I've forgone any validation on
        the provided lists contents beyond it all needing to be of type string.
        """
        try:
            urls_lst = urls_lst.split(',')
            self._start_urls = urls_lst
        except AttributeError:
            raise TypeError("Stop using something that's not a comma separated string as a list of urls please!")

    def parse(self, response, **kwargs):
        pass


if __name__ == '__main__':
    test = BooksToScrapeSpider(start_urls='sjkdsd,sakjsjs', name='sick ass spider!')
    print(test.name)
    print(test.run_time)
    print(test.manual_run)
    print(test.run_id)
    print(test.start_urls)
