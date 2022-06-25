"""
here be crawly bastards

TODO: - write the entire actual scraping code
      - consider best composition for the scraping code w.r.t crawlers, scrapers, etc...
      - consider logging
      - consider data storage post scrape
"""
import uuid

import pydantic
from scrapy.spiders import (
    CrawlSpider,
    Rule,
)
from scrapy.linkextractors import LinkExtractor
from datetime import datetime
from pydantic import BaseModel

from spiders.input_transformer import InputTransformer
from spiders.data_validators import BookShelfData
from spiders.custom_errors import reraise


class BooksToScrapeShelfSpider(CrawlSpider):
    """
    Crawl and scrape the shelf level data from books to scrape dot com.
    """
    def __init__(
        self,
        name: str,
        start_urls: str,
        allowed_domains: str,
        manual_run: str = 'True',
    ) -> None:
        """Initialise the class.

        Parameters
        ----------
        name : Desired name for spider.
        start_urls : Comma separated string of urls to start at, e.g 'www.google.co.uk,www.eggs.org'.
        allowed_domains : As with start urls, a comma separated list of allowed domains, to avoid over crawling
        manual_run : Set to False if the run was scheduled rather than manually triggered.
        """
        self.name = InputTransformer.transform_name(name)
        self.start_urls = InputTransformer.transform_input_urls_list(start_urls)
        self.allowed_domains = InputTransformer.transform_input_urls_list(allowed_domains)
        self.manual_run = InputTransformer.transform_manual_run(manual_run)

        self.run_time = datetime.now()
        self.run_id = uuid.uuid4()

        self.rules = (
            Rule(LinkExtractor(allow=("category", ), deny=("catalogue/page", )), callback="parse", follow=True),
        )

        super(BooksToScrapeShelfSpider, self).__init__(name=self.name,
                                                       start_urls=self.start_urls,
                                                       allowed_domains=self.allowed_domains,
                                                       rules=self.rules)

    def parse(self, response, **kwargs):
        """Code that will scrape shelf level data."""
        page_number = self.get_page_number(response.url)

        for i in range(0, 5):  # this will be for el in scraped_el_lst after we get one
            scraped_data = BookShelfData(
                response_url=response.url,
                run_id=self.run_id,
                page_number=page_number,
            )

            print(scraped_data.json())  # save it at this point

    @staticmethod
    def get_page_number(response_url: str) -> int:  # feels like this belongs elsewhere bad composition 0/10
        """Get the page number out the url.

        Parameters
        ----------
        response_url: A valid URL from books to scrape

        Returns
        -------
        int
            The page number the items are being scraped off.
        """
        if 'page-' not in response_url:
            return 1
        else:
            try:
                return int(response_url.split('page-')[1].split('.')[0])
            except ValueError as e:
                reraise(e, "somethings fucked with the url here! look closer lad! look closer than you've ever looked!")
