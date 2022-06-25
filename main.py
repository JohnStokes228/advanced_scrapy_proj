"""
Main runner code for the project.

TODO: - bloody write some bloody code mate
"""
from spiders.spiders import BooksToScrapeSpider


if __name__ == "__main__":
    print("what did you expect, quality code?")
    test = BooksToScrapeSpider(name='sick ass spider!', start_urls='sjkdsd,sakjsjs')
    print(test.name)
    print(test.run_time)
    print(test.manual_run)
    print(test.run_id)
    print(test.start_urls)
