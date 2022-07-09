"""
Main runner code for the project.

TODO: - bloody write some bloody code mate
"""
from shitcode.spider_try_1.spiders import BooksToScrapeShelfSpider
from scrapy.crawler import CrawlerProcess


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(BooksToScrapeShelfSpider,
                  name='johnno',
                  start_urls='https://books.toscrape.com/',
                  allowed_domains='toscrape.com')
    process.start()
