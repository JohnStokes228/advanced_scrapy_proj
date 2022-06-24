"""
here be crawly bastards

TODO: - add data schema as input
      - write the entire actual scraping code
      - consider best composition for the scraping code w.r.t crawlers, scrapers, etc...
"""
import uuid

from scrapy import Spider
from datetime import datetime

from spiders.input_validator import InputValidator


class BooksToScrapeSpider(Spider):
    def __init__(
        self,
        name: str,
        start_urls: str,
        manual_run: str = 'True',
    ) -> None:
        """Initialise the class.

        Parameters
        ----------
        name : Desired name for spider.
        start_urls : Comma separated string of urls to start at, e.g 'www.google.co.uk,www.eggs.org'.
        manual_run : Set to False if the run was scheduled rather than manually triggered.
        """
        self.start_urls = InputValidator.validate_start_urls(start_urls)
        self.name = InputValidator.validate_name(name)
        self.manual_run = InputValidator.validate_manual_run(manual_run)
        self.run_time = datetime.now()
        self.run_id = uuid.uuid4()

        super(BooksToScrapeSpider, self).__init__(start_urls=self.start_urls, name=self.name)

    def parse(self, response, **kwargs):
        pass


if __name__ == '__main__':
    test = BooksToScrapeSpider(start_urls='sjkdsd,sakjsjs', name='sick ass spider!')
    print(test.name)
    print(test.run_time)
    print(test.manual_run)
    print(test.run_id)
    print(test.start_urls)
