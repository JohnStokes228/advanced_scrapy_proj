"""
Main runner code for the project.

TODO: - bloody write some bloody code mate
"""
from spider_try_1.spiders import BooksToScrapeShelfSpider
from spider_try_1.data_validators import BookShelfData
import uuid
from scrapy.crawler import CrawlerProcess


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(BooksToScrapeShelfSpider,
                  name='johnno',
                  start_urls='https://books.toscrape.com/',
                  allowed_domains='toscrape.com')
    process.start()
