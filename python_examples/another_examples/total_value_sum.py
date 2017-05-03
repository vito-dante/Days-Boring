from typing import Iterable
from functools import reduce

def total_sum(mylist: Iterable[int]) -> int:
    total = 0
    for number in mylist:
        if number % 2 == 0:
            total += number
    return total


def example_boolean(value: bool) -> bool:
    if value:
        return False
    return True

def total_sum_best_way(mylist: Iterable[int]) -> int:
    return reduce(lambda x,y: x+y, filter(lambda x: x%2==0, mylist))
