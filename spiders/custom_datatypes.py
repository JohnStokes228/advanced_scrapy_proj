"""
Custom datatypes for use with pydantic, will enforce validation at point of instantiation.
"""
import re

from word2number import w2n

from spiders.custom_errors import InvalidPriceError


class InStock:
    """Custom item to use in pydantic, transforms in_stock text into binary"""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, vl: str) -> bool:
        if vl.lower() != " in stock ":
            return False
        return True

    def __repr__(self):
        return super().__repr__()


class StarRating(int):
    """Custom item to use in pydantic, transforms star_rating text into float"""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, vl: str) -> int:
        return w2n.word_to_num(vl)

    def __repr__(self):
        return super().__repr__()


class Price(float):
    """Custom item to use in pydantic, transforms price text into float"""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, vl: str) -> float:
        price = re.findall("\d+\.\d+", vl)
        try:
            return float(price[0])
        except ValueError:
            raise InvalidPriceError(vl)

    def __repr__(self):
        return super().__repr__()


class PageNumber(int):
    """Custom item to use in pydantic, transforms url from books to scrape into int for page number."""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, vl: str) -> int:
        if 'page-' not in vl:
            return 1
        else:
            try:
                return int(vl.split('page-')[1].split('.')[0])
            except ValueError as e:
                reraise(e, "somethings fucked with the url here! look closer lad! look closer than you've ever looked!")

    def __repr__(self):
        return super().__repr__()


class ItemRank(int):
    """Custom item to use in pydantic, transforms item url into items rank."""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, vl: str) -> int:
        try:
            item_rank = int(
                vl
                .split('/')[4]  # tightly structured url, this is the rank fragment
                .split('_')[1]  # dont care about the genres numeric code, which follows the underscore
            )

            return item_rank
        except ValueError as e:
            reraise(e, "somethings fucked with the url here! look closer lad! look closer than you've ever looked!")

    def __repr__(self):
        return super().__repr__()