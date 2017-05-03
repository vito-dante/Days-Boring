from typing import Iterator

def prime(until: int) -> Iterator[int]:
    for number in range(until+1):
        if(is_prime(number)):
            yield number

def is_prime(number: int) -> bool:
    divisible = 0
    if number == 1:
        return True
    for item in range(1,number+1):
        if not(number % item):
            divisible += 1
    if divisible == 2:
        return True
    return False
