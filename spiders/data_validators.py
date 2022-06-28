"""
Base Models to validate scraped data with.
"""
import hashlib

from pydantic import (
    BaseModel,
    Field,
    UUID4,
    validator,
    Extra,
)
from typing import (
    Dict,
    Any,
    Optional,
)
from datetime import datetime

from spiders.custom_errors import InvalidURLError
from spiders.custom_datatypes import (
    Price,
    StarRating,
    InStock,
    PageNumber,
    ItemRank,
)


class BookShelfData(BaseModel):
    """Validator for shelf level scrape data off of books to scrape dot com"""
    # Auto generated attrs
    scrape_time: datetime = Field(default_factory=datetime.now, const=True)

    # Scrape level attrs
    response_url: str = Field()
    run_id: UUID4 = Field()
    page_number: PageNumber = Field()  # also fits in Custom data section

    # Raw data
    raw_html: str = Field()

    # Item level attrs
    item_url: Optional[str] = Field()
    book_title: Optional[str] = Field()
    page_rank: Optional[int] = Field()

    # Custom data - dtype changes compared to that received
    in_stock: Optional[InStock] = Field()
    price: Optional[Price] = Field()
    star_rating: Optional[StarRating] = Field()
    item_rank: Optional[ItemRank] = Field()  # ? should this be a validator?

    # Imputed attr
    genre: Optional[str] = Field(const=True)
    item_id: Optional[str] = Field(const=True)  # so queries can be generic at the shelf level

    class Config:
        validate_assignment = True
        extra = Extra.forbid

    @validator('response_url')
    def validate_response_url(
        cls,
        vl: str,
        values: Dict[str, Any],
    ) -> str:
        """Validate that response URL matches the expected structure via regex.

        Parameters
        ----------
        vl: Value to be validated.
        values: Dict of all values in class.

        Returns
        -------
        str
            The validated URL that will deffo pass validation because its valid goddammit.
        """
        if "https://books.toscrape.com/catalogue/category/books/" not in vl:
            raise InvalidURLError(url=vl, scrape_id=values["scrape_id"])
        return vl

    @validator('item_url')
    def validate_item_url(
        cls,
        vl: str,
        values: Dict[str, Any],
    ) -> str:
        """Validate that item URL matches the expected structure via regex.

        Parameters
        ----------
        vl: Value to be validated.
        values: Dict of all values in class.

        Returns
        -------
        str
            The validated URL that will deffo pass validation because its valid goddammit.
        """
        if ("https://books.toscrape.com/catalogue/" not in vl) | ("category/books" in vl):
            raise InvalidURLError(url=vl, scrape_id=values["scrape_id"])
        return vl

    @validator('genre', always=True)
    def extract_genre(
        cls,
        vl,
        values: Dict[str, Any]
    ) -> str:
        """Extract the book genre from the response URL.

        Parameters
        ----------
        values: Dict of all values in class.

        Returns
        -------
        str
            The books genre, cleaned and ready to go.
        """
        genre = (
            values["response_url"]
            .split('/')[6]  # tightly structured url, this is the genre fragment
            .split('_')[0]  # don't care about the genres numeric code, which follows the underscore
            .replace('-', ' ')
            .lower()
        )

        return genre

    @validator('item_id', always=True)
    def hash_str(
        cls,
        vl,
        values: Dict[str, Any],
    ) -> str:
        """Hash the desired column to produce the item id.

        Parameters
        ----------
        values: Dict of all values in class.

        Returns
        -------
        str
            The hashed title of the book.
        """
        return hashlib.md5(values['book_title'].encode()).hexdigest()


if __name__ == '__main__':
    test = BookShelfData(
        response_url='https://books.toscrape.com/catalogue/category/books/food-and-drink_33/page-2.html',
        run_id='',
        page_number=1,
        raw_html='nah m8',
        item_url='https://books.toscrape.com/catalogue/how-to-be-a-domestic-goddess_470/index.html',
        item_rank='https://books.toscrape.com/catalogue/how-to-be-a-domestic-goddess_470/index.html',
        book_title='title of the book',
        price='a loads of cash £13.90',
        page_rank=12,
        in_stock=' in stock ',
        star_rating='star_rating Two',
    )
    print(test)
