"""
here be crawly bastards

TODO: - add data schema as input
      - write the entire actual scraping code
      - consider best composition for the scraping code w.r.t crawlers, scrapers, etc...
"""
import uuid

from scrapy.spiders import (
    CrawlSpider,
    Rule,
)
from scrapy.linkextractors import LinkExtractor
from datetime import datetime

from spiders.input_transformer import InputTransformer
from spiders.data_validators import BooksToScrapeShelfValidator


class BooksToScrapeShelfSpider(CrawlSpider):
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
        # scrape all the shit
        # run the pipeline that will act to save the scraped stuff
        # needs logger
        # scraped_data = scrape(target_data)  # run the scrape function on targets
        scraped_data = BooksToScrapeShelfValidator(
            response_url=response.url,
            item_url='bullshit',
        )

        print(scraped_data.json())
