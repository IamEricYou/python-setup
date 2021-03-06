from tqdm import tqdm
from numbers import Real
from typing import Union


def multiply_two_numbers(
    a: Union[int, Real], b: Union[int, Real]
) -> Union[int, Real]:
    return a * b


class TestClass:
    def __init__(self, variable: str) -> None:
        self.variable = variable


def test() -> None:
    test_list_appended = list()
    test_list = [i for i in range(0, 100000)]
    for i in tqdm(test_list, desc="Looping now"):
        test_list_appended.append(i)


def add(x: int, y: int) -> int:
    return x + y
