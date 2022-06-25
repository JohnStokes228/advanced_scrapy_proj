"""
Custom datatypes for use with pydantic, will enforce validation at point of instantiation.
"""
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
