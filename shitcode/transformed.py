"""
Storage for teh transformed class, an experiment in dunder methods that i dont think quite landed tbh
"""
from typing import Optional, List
from distutils.util import strtobool


class Transformed:
    """Transformation of strs in set ways, no ABC."""
    def __init__(self, input_string: str):
        self.input_string = input_string

    def __str__(self) -> str:
        trans_table = str.maketrans(' ', '_', string.punctuation)
        return str(self.input_string.lower().translate(trans_table))

    def __getitem__(self, item: int) -> Optional[List[str]]:
        try:
            output_lst = [value.replace(' ', '') for value in self.input_string.split(',')]
            return output_lst[item]
        except IndexError:
            raise IndexError("index is way out of range tbh bro")
        except AttributeError:
            raise TypeError("input frankly can't have been a string m8")

    def __bool__(self) -> bool:
        try:
            return bool(strtobool(self.input_string))
        except ValueError:
            raise ValueError("The boolean representation of your provided string is ambiguous :(")


if __name__ == "__main__":
    tst4 = Transformed('djfnsnf,njnf__839273AAAAA')
    print(str(tst4))
    print(list(tst4)[1])
    tst5 = Transformed('True')
    print(bool(tst5))