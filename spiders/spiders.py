"""
here be crawly bastards

TODO: - consider best composition for the scraping code w.r.t crawlers, scrapers, etc...
      - consider logging
      - consider data storage post scrape
      - test run is probs about time for that
"""
import uuid
import json

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
from spiders.data_saver import DataSaver


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
        folder_name: str = 'swamp',
    ) -> None:
        """Initialise the class.

        Parameters
        ----------
        name : Desired name for spider.
        start_urls : Comma separated string of urls to start at, e.g 'www.google.co.uk,www.eggs.org'.
        allowed_domains : As with start urls, a comma separated list of allowed domains, to avoid over crawling.
        manual_run : Set to False if the run was scheduled rather than manually triggered.
        folder_name : Name of folder to save output data to.

        Notes
        -----
        This got madly out of hand. hopefully its still somewhat legible. lol if not tbh...
        """
        self.name = InputTransformer.transform_name(name)
        self.start_urls = InputTransformer.transform_input_urls_list(start_urls)
        self.allowed_domains = InputTransformer.transform_input_urls_list(allowed_domains)
        self.manual_run = InputTransformer.transform_manual_run(manual_run)

        self.run_time = datetime.now().isoformat()
        self.run_id = str(uuid.uuid4())

        self.data_saver = DataSaver(name=self.name, folder_name=folder_name, sub_folders=['runs', 'data'],
                                    spider=self.__class__.__name__)
        self.data_saver.save_data(
            to_save={key: value for key, value in vars(self).items() if key != 'data_saver'},
            sub_folder='runs'
        )

        self.rules = (
            Rule(LinkExtractor(allow=("category", ), deny=("catalogue/page", )), callback="parse", follow=True),
        )

        super(BooksToScrapeShelfSpider, self).__init__(name=self.name,
                                                       start_urls=self.start_urls,
                                                       allowed_domains=self.allowed_domains,
                                                       rules=self.rules)

    def parse(self, response, **kwargs):
        """Code that will scrape shelf level data."""
        for page_rank, item in enumerate(response.xpath("//article[@class='product_pod']")):
            scraped_data = BookShelfData(
                response_url=response.url,
                run_id=self.run_id,  # used to link data to run info
                page_number=response.url,  # extracted during validation
                raw_html=item,
                item_url=item.xpath("/div/a/@href").extract()[0],
                book_title=item.xpath("/h3/a/@title").extract()[0],
                page_rank=page_rank,
                in_stock=item.xpath("/div/p[@class='instock availability']/text()").extract()[0],
                price=item.xpath("/div/p[@class='price_color']/text()").extract()[0],
                star_rating=item.xpath("/p/@class").extract()[0],
                item_rank=item.xpath("/div/a/@href").extract()[0],  # extracted from url
            )

            self.data_saver.save_data(to_save=scraped_data.json(), sub_folder='data')  # save it at this point
