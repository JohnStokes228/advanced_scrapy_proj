"""
Main runner code for the project.

TODO: - bloody write some bloody code mate
"""
from spiders.spiders import BooksToScrapeShelfSpider
from spiders.data_validators import BookShelfData
import uuid
from scrapy.crawler import CrawlerProcess


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(BooksToScrapeShelfSpider,
                  name='johnno',
                  start_urls='https://books.toscrape.com/',
                  allowed_domains='toscrape.com')
    process.start()
