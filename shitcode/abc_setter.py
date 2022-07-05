import string

from abc import ABC, abstractmethod
from typing import Any, Optional, List
from distutils.util import strtobool


class StrTransformer(ABC):
    """Transformation of strs in set ways, ABC"""
    def __init__(self, input_string):
        self.input_string = input_string
        self.transform = input_string

    @property
    def transform(self) -> str:
        """Getter for folder_name"""
        return self._transform

    @transform.setter
    @abstractmethod  # implement this for each child - it acts as the cleaning sub function
    def transform(self, vl: str) -> None:
        pass

    def __str__(self):
        return str(self.transform)

    def __getitem__(self, item: int) -> Any:
        try:
            return self.transform[item]
        except IndexError:
            raise IndexError("index is way out of range tbh bro")

    def __bool__(self):
        try:
            return bool(self.transform)
        except ValueError:
            raise ValueError("nah can't make that a boolean fam")


class CleanStr(StrTransformer):
    """Transform str using simple cleaning methods."""
    @StrTransformer.transform.setter
    def transform(self, vl: str) -> None:
        trans_table = str.maketrans(' ', '_', string.punctuation)
        res = (
            vl
            .lower()
            .translate(trans_table)
            .strip('_')
        )
        self._transform = res


class StrToList(StrTransformer):
    """Transform str using rules for lists."""
    @StrTransformer.transform.setter
    def transform(self, vl: str) -> None:
        try:
            self._transform = [value.replace(' ', '') for value in vl.split(',')]
        except AttributeError:
            raise TypeError("Presumably the input wasn't a string! (can't see how else this would break tbh...)")


class StrToBool(StrTransformer):
    """Transform str using rules for booleans."""
    @StrTransformer.transform.setter
    def transform(self, vl: str) -> None:
        try:
            self._transform = strtobool(vl)
        except ValueError:
            raise ValueError("The boolean representation of your provided string is ambiguous :(")


if __name__ == '__main__':
    tst = str(CleanStr('True, I am a cool dude 364te90dw!!  '))
    print(tst)
    tst2 = list(StrToList('hjafhjah, faslkjfjhfajka,fhfehef'))
    for test in tst2:
        print(test)
    tst3 = bool(StrToBool('True'))
    print(tst3, type(tst3))