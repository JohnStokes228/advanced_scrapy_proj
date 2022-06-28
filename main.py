"""
Main runner code for the project.

TODO: - bloody write some bloody code mate
"""
from spiders.spiders import BooksToScrapeShelfSpider
from spiders.data_validators import BookShelfData
import uuid


if __name__ == "__main__":
    print("what did you expect, quality code?")
    test = BookShelfData(
        response_url='https://books.toscrape.com/catalogue/category/books/food-and-drink_33/page-2.html',
        run_id=str(uuid.uuid4()),
        page_number='https://books.toscrape.com/catalogue/category/books/food-and-drink_33/page-2.html',
        raw_html='nah m8',
        item_url='https://books.toscrape.com/catalogue/how-to-be-a-domestic-goddess_470/index.html',
        item_rank='https://books.toscrape.com/catalogue/how-to-be-a-domestic-goddess_470/index.html',
        book_title='title of the book',
        price='a loads of cash £13.90',
        page_rank=12,
        in_stock=' in stock ',
        star_rating='star_rating Two',
    )
    print(test.json())

    test2 = BooksToScrapeShelfSpider(
        name='johnno',
        start_urls='https://books.toscrape.com/',
        allowed_domains='toscrape.com',
    )
    print(vars(test2).items())

