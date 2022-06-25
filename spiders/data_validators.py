"""
Base Models to validate scraped data with.
"""
import re
import uuid

from pydantic import (
    BaseModel,
    Field,
    UUID4,
    validator,
)
from typing import (
    Dict,
    Any,
)
from datetime import datetime
from spiders.custom_errors import InvalidURLError


class BooksToScrapeShelfValidator(BaseModel):
    """Validator for shelf level scrape data off of books to scrape dot com"""
    # Auto generated attrs
    scrape_id: UUID4 = Field(default_factory=uuid.uuid4, const=True)
    scrape_time: datetime = Field(default_factory=datetime.now, const=True)

    # Scrape level attrs
    response_url: str = Field()
    manual_run: str = Field()
    run_time: str = Field()
    run_id: str = Field()

    # item level attrs
    item_url: str = Field()
    star_rating: str = Field()
    book_title: str = Field()
    price: str = Field()
    in_stock_flag: str = Field()

    class Config:
        validate_assignment = True

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


if __name__ == '__main__':
    test = BooksToScrapeShelfValidator(
        response_url='https://books.toscrape.com/catalogue/category/books/',
        item_url='https://books.toscrape.com/catalogue/fiddler'
    )
    print(test)
    test.item_url = 'lol_nah mate'
