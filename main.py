"""
Main runner code for the project.

TODO: - bloody write some bloody code mate
"""
from spiders.spiders import BooksToScrapeSpider


if __name__ == "__main__":
    print("what did you expect, quality code?")
    test = BooksToScrapeSpider(start_urls='sjkdsd,sakjsjs', name='sick ass spider!')
    print(test.name)
    print(test.run_time)
    print(test.manual_run)
    print(test.run_id)
    print(test.start_urls)
